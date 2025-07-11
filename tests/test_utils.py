from app.utils.hash import hash_file

def test_file_hash_different_content():
    """Test that different content produces different hashes."""
    content1 = b"Hello, World!"
    content2 = b"Hello, world!"  # Different case
    
    hash1 = hash_file(content1)
    hash2 = hash_file(content2)
    
    assert hash1 != hash2
    assert len(hash1) == 64  # SHA-256 produces 64 char hex string
    assert len(hash2) == 64

def test_file_hash_same_content():
    """Test that same content produces same hash."""
    content = b"Hello, World!"
    
    hash1 = hash_file(content)
    hash2 = hash_file(content)
    
    assert hash1 == hash2
    
def test_file_hash_empty_content():
    """Test hashing empty content."""
    empty_hash = hash_file(b"")
    
    # Known SHA-256 hash of empty string
    expected = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert empty_hash == expected 