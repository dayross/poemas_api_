# poemas API
### La API esta disponible en linea en https://poemas-api.onrender.com 🩷
Una API que entrega textos cortos con tintes romanticos o relacionados a cosas de amor (poemas, frases, haikus).

estado de la API : completada y aceptando sugerencias para endpoints.

los textos seran solo en español y cortos, y la API será de uso público y gratuito :3c

## pd: viva el amor el desinteres es un pndjo

### pasos
1. tener python y un ambiente virtual para python
2. en el ambiente virtual (o venv) hacer:

	pip install -r requirements.txt

3. dar uvicorn main:poemas --reload
4. verlo en el localhost

# Endpoints

- /autores : da la lista de autores de los textos que se encuentran (algunos textos no les encontre autor so feel free).
- /autor/{nombre_del_autor} : da los textos que se encuentran de ese autor. el nombre del autor va con acentos y separada por guiones bajos.
- /subir/{tipo_texto} : POST para subir un texto de cierto tipo de los disponibles. ocupa una api key como query param. si se quiere una api key, contactenme.
- /tipo/{tipo_de_texto} : da todos los textos de ese tipo (poema, frase, haiku).
- /texto/{tipo_texto}/autor/{autor} : da los tipos de texto.
- /{tipo_texto}/random : da un texto al azar del tipo de texto seleccionado.
- /random : da un texto al azar de cualquiera de los tipos disponibles.







