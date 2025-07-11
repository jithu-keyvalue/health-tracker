📝 Notes
-----
- 🧪 Quick Start
    ```python
    # 1. Basic test
    def test_password_hashing():
        password = "secret123"
        hashed = hash_password(password)
        assert hashed != password
        assert verify_password(password, hashed) is True

    # 2. Run tests
    pytest                     # Run all tests
    pytest test_user.py       # Run specific file
    pytest -v                 # Verbose output
    pytest -k "password"      # Run tests matching name
    ```

- 🧪 Testing Tips: Building a Test Function

    1. Basic test structure:
    ```python
    # 1. Import what we need
    import pytest
    from app.schemas.user import UserCreate
    from app.services.user import signup

    # 2. Mark test as async (since we're testing async function)
    @pytest.mark.asyncio
    async def test_signup_success(mocker):
        """Test successful user signup."""
    ```

    2. Set up test data:
    ```python
    # Create data we'll use in our test
    user_data = UserCreate(
        email="test@example.com",
        password="securepass123",
        name="Test User"
    )
    ```

    3. Understanding mocks (fake objects):
    ```python
    # Real code uses database, password hashing, etc.
    # For tests, we replace these with "mocks" - fake versions that:
    # - Don't actually connect to DB or hash passwords
    # - Return predictable values we control
    # - Record how they were used so we can verify later
    ```

    4. Create mock database:
    ```python
    # Real code: db = Database(connection_string)
    # Test code: Create fake DB that can be "awaited"
    mock_db = mocker.AsyncMock()
    ```

    5. Replace real functions with mocks:
    ```python
    # When code calls get_by_email, use our mock instead
    mock_get_by_email = mocker.patch(
        "app.services.user.user_repo.get_by_email",
        return_value=None  # Pretend no user exists
    )

    # When code calls hash_password, return known value
    mock_hash_password = mocker.patch(
        "app.services.user.hash_password",
        return_value="hashed_password_123"
    )
    ```

    6. Create mock return values:
    ```python
    # Create fake user that repo will "return"
    mock_user = mocker.Mock()
    mock_user.id = "123"
    mock_user.email = user_data.email
    mock_user.name = user_data.name

    # When code calls create, return our fake user
    mock_create = mocker.patch(
        "app.services.user.user_repo.create",
        return_value=mock_user
    )
    ```

    7. Call the function we're testing:
    ```python
    # Actually run the signup function
    result = await signup(mock_db, user_data)
    ```

    8. Verify everything worked:
    ```python
    # Check that functions were called correctly
    mock_get_by_email.assert_called_once_with(mock_db, user_data.email)
    mock_hash_password.assert_called_once_with("securepass123")

    # Check create was called with right data
    mock_create.assert_called_once()
    create_args = mock_create.call_args[0]  # Arguments passed to create
    assert create_args[0] == mock_db  # First arg should be db
    assert create_args[1].email == user_data.email  # Should have same email
    assert create_args[1].password == "hashed_password_123"  # Should be hashed

    # Check the final result
    assert result["message"] == "User created"
    assert result["user"].email == user_data.email
    assert result["user"].name == user_data.name
    ```

- 🔐 Security Setup
    ```python
    # 1. Password hashing config (OWASP recommended)
    ph = PasswordHasher(
        time_cost=2,          # Iterations
        memory_cost=19456,    # 19 MiB - GPU resistant
        parallelism=1,        # Single thread
        hash_len=32,          # 32 bytes output
        type=Type.ID          # Argon2id variant
    )

    # 2. Hash and verify
    hashed = ph.hash("mypassword")
    is_valid = ph.verify(hashed, "mypassword")
    ```

- ⚙️ App Configuration
    ```python
    # 1. Define settings
    from pydantic_settings import BaseSettings, SettingsConfigDict

    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_file=".env")
        database_url: str
        secret_key: str
        redis_url: str = "redis://localhost"  # With default

    # 2. Use settings
    settings = Settings()
    db = Database(settings.database_url)
    ```