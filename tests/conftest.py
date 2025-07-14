"""
Test fixtures for health tracker app.
"""

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from app.schemas.user import UserCreate
from app.utils.auth import hash_password, create_access_token

@pytest.fixture
def valid_user_data():
    """User data for testing signup/login functionality."""
    return UserCreate(
        email="test@example.com",
        password="secure_password_123",
        name="Test User"
    )

@pytest.fixture
async def test_user_with_password():
    """User with hashed password for login testing."""
    token_data = {"sub": "test-user-456"}
    token = create_access_token(token_data)
    
    user = AsyncMock()
    user.id = "test-user-456"
    user.email = "fixture@example.com"
    user.name = "Fixture User"
    user.password_hash = hash_password("correct_password")
    user.token = token
    
    return user 