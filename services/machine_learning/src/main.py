from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from engine.pluggin_attach_point import get_pluggable_models
import uvicorn
from pydantic import BaseModel
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
    return available_architectures[model_name].PluggableModel().get_param_object()

class Hyperparameters(BaseModel):
    num_layers: int
    num_neurons: int
    hidden_activation_function: str
    out_activation_function: str

@app.post("/model/create/{model_name}")
def create_model(model_name: str, param: Hyperparameters):
    if model_name not in available_architectures:
        raise HTTPException(status_code=404, detail="Model not found")
    hyperparameters = param.model_dump()
    return available_architectures[model_name].PluggableModel().create(hyperparameters)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)