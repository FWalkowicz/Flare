import json
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kaggle_scrapping import KaggleScrapping

app = FastAPI()
scrapper = KaggleScrapping()
cors_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/show_datasets/{name}")
def show_datasets(name: str):
    datasets = scrapper.search(name)
    datasets_json = datasets.to_json(orient="records")
    parsed = json.loads(datasets_json)
    return parsed
