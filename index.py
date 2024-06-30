from fastapi import FastAPI


app = FastAPI() # Create an instance of FastAPI 


@app.get("/ping")
def delete_todo():
    return {"ping": "pong"}

