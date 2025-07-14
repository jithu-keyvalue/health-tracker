"""
Tests for health tracker app functionality.
"""

import pytest
from app.services.user import signup, login
from app.schemas.user import UserLogin
from app.utils.auth import hash_password
from fastapi import HTTPException
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_signup_duplicate_email(valid_user_data):
    """Test signup prevents duplicate emails."""
    mock_db = AsyncMock()
    mock_user_repo = AsyncMock()
    
    # Mock that user already exists
    mock_user_repo.get_by_email.return_value = {"email": valid_user_data.email}
    
    import app.services.user as user_service
    user_service.user_repo = mock_user_repo
    
    with pytest.raises(HTTPException) as exc_info:
        await signup(mock_db, valid_user_data)
    
    assert exc_info.value.status_code == 400
    assert "Email already registered" in str(exc_info.value.detail)

@pytest.mark.asyncio
async def test_signup_success(valid_user_data):
    """Test successful user signup with step-by-step mocking."""
    # 1. Create mock database (fake DB that can be "awaited")
    mock_db = AsyncMock()
    
    # 2. Mock the user repository
    mock_user_repo = AsyncMock()
    
    # 3. Mock that user doesn't exist (no duplicate email)
    mock_user_repo.get_by_email.return_value = None
    
    # 4. Create fake user that repo will "return"
    mock_user = AsyncMock()
    mock_user.id = "user-123"
    mock_user.email = valid_user_data.email
    mock_user.name = valid_user_data.name
    
    # 5. Mock user creation
    mock_user_repo.create.return_value = mock_user
    
    # 6. Replace real functions with mocks
    import app.services.user as user_service
    user_service.user_repo = mock_user_repo
    
    # 7. Call the function we're testing
    result = await signup(mock_db, valid_user_data)
    
    # 8. Verify everything worked
    # Check that functions were called correctly
    mock_user_repo.get_by_email.assert_called_once_with(mock_db, valid_user_data.email)
    mock_user_repo.create.assert_called_once()
    
    # Check the final result
    assert result["message"] == "User created"
    assert result["user"].email == valid_user_data.email
    assert result["user"].name == valid_user_data.name

@pytest.mark.asyncio
async def test_login_invalid_credentials(valid_user_data):
    """Test login with wrong password."""
    mock_db = AsyncMock()
    mock_user_repo = AsyncMock()
    
    # Mock user exists but password is wrong
    mock_user = AsyncMock()
    mock_user.id = "user-123"
    mock_user.email = valid_user_data.email
    mock_user.password_hash = hash_password("different_password")
    mock_user_repo.get_by_email.return_value = mock_user
    
    import app.services.user as user_service
    user_service.user_repo = mock_user_repo
    
    login_data = UserLogin(
        email=valid_user_data.email,
        password=valid_user_data.password  # Wrong password
    )
    
    with pytest.raises(HTTPException) as exc_info:
        await login(mock_db, login_data)
    
    assert exc_info.value.status_code == 401
    assert "Invalid credentials" in str(exc_info.value.detail)

@pytest.mark.asyncio
async def test_login_success(test_user_with_password):
    """Test successful login with correct credentials."""
    mock_db = AsyncMock()
    mock_user_repo = AsyncMock()
    
    # Mock user exists with correct password
    mock_user_repo.get_by_email.return_value = test_user_with_password
    
    import app.services.user as user_service
    user_service.user_repo = mock_user_repo
    
    login_data = UserLogin(
        email=test_user_with_password.email,
        password="correct_password"
    )
    
    result = await login(mock_db, login_data)
    
    assert result.access_token is not None
    assert result.token_type == "bearer" 