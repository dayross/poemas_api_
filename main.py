
from enum import Enum
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union, Annotated
import json , random, os
from dotenv import load_dotenv
import custom_errors

class TiposTexto(str, Enum):
    poema = "poema"
    haiku = "haiku"
    frase = "frase"

class TextoEntity(BaseModel):
    nombre: str | None = None
    autor : str | None = None
    contenido : str
    extracto : bool


poemas = FastAPI()

load_dotenv()
api_key = os.getenv('API_KEY')     

def texto_a_numero(texto : TiposTexto):
    if texto is TiposTexto.poema:
         return 0
    elif texto is TiposTexto.haiku:
         return 1
    else:
         return 2
    

def numero_a_texto(numero : int):
     if numero == 0:
          return TiposTexto.poema
     elif numero == 1:
          return TiposTexto.haiku
     else:
          return TiposTexto.frase


@poemas.get("/")
def root():
    return {"message":"Esta es la API de textos romanticos. Creada por @dayross_z"}

@poemas.get("/autores")
def autor():
    lista_autores = []
    i = 0
    try:
        with open("data.json", "r", encoding="UTF-8") as file:
            data = json.loads(file.read())
            for x in data:
                tipo_texto = numero_a_texto(i)
                for y in x[tipo_texto]:
                    actual_autor = y["autor"]
                    if actual_autor not in lista_autores and actual_autor != "":
                        lista_autores.append(actual_autor)
                i +=1
                return JSONResponse(content=lista_autores, media_type="application/json; charset=utf-8")

        if not data:
                raise HTTPException(status_code=404, detail="No hay texto disponible")
    except FileNotFoundError:
            raise custom_errors.not_found
    
@poemas.get("/autor/{autor_name}")
def autor(autor_name : str):
    return {"autor" : autor_name}

@poemas.get("/tipo/{tipo_texto}")
def tipos(tipo_texto : TiposTexto):
    i = texto_a_numero(tipo_texto)
    try:
        with open("data.json", "r", encoding="UTF-8") as file:
            data = json.loads(file.read())
            
            return JSONResponse(content=data[i][tipo_texto], media_type="application/json; charset=utf-8")
    except FileNotFoundError:
            raise custom_errors.not_found
    
@poemas.get("/texto/{tipo_texto}/autor/{autor}")
def texto_por_autor(tipo_texto : TiposTexto, autor : str = 'AUTHOR'):
    i = texto_a_numero(tipo_texto)
    lista_textos = []
    try:
        with open("data.json", "r", encoding="UTF-8") as file:
            data = json.loads(file.read())
            for x in data[i][tipo_texto]:
                if x["autor"].upper() == autor.upper().replace("_", " "):
                    lista_textos.append(x)

            if len(lista_textos) > 0:
                
                return JSONResponse(content=lista_textos, media_type="application/json; charset=utf-8")
            else:
                return {"No se han encontrado" ,tipo_texto}
    except FileNotFoundError:
            raise custom_errors.not_found
        
# funcion para subir un texto, 
@poemas.post("/subir/{tipo_texto}")
def crear_texto(tipo_texto : TiposTexto , texto :TextoEntity, key : str | None):
    if key != api_key:
         return {"La API KEY no es valida"}
     

    i = texto_a_numero(tipo_texto)
    try:
        with open("data.json", "r+", encoding="UTF-8") as file:
                data = json.load(file)
                print('abierto el archivo')
                if tipo_texto in data[i]:
                    data[i][tipo_texto].append(texto.dict())
                    print('entro al archivo')
                else:
                     print(data[i][tipo_texto])

                file.seek(0)
                print('file seek')
                json.dump(data, file, ensure_ascii=False, indent=3)
                file.truncate()

                return {"message" : "Texto agregado exitosamente"}
    except FileNotFoundError:
        raise custom_errors.not_found

@poemas.get("/{tipo_texto}/random")
def random_tipo_texto(tipo_texto : TiposTexto):
    i = 3
    if tipo_texto=="poema":
        i = 0
    elif tipo_texto=="haiku":
        i = 1
    else:
        i = 2
    
    try:
        with open("data.json", "r", encoding="UTF-8") as file:
            data = json.loads(file.read())
            resp = random.choice(data[i][tipo_texto])
            return JSONResponse(content=resp, media_type="application/json; charset=utf-8")
    except FileNotFoundError:
        raise custom_errors.not_found
        
@poemas.get("/random")
def random_texto():
    i = random.choice([0,1])
    print(i)
    texto = numero_a_texto(i)

    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.loads(file.read())
            choice = random.choice(data[i][texto])
            resp = { "tipo" : texto,
                     "contenido" : choice}
            return JSONResponse(content=resp, media_type="application/json; charset=utf-8")
    except FileNotFoundError:
        raise custom_errors.not_found

# @poemas.get("/example")
# async def example():
#     content = {"message": "Este es un texto en UTF-8: áéíóú ñ"}
#     return JSONResponse(content=content, media_type="application/json; charset=utf-8")
    
    

# validación para query parameters
# @poemas.get("/dar-tipos/")
# def dar_tipos_texto(texto : Annotated[str | None, Query(max_length=20)] = None):
#     resultados = {'texto' : [{'tipo_texto' : TiposTexto.frase}, 
#                              {'tipo_texto' : TiposTexto.haiku}, 
#                              {'tipo_texto' : TiposTexto.poema} ]}
#     if texto : 
#         resultados.update({'tipo_texto' : texto})
#     return resultados

# def crear_poema(texto : Annotated[TiposTexto , Query(max_length=300)]):
#     resultado = {'prueba' : [{'autor' : 'PRUEBA_AUTOR'}]}
#     if texto:
#         resultado.update({'contenido' : texto})
#     return resultado
    


# # queries NECESARIOS (genero) y OPCIONALES   
# @poemas.get("/texto/{tipo_texto}/generos/")
# def texto_por_genero(tipo_texto : TiposTexto ,genero : str, autor : Union[str, None] = None ):
#     return {'tipo_texto' : tipo_texto,
#             'genero' : genero,
#             'autor' : autor}

# @poemas.get("/todo/")
# def varios_poemas(skip : int = 0, limit : int = 0):
#     return fake_items_db[skip : skip + limit]
