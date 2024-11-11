from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def root():
    return {"message": "Hello World"}
