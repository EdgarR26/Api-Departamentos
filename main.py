from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel
from typing import List

# Configuración de FastAPI
app = FastAPI()

client = MongoClient("mongodb+srv://eramirez13:SuSerNFNzHMSKB1a@desarrolloweb.nclk9.mongodb.net/?retryWrites=true&w=majority&appName=Desarrolloweb")
db = client["Desarrolloweb"]
collection = db["Departamentos"]

# Modelos de Pydantic
class Departamento(BaseModel):
    nombre: str
    capital: str
    poblacion: int
    area_km2: int
    municipios: List[str]

# Obtener la lista de todos los departamentos
@app.get("/departamentos", response_model=List[Departamento])
async def obtener_departamentos():
    departamentos = list(collection.find({}, {"_id": 0}))
    return departamentos

# Obtener los municipios de un departamento específico
@app.get("/departamentos/{nombre_departamento}/municipios")
async def obtener_municipios(nombre_departamento: str):
    departamento = collection.find_one({"nombre": nombre_departamento}, {"_id": 0, "municipios": 1})
    if departamento:
        return departamento["municipios"]
    else:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")

# Obtener la información detallada de un departamento específico
@app.get("/departamentos/{nombre_departamento}", response_model=Departamento)
async def obtener_informacion_departamento(nombre_departamento: str):
    departamento = collection.find_one({"nombre": nombre_departamento}, {"_id": 0})
    if departamento:
        return departamento
    else:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")

