import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello_world():
    return "world!"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
