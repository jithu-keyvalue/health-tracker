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
    Using pytest-asyncio and mocking.
    ```python
    @pytest.mark.asyncio
    async def test_signup(mocker):
        # Mock dependencies
        mock_db = mocker.AsyncMock()
        mocker.patch(
            "app.services.user.user_repo.get_by_email",
            return_value=None
        )
        
        # Test the service
        result = await signup(mock_db, user_data)
        assert result["message"] == "User created"
    ```
    Key patterns:
    - Mark tests with @pytest.mark.asyncio
    - Mock async dependencies
    - Test both success and error paths

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