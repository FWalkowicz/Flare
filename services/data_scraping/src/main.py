import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from kaggle_scrapping import KaggleScrapping

# Initialize the FastAPI app
app = FastAPI()

# Initialize the KaggleScrapping instance to interact with Kaggle API
scraper = KaggleScrapping()

# Define the origins that are allowed to make cross-origin requests (CORS)
cors_origins = ["*"]

# Add CORS middleware to the FastAPI app to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/show_datasets/{name}")
def show_datasets(name: str):
    """
    Endpoint to search for datasets on Kaggle by name and return the results in JSON format.

    :param name: str
        The name or keyword to search for datasets on Kaggle.
    :return: JSON
        A JSON list of datasets that match the search criteria, including the dataset reference,
        subtitle, and available .csv files.
    """
    datasets_list = scraper.search(name)
    datasets_json = datasets_list.to_json(orient="records")
    parsed = json.loads(datasets_json)
    return parsed


class Dataset_to_download(BaseModel):
    """
    Data model to define the structure of the data required for downloading a dataset.

    Attributes
    ----------
    ref_name : str
        The reference name of the dataset on Kaggle.
    file_name : str
        The name of the specific file within the dataset to download.
    """
    ref_name: str
    file_name: str


@app.post("/download")
def download(dataset_info: Dataset_to_download):
    """
    Endpoint to download a specified CSV file from a Kaggle dataset and return the first 25 rows in JSON format.

    :param dataset_info: Dataset_to_download
        A Pydantic model containing the reference name of the Kaggle dataset and the file name to download.
    :return: JSON
        A JSON list of the first 25 rows of the downloaded dataset.
    """
    print(dataset_info)
    dataset = scraper.download(dataset_name=dataset_info.ref_name, file_name=dataset_info.file_name).head(25)
    dataset_json = dataset.to_json(orient="records")
    parsed = json.loads(dataset_json)
    return parsed
