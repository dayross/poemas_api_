si se especifica el tipo que se busca, la respuesta es así:

{
    "nombre": "string",
    "autor": "string",
    "contenido": "string",
    "extracto": true
  }

si no se especifica (como en el /random), la respuesta es asi:

{
    "tipo": "string",
    "contenido": {
        "nombre": "string",
        "autor": "string",
        "contenido": "string",
        "extracto": true
    }
}