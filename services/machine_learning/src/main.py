from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from engine.plugginAttachPoint import get_pluggable_models
#dev flags

DS_BACKEND_ADRESS = 'http://192.168.1.81:8081'

enforce_cors = True

available_architectures = get_pluggable_models()

#lifecycle logic

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting...")
    yield
    print("Shutting down...")


app = FastAPI()

cors_origins = ["*"]

if enforce_cors:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/model/list")
def list_available_models():
    return [
        model_name for model_name in available_architectures
    ]

@app.get("/model/create")
def get_architecture_params(model_name: str):
    return available_architectures[model_name].PluggableModel().get_param_object