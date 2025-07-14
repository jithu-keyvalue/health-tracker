"""
Tests for utility functions.
"""

from app.utils.hash import hash_file
from app.utils.auth import hash_password, verify_password

def test_password_hashing():
    """Test password hashing and verification."""
    password = "secure_password_123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrong_password", hashed)

def test_file_hash_consistency():
    """Test file hashing produces consistent results."""
    content = b"Sample health record content"
    
    # Same content should produce same hash
    hash1 = hash_file(content)
    hash2 = hash_file(content)
    assert hash1 == hash2
    
    # Different content should produce different hash
    different_content = content + b" modified"
    hash3 = hash_file(different_content)
    assert hash1 != hash3
    
    # Hash should be proper SHA-256 format
    assert len(hash1) == 64
    assert all(c in '0123456789abcdef' for c in hash1) 