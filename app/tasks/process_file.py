import os
import json
from openai import OpenAI
import logging
from celery import Celery
from app.db.session import AsyncSessionLocal
from app.db.models import UploadedFile, Observation
from datetime import datetime
from app.core.settings import settings
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

client = OpenAI(api_key=settings.OPENAI_API_KEY)

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL
)

logger = logging.getLogger(__name__)

@celery_app.task
def process_uploaded_file(file_hash: str, content: str, user_id: str):
    asyncio.run(_process_lab_report_async(file_hash, content, user_id))

async def _process_lab_report_async(file_hash: str, content: str, user_id: str):
    async with AsyncSessionLocal() as db:
        try:
            await _process_file_logic(db, file_hash, content, user_id)
        except Exception:
            logger.exception("❌ Error while processing file")
            await db.rollback()
            raise

async def _process_file_logic(db: AsyncSession, file_hash: str, content: str, user_id: str):
    logger.info(f"Processing file hash={file_hash} for user={user_id}")
    
    # Extract health data from content
    records = await _extract_health_data(content)
    
    # Save file entry
    file = UploadedFile(user_id=user_id, hash=file_hash)
    db.add(file)
    await db.commit()
    await db.refresh(file)
    
    # Create and save observations
    observations = _create_observations(records, user_id, file.id)
    db.add_all(observations)
    await db.commit()
    
    logger.info(f"✅ Done processing file {file_hash}")

async def _extract_health_data(content: str) -> list:
    """Extract health metrics from lab report content using OpenAI."""
    prompt = _build_extraction_prompt(content)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    return _parse_openai_response(response)

def _build_extraction_prompt(content: str) -> str:
    """Build the prompt for OpenAI health data extraction."""
    return (
        "Extract the following metrics from the lab report content below:\n"
        "- Date (format: YYYY-MM-DD)\n"
        "- Hemoglobin (Hb) in g/dL\n"
        "- TSH in μIU/mL\n"
        "- Glucose in mg/dL\n"
        "- Cholesterol in mg/dL\n"
        "Return them as valid JSON — an array of objects like this:\n"
        "[{\"date\": \"YYYY-MM-DD\", \"hb\": 13.5, \"tsh\": 2.4, \"glucose\": 110, \"cholesterol\": 180}]\n"
        "Do NOT return percentages or any other units. Use standard units only.\n\n"
        f"Report:\n{content}"
    )

def _parse_openai_response(response) -> list:
    """Parse OpenAI response and return health data records."""
    raw = response.choices[0].message.content.strip()
    if raw.startswith("```json"):
        raw = raw.strip("```json").strip("```").strip()
    
    return json.loads(raw)

def _create_observations(records: list, user_id: str, file_id: str) -> list:
    """Create Observation objects from health data records."""
    observations = []
    
    for record in records:
        for metric in ["hb", "tsh", "glucose", "cholesterol"]:
            value = record.get(metric)
            if value is not None:
                obs = Observation(
                    date=datetime.fromisoformat(record["date"]).date(),
                    metric=metric,
                    value=float(value),
                    user_id=user_id,
                    file_id=file_id
                )
                observations.append(obs)
    
    return observations