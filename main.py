from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return{
        "message":"welcometo the app"
    }


@app.get("/welcome")
def welcome():
    return{
        "message":"welcome to mini RAG"
    }