from fastapi import FastAPI
from datetime import datetime

from app.graphql.entry import graphql_app

app = FastAPI()

app.include_router(graphql_app, prefix="/query")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ping")
async def ping():
    return {
        "version": app.version,
        "docs": app.docs_url,
        "name": "FastAPI strawberry graphQL",
        "now": datetime.now(),
    }
    
    
