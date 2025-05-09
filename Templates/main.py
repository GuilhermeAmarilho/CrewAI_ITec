from fastapi import FastAPI
from api.routes import router
import os

# os.system("cls")
print('\n\n\n\n\n\n\n')


app = FastAPI(
    title="CrewAI",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    # é recomendado manter o uvicorn para ser necessário rodar apenas o main.py p/iniciar o  programa.
    # Caso não tivesse, teria que rodar uvicorn main:app --reload toda vez que der update
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
