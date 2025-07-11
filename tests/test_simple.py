from app.utils.auth import hash_password

# The simplest possible test
def test_true_is_true():
    assert True is True

def test_password_hashing():
    password = "secret123"
    hashed = hash_password(password)
    assert hashed != password  # Should be hashed
    assert len(hashed) > 20    # Should be long enough 