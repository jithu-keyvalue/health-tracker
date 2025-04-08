from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "Guest"):
    return f"Hello, name!"
