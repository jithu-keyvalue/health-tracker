import pytest
from fastapi import HTTPException
from app.schemas.user import UserCreate
from app.services.user import signup

@pytest.mark.asyncio
async def test_signup_success(mocker):
    """Test successful user signup."""
    # Mock data
    user_data = UserCreate(
        email="test@example.com",
        password="securepass123",
        name="Test User"
    )
    
    # Mock database session
    mock_db = mocker.AsyncMock()
    
    # Mock repository calls
    mocker.patch(
        "app.services.user.user_repo.get_by_email",
        return_value=None  # No existing user
    )
    
    created_user = mocker.Mock()
    created_user.id = "123"
    created_user.email = user_data.email
    created_user.name = user_data.name
    
    mocker.patch(
        "app.services.user.user_repo.create",
        return_value=created_user
    )
    
    # Call signup
    result = await signup(mock_db, user_data)
    
    # Verify response
    assert result["message"] == "User created"
    assert result["user"].email == user_data.email
    assert result["user"].name == user_data.name

@pytest.mark.asyncio
async def test_signup_email_exists(mocker):
    """Test signup with existing email."""
    # Mock data
    user_data = UserCreate(
        email="exists@example.com",
        password="securepass123",
        name="Test User"
    )
    
    # Mock database session
    mock_db = mocker.AsyncMock()
    
    # Mock repository to return existing user
    mocker.patch(
        "app.services.user.user_repo.get_by_email",
        return_value=mocker.Mock()  # Existing user
    )
    
    # Verify raises HTTP 400
    with pytest.raises(HTTPException) as exc_info:
        await signup(mock_db, user_data)
    
    assert exc_info.value.status_code == 400
    assert "Email already registered" in exc_info.value.detail 