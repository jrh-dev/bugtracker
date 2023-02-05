import logging
from fastapi import FastAPI
from api import endpoints

logging.basicConfig(filename="api.log", level=logging.INFO)

app = FastAPI()

app.include_router(endpoints.router)
