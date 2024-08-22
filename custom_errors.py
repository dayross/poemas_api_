from fastapi import HTTPException
not_found = HTTPException(status_code=404, detail="No se encontró la fuente de datos")