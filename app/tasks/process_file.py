import os
import json
from openai import OpenAI
import logging
from celery import Celery
from app.db.session import SessionLocal
from app.db.models import UploadedFile
from app.db.models import Observation
from datetime import datetime, timezone

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

celery_app = Celery(
    "worker",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0")
)

logger = logging.getLogger(__name__)

@celery_app.task
def process_uploaded_file(file_hash: str, content: str, user_id: str):
    db = SessionLocal()
    try:
        logger.info(f"Processing file hash={file_hash} for user={user_id}")

        # Prepare prompt for OpenAI
        prompt = (
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

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        raw = response.choices[0].message.content.strip()
        if raw.startswith("```json"):
            raw = raw.strip("```json").strip("```").strip()

        records = json.loads(raw)

        # Save file entry (since already deduped at API level)
        file = UploadedFile(user_id=user_id, hash=file_hash)
        db.add(file)
        db.commit()
        db.refresh(file)

        for rec in records:
            for metric in ["hb", "tsh", "glucose", "cholesterol"]:
                value = rec.get(metric)
                if value is not None:
                    obs = Observation(
                        date=datetime.fromisoformat(rec["date"]).date(),
                        metric=metric,
                        value=float(value),
                        user_id=user_id,
                        file_id=file.id
                    )
                    db.add(obs)

        db.commit()
        logger.info(f"✅ Done processing file {file_hash}")
    except Exception:
        logger.exception("❌ Error while processing file")
    finally:
        db.close()