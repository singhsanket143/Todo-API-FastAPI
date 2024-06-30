from fastapi import FastAPI


app = FastAPI() # Create an instance of FastAPI 


@app.get("/ping")
def check_ping():
    return {"ping": "pong"}

