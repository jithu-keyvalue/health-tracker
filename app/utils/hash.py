import hashlib

def hash_file(contents: bytes) -> str:
    return hashlib.sha256(contents).hexdigest()
