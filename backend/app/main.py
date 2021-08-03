import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "test"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
