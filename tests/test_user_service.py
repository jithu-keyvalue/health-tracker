import pytest
from fastapi import HTTPException
from app.schemas.user import UserCreate
from app.services.user import signup

@pytest.mark.asyncio
async def test_signup_success(mocker):
    """Test successful user signup."""
    # Test data
    user_data = UserCreate(
        email="test@example.com",
        password="securepass123",
        name="Test User"
    )
    
    # Mock DB session
    mock_db = mocker.AsyncMock()
    
    # Mock get_by_email to return None (no existing user)
    mock_get_by_email = mocker.patch(
        "app.services.user.user_repo.get_by_email",
        return_value=None
    )
    
    # Mock hash_password to return predictable hash
    mock_hash_password = mocker.patch(
        "app.services.user.hash_password",
        return_value="hashed_password_123"
    )
    
    # Prepare mock user that create will return
    mock_created_user = mocker.Mock()
    mock_created_user.id = "123"
    mock_created_user.email = user_data.email
    mock_created_user.name = user_data.name
    
    # Mock create to return our prepared user
    mock_create = mocker.patch(
        "app.services.user.user_repo.create",
        return_value=mock_created_user
    )
    
    # Call the function we're testing
    result = await signup(mock_db, user_data)
    
    # Verify:
    # 1. Checked for existing user
    mock_get_by_email.assert_called_once_with(mock_db, user_data.email)
    
    # 2. Password was hashed
    mock_hash_password.assert_called_once_with("securepass123")
    
    # 3. User was created with correct data
    mock_create.assert_called_once()
    create_args = mock_create.call_args[0]
    assert create_args[0] == mock_db  # First arg should be db session
    assert create_args[1].email == user_data.email  # Email matches
    assert create_args[1].password == "hashed_password_123"  # Password was hashed
    
    # 4. Response has correct format and data
    assert result["message"] == "User created"
    assert result["user"].email == user_data.email
    assert result["user"].name == user_data.name

@pytest.mark.asyncio
async def test_signup_email_exists(mocker):
    """Test signup with existing email - should fail."""
    user_data = UserCreate(
        email="exists@example.com",
        password="securepass123",
        name="Test User"
    )
    
    # Mock DB session
    mock_db = mocker.AsyncMock()
    
    # Mock get_by_email to return an existing user
    mock_get_by_email = mocker.patch(
        "app.services.user.user_repo.get_by_email",
        return_value=mocker.Mock()  # Any non-None value = user exists
    )
    
    # Mock create - should never be called
    mock_create = mocker.patch(
        "app.services.user.user_repo.create"
    )
    
    # Function should raise HTTPException
    with pytest.raises(HTTPException) as exc_info:
        await signup(mock_db, user_data)
    
    # Verify:
    # 1. Checked for existing user
    mock_get_by_email.assert_called_once_with(mock_db, user_data.email)
    
    # 2. Never tried to create user
    mock_create.assert_not_called()
    
    # 3. Raised correct error
    assert exc_info.value.status_code == 400
    assert "Email already registered" in exc_info.value.detail 