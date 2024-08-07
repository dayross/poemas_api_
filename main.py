from fastapi import FastAPI

from enum import Enum

class TiposTexto(str, Enum):
    poema = "poema"
    haiku = "haiku"
    frase = "frase"


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

@poemas.get("/tipo/{tipo_texto}")
def tipos(tipo_texto : TiposTexto):
    if tipo_texto is TiposTexto.poema:
        return {"tipo de texto" : tipo_texto,
                tipo_texto : {
                    "titulo" : "Amor",
                    "content" : """ Todos los que amo
                                    están en ti
                                    y tú
                                    en todo lo que amo.""",
                    "autor" : "Claribel Alegría"}}
    if tipo_texto.value == "frase":
        return {"tipo de texto" : tipo_texto,
                tipo_texto : {
                    "content" : """Contigo siempre lo que con nadie nunca.""",
                    "autor" : "El Arrebato"}}
    if tipo_texto.value == "haiku":
        return {"tipo de texto" : tipo_texto,
                tipo_texto : {
                    "content" : """No estoy en mí. 
                                    Perderte es extraviarme
                                    Hallarte hallarme.""",
                    "autor" : "Antonio Zirión Quijano"}}
    
    