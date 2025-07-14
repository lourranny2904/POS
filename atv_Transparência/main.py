from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS (opcional, útil para frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://portaldatransparencia.gov.br/api-de-dados"
TOKEN = os.getenv("TOKEN_TRANSPARENCIA")

HEADERS = {
    "Authorization": f"Token {TOKEN}"
}

# --- ENDPOINTS ---

@app.get("/bolsa-familia")
async def bolsa_familia(cpf: str, mesAno: str):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/bolsa-familia-por-cpf"
        params = {"cpfBeneficiario": cpf, "mesAno": mesAno}
        r = await client.get(url, headers=HEADERS, params=params)
        return r.json()

@app.get("/bolsa-familia-municipio")
async def bolsa_familia_municipio(codigoIbge: str, mesAno: str):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/bolsa-familia-por-municipio"
        params = {"codigoIbge": codigoIbge, "mesAno": mesAno}
        r = await client.get(url, headers=HEADERS, params=params)
        return r.json()

@app.get("/garantia-safra")
async def garantia_safra(cpf: str, mesAno: str):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/garantia-safra-beneficiarios"
        params = {"cpfBeneficiario": cpf, "mesAno": mesAno}
        r = await client.get(url, headers=HEADERS, params=params)
        return r.json()

@app.get("/seguro-defeso")
async def seguro_defeso(cpf: str, mesAno: str):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/seguro-defeso-beneficiarios"
        params = {"cpfBeneficiario": cpf, "mesAno": mesAno}
        r = await client.get(url, headers=HEADERS, params=params)
        return r.json()

@app.get("/servidor-federal")
async def servidor_federal(cpf: str):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/servidores"
        params = {"cpf": cpf}
        r = await client.get(url, headers=HEADERS, params=params)
        return r.json()
