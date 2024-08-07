from fastapi import FastAPI

poemas = FastAPI()

@poemas.get("/")
def root():
    return {"message" : "Diana Rocío"}

@poemas.get("/autor")
def autor():
    return {"autor" : "DEFAULT"}

@poemas.get("/autor/{autor_name}")
def autor(autor_name : str):
    return {"autor" : autor_name}