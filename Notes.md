📝 Notes
-----
- 🧪 Testing Foundation  
    Minimal pytest setup for initial tests.
    ```python
    # tests/test_simple.py - Basic structure
    def test_true_is_true():
        assert True  # Verify test runner works
    
    def test_password_hashing():
        password = "secret123"
        hashed = hash_password(password)
        assert hashed != password  # Never store plaintext
    ```
    
    Configuration in pytest.ini:
    ```ini
    [pytest]
    pythonpath = .  # Enable imports from project root
    ```
    
    Run tests: `pytest -v tests/test_simple.py`

- 🧪 Testing Async Services  
    Testing FastAPI services without real database.
    ```python
    @pytest.mark.asyncio  # Enable async test
    async def test_signup(mocker):
        # 1. Setup test data
        user_data = UserCreate(
            email="test@example.com",
            name="Test User"
        )
        
        # 2. Create mocks
        mock_db = mocker.AsyncMock()  # Fake DB session
        mock_get_by_email = mocker.patch(  # Fake repo call
            "app.services.user.user_repo.get_by_email",
            return_value=None  # No existing user
        )
        
        # 3. Run the function
        result = await signup(mock_db, user_data)
        
        # 4. Verify behavior
        mock_get_by_email.assert_called_once()  # Called once
        assert result["message"] == "User created"
    ```
    Why Mock?
    - No real database needed
    - Tests run fast
    - No cleanup required
    - Can test error cases easily
    
    Common Patterns:
    - @pytest.mark.asyncio for async tests
    - mocker.AsyncMock() for async dependencies
    - mocker.patch() to replace functions
    - assert_called_once() to verify calls
    - pytest.raises() for errors

- 🔐 Password Hashing  
    Using Argon2id (OWASP 2024 recommendation).
    ```python
    # app/utils/auth.py
    from argon2 import PasswordHasher, Type
    
    ph = PasswordHasher(
        time_cost=2,          # Iterations
        memory_cost=19456,    # 19 MiB - GPU resistant
        parallelism=1,        # Single thread
        hash_len=32,          # 32 bytes output
        type=Type.ID          # Argon2id variant
    )
    ```
    Why Argon2id:
    - Memory-hard: Resistant to GPU attacks
    - Time-cost: Adjustable iteration count
    - Modern: Preferred over bcrypt/PBKDF2
    @https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

- ⚙️ Settings Pattern  
    Modern Pydantic v2 configuration.
    ```python
    # app/core/settings.py
    from pydantic_settings import BaseSettings, SettingsConfigDict
    
    class Settings(BaseSettings):
        model_config = SettingsConfigDict(env_file=".env")
        # Type-checked environment variables
        secret_key: str
        database_url: str
    ```
    Key changes:
    - No more nested Config class
    - Runtime type validation
    - Automatic .env loading