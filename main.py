from fastapi import FastAPI, Query

from enum import Enum

from typing import Union, Annotated

from pydantic import BaseModel

class TiposTexto(str, Enum):
    poema = "poema"
    haiku = "haiku"
    frase = "frase"

class TextoEntity(BaseModel):
    titulo: str | None = None
    autor : str | None = None
    contenido : str
    genero : str | None = None


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
                    "content" : """ Todos los que amo están en ti y tú en todo lo que amo.""",
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

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@poemas.get("/items/")
def varios_poemas(skip : int = 0, limit : int = 0):
    return fake_items_db[skip : skip + limit]


@poemas.get("/texto/{tipo_texto}/autor/{autor}")
def texto_por_autor(tipo_texto : TiposTexto, autor : str = 'AUTHOR'):
    # if tipo_texto in TiposTexto:
        return {'tipo_texto' : tipo_texto,
                'autor' : autor}

# queries NECESARIOS (genero) y OPCIONALES   
@poemas.get("/texto/{tipo_texto}/generos/")
def texto_por_genero(tipo_texto : TiposTexto ,genero : str, autor : Union[str, None] = None ):
    return {'tipo_texto' : tipo_texto,
            'genero' : genero,
            'autor' : autor}


# funcion para subir un texto, 
@poemas.post("/subir/")
def crear_texto(texto : TextoEntity):
    return texto

# validación para query parameters
@poemas.get("/dar-tipos/")
def dar_tipos_texto(texto : Annotated[str | None, Query(max_length=20)] = None):
    resultados = {'texto' : [{'tipo_texto' : TiposTexto.frase}, 
                             {'tipo_texto' : TiposTexto.haiku}, 
                             {'tipo_texto' : TiposTexto.poema} ]}
    if texto : 
        resultados.update({'tipo_texto' : texto})
    return resultados

# def crear_poema(texto : Annotated[TiposTexto , Query(max_length=300)]):
#     resultado = {'prueba' : [{'autor' : 'PRUEBA_AUTOR'}]}
#     if texto:
#         resultado.update({'contenido' : texto})
#     return resultado

    
    
