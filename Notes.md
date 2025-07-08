📝 Notes
--------

- 🌐 Stateless Auth
    Server doesn't store session data
    - Token contains all needed info
    - Each request is independent
    - Good for API scalability

- 🔐 JWT Authentication
    Token-based auth for stateless APIs
    ```python
    # Create token
    token = jwt.encode({"user_id": 123}, SECRET_KEY)

    # Verify token
    data = jwt.decode(token, SECRET_KEY)
    ```
    [Docs](https://jwt.io/introduction)

- 📦 JWT Structure
    Three parts: header.payload.signature
    ```python
    # Example payload
    {
      "sub": "123",           # Subject (user)
      "exp": 1516239022,     # Expiry
      "name": "John Doe"     # Custom claims
    }
    ```
    [Docs](https://jwt.io/introduction#payload)

- ✍️ JWT Signing
    Prevents token tampering
    ```python
    # header.payload.signature
    # Signature = hash(header + payload + SECRET_KEY)
    
    # If payload changed, signature won't match
    # Only server with SECRET_KEY can create valid tokens
    ```
    [Docs](https://jwt.io/introduction#signature)

- ⏰ Token Expiry
    Tokens should expire for security
    ```python
    # Add expiry time
    token = jwt.encode({
        "user_id": 123,
        "exp": datetime.now() + timedelta(minutes=15)
    }, SECRET_KEY)
    ```
    [Docs](https://pyjwt.readthedocs.io/en/latest/usage.html#expiration-time-claim-exp)

- 🔒 Password Hashing
    Never store raw passwords
    ```python
    # Hash password
    hashed = pwd_context.hash("secret123")

    # Verify password
    is_valid = pwd_context.verify("secret123", hashed)
    ```
    [Docs](https://passlib.readthedocs.io/en/stable/narr/quickstart.html)

- 🛡️ Auth Headers
    Send tokens in Authorization header
    ```python
    # Frontend
    headers = {"Authorization": f"Bearer {token}"}

    # Backend
    token = request.headers["Authorization"].split(" ")[1]
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

- 💾 Client Storage
    Store tokens for session persistence
    ```javascript
    // Save token
    localStorage.setItem("token", access_token)

    // Use in requests
    const token = localStorage.getItem("token")
    if (token) {
        headers.Authorization = `Bearer ${token}`
    }
    ```
