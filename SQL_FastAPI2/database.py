from sqlmodel import SQLModel, create_engine, Session
from contextlib import asynccontextmanager
from fastapi import FastAPI

#Establecemos la URL de la base de datos (en este caso, SQLite)
sqlite_url = "sqlite:///db/mydatabase.db"  #Ruta de la base de datos
engine = create_engine(sqlite_url, echo=True)  # echo=True para ver los logs SQL generados

#Función para crear las tablas de la base de datos
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  #Crea todas las tablas definidas en los modelos

#Función para obtener sesiones de base de datos
def get_session():
    with Session(engine) as session:  #Creamos una sesión utilizando el engine
        yield session  #Retornamos la sesión para ser utilizada en las operaciones CRUD

#Esta función se usará para gestionar el ciclo de vida de la aplicación y crear las tablas al iniciar
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  #Crear las tablas
    yield  #La aplicación se ejecuta aquí, mientras está en funcionamiento
    print("Adios")  #Mensaje cuando la app se apaga
