📝 Notes  
--------

- 🌐 CORS (Cross-Origin Resource Sharing)  
  By default, a website can only make requests to the same domain it came from. 
  
  - If your HTML is served from one place (like localhost:8000) and tries to talk to an API on another (like localhost:8001), the browser blocks it unless the server explicitly allows it. 

  - This prevents malicious websites from secretly calling your APIs using a user’s browser.


- CORS: example
    - You’re logged into your account on aic.com (AI Coach backend).
    - You visit a random blog at shadytricks.com.
    - That site secretly runs JavaScript to call aic.com/api/users/231 (maybe to delete your account).
    - Your browser sees that this request is from a different origin (shadytricks.com → aic.com) and pauses it.
    - It asks aic.com via a preflight request: “Should I allow requests from shadytricks.com?”
    - If aic.com replies with Access-Control-Allow-Origin: shadytricks.com, the browser lets it through.
    - If not (which is the secure default), the browser blocks it.
    - CORS makes sure only trusted origins (like app.aic.com) can access protected APIs on your behalf.

- origin - protocol + domain + port  
    - http://localhost:8000 and http://localhost:8001 are distinct origins  
    - http://localhost:8000 & file://... (null origin) are also different origins.

- 🌍 http.server  
Used to serve static frontend files (like signup.html) via a local web server. Required for browser to treat it as a real website.

  ```bash
  cd ui
  python3 -m http.server 8001
  ```

- 🧠 JS fetch()  
  Used to make API calls from the browser.

  ```javascript
  fetch("/observations", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ date, hb })
  });
  ```


- 🪵 Logging  
  - Use `logging` instead of `print()` — it's structured, configurable, and works in production.

  ```python
  import logging
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(__name__)
  logger.info("User 6242 created request 2314")
  ```

  ```bash
  2025-04-09 14:24:11,024 [ERROR] User 6242 created request 2314.
  ```

- 📊 Log Levels:  
  - DEBUG	Internal details (dev only)
  - INFO	Normal app events (requests, saves)
  - WARNING	Something odd, but not broken
  - ERROR	Failures that need attention


- 🛠️ Why not print()?  
  - Only prints to local terminal  
  - Not captured by log files or cloud log collectors  
  - `logging` is structured and works everywhere