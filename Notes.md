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
    mock_db = AsyncMock()
    ```

    5. Mock the user repository:
    ```python
    # Create mock repository
    mock_user_repo = AsyncMock()
    
    # Mock that user doesn't exist (no duplicate email)
    mock_user_repo.get_by_email.return_value = None
    ```

    6. Create mock return values:
    ```python
    # Create fake user that repo will "return"
    mock_user = AsyncMock()
    mock_user.id = "user-123"
    mock_user.email = user_data.email
    mock_user.name = user_data.name

    # Mock user creation
    mock_user_repo.create.return_value = mock_user
    ```

    7. Replace real functions with mocks:
    ```python
    # Replace the real repository with our mock
    import app.services.user as user_service
    user_service.user_repo = mock_user_repo
    ```

    8. Call the function we're testing:
    ```python
    # Actually run the signup function
    result = await signup(mock_db, user_data)
    ```

    9. Verify everything worked:
    ```python
    # Check that functions were called correctly
    mock_user_repo.get_by_email.assert_called_once_with(mock_db, user_data.email)
    mock_user_repo.create.assert_called_once()

    # Check the final result
    assert result["message"] == "User created"
    assert result["user"].email == user_data.email
    assert result["user"].name == user_data.name
    ```

- 🧪 Test Fixtures (conftest.py)
    ```python
    # 1. Basic fixture - reusable test data
    @pytest.fixture
    def valid_user_data():
        return UserCreate(
            email="test@example.com",
            password="secure_password_123",
            name="Test User"
        )

    # 2. Use fixtures in tests
    def test_signup_duplicate_email(valid_user_data):
        # Mock setup...
        with pytest.raises(HTTPException):
            await signup(mock_db, valid_user_data)

    def test_signup_success(valid_user_data):
        # Same fixture, different test
        result = await signup(mock_db, valid_user_data)
        assert result["user"].email == valid_user_data.email
    ```

- 🧪 Fixtures vs Mocks
    ```python
    # Fixtures: Reusable test data/setup
    @pytest.fixture
    def valid_user_data():
        return UserCreate(email="test@example.com", ...)

    # Mocks: Replace external dependencies (our approach)
    mock_user_repo = AsyncMock()
    import app.services.user as user_service
    user_service.user_repo = mock_user_repo

- 🧪 Async Fixtures
    ```python
    # For async fixtures, use @pytest_asyncio.fixture
    @pytest_asyncio.fixture
    async def async_user():
        return AsyncMock()
    
    # Regular fixtures use @pytest.fixture
    @pytest.fixture
    def user_data():
        return {"email": "test@example.com"}
    ```

- 🧪 Mock Methods
    ```python
    # Direct assignment - simple, explicit
    user_service.user_repo = mock_user_repo

    # @patch decorator - automatic, REVERSE order injection
    @patch('app.services.user.user_repo')      # Second parameter
    @patch('app.services.user.hash_password')  # First parameter
    def test_with_patches(mock_hash, mock_repo):
        # Parameters injected in REVERSE order of decorators
        mock_hash.return_value = "hashed_123"
        mock_repo.get_by_email.return_value = None
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