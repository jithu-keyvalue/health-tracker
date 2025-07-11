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

- 🧪 Pure Function Tests  
    Testing utility functions with known inputs/outputs.
    ```python
    # tests/test_utils.py
    def test_file_hash():
        content = b"Hello, World!"
        hash1 = hash_file(content)
        hash2 = hash_file(content)
        
        assert hash1 == hash2  # Consistent results
        assert len(hash1) == 64  # Expected format
    ```
    Key patterns:
    - Test with known inputs
    - Verify consistency
    - Check edge cases
    - Use deterministic examples

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