📝 Notes
--------

- 📦 JWT (JSON Web Token)  
  Used for authentication and authorization in web applications. Tokens are signed and contain claims about the user.

  - Structure: A JWT consists of three parts: Header, Payload, and Signature.
  - Base64-encoded: Both the header and payload are Base64 encoded for transport, but not encrypted.
  - Signature: This ensures data integrity.

- 🎫 Bearer Token  
  - Authentication token passed in the Authorization header of an HTTP request.
  - Access Control: Whoever holds the token can use it to access protected resources.

  Example header:
  ```javascript
  Authorization: Bearer <your_token>
  ```


- 🔑 Access Token  
A JWT used to access protected resources. Contains claims like sub (subject) and exp (expiration).

  - sub: Typically stores the user ID or unique identifier (e.g., UUID or user ID).
  - exp: Token expiration; should be set to limit the token's lifespan (e.g., 15 minutes).

  Example to create the access token:  
  ```python
  access_token = create_access_token(data={"sub": str(db_user.id)})
  ```

- 🔒 Security & Hashing  
  bcrypt & passlib: Used for password hashing. Storing passwords as plain-text is not secure.

  ```python
  from passlib.context import CryptContext
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  hashed_password = pwd_context.hash("password123")
  ```

  Password Verification: Use pwd_context.verify() to verify a password against the stored hash.
  ```python
  pwd_context.verify("password123", hashed_password)
  ```

- 🔑 JWT Token Handling  
  jwt.encode(): Creates and signs the JWT token with the payload (data) and secret key.

  ```python
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  ```

  jwt.decode(): Decodes the JWT token and validates its signature using the secret key.

  ```python
  payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  ```

- Why Signing Is Useful:  

  - Authenticity: It ensures that the token data was created by someone with the secret key (e.g., the server).

  - Prevents Tampering: If anyone changes the data in the token, the signature will no longer be valid, so the server can reject the altered token.

- 🚨 FastAPI Specific  
  HTTPException: Raises error responses with appropriate status codes.

  ```python
  raise HTTPException(status_code=400, detail="Invalid credentials")
  ```

- Status Codes: Common status codes used in authentication.
  - 401: Unauthorized (invalid or missing token).
  - 404: Not Found (e.g., user not found).

  Example:
    ```python
    raise HTTPException(status_code=401, detail="Invalid token")
    ```

- 🔐 Session Management  
  - Stateless authentication: JWT tokens store all session data, so the server doesn't need to remember user states.
  - LocalStorage: JWT token is stored in the browser's localStorage to maintain user sessions across requests.
  ```javascript
  localStorage.setItem("token", access_token);
  ```

- 🔄 UUID  
    UUID (Universally Unique Identifier): Used for unique identifiers in distributed systems.

    Example for generating a UUID:

    ```python
    import uuid
    user_id = uuid.uuid4()
    ```

- 🧳 Session Handling  
    Session: Use SQLAlchemy's Session to interact with the database.

    ```python
    db_user = db.query(User).filter(User.email == email).first()
    ```

- 💾 Local Storage  
    Local Storage: Stores the JWT token in the browser to keep users logged in.
    Checking Login: The presence of a token in localStorage indicates if the user is logged in.

  ```javascript
  if(localStorage.getItem("token")) { ... }
  ```
