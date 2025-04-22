from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlmodel import Session, select
from models import Autor, AutorPublic, AutorCreate, Article, ArticlePublic, ArticleCreate
from database import get_session, lifespan


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "API Autors Articles!"}


#Ruta para obtener todos los autores
@app.get("/autors/",
         response_model=List[AutorPublic])  #El endpoint es GET /autors/ y devuelve una lista de 'AutorPublic'


def list_autors(session: Session = Depends(get_session)):  # 'session' es la conexión a la base de datos.
    # Realizamos una consulta a la base de datos para obtener todos los autores.
    autors = session.exec(select(Autor)).all()  #'select(Autor)' obtiene todos los registros de la tabla 'Autor'.
    return autors  #Devolvemos la lista de autores.


#Ruta para obtener un autor por su ID
@app.get("/autors/{autor_id}", response_model=AutorPublic)  # El endpoint es GET /autors/{autor_id}
def get_autor(autor_id: int, session: Session = Depends(get_session)):  # Recibimos el 'autor_id' como parámetro.
    autor = session.get(Autor, autor_id)  # 'session.get' busca el autor por su 'id'.
    if not autor:  # Si no encontramos el autor, lanzamos un error.
        raise HTTPException(status_code=404, detail="Autor no encontrado")  # Error 404 si no se encuentra.
    return autor  # Devolvemos el autor encontrado.


#Ruta para crear un nuevo autor
@app.post("/autors/", response_model=AutorPublic)  #El endpoint es POST /autors/ para crear un nuevo autor.
def create_autor(autor: AutorCreate,session: Session = Depends(get_session)):  #Recibimos los datos del autor a través de 'AutorCreate'.
    db_autor = Autor(name=autor.name, bio=autor.bio)  #Creamos un nuevo objeto 'Autor' usando los datos recibidos.
    session.add(db_autor)  #Añadimos el nuevo autor a la sesión de base de datos.
    session.commit()  #Guardamos los cambios en la base de datos.
    session.refresh(db_autor)  # Refrescamos el objeto para obtener los datos guardados, como el 'id'.
    return db_autor  #Devolvemos el autor que acabamos de crear.


#Ruta para obtener todos los artículos
@app.get("/articles/",
         response_model=List[ArticlePublic])  #El endpoint es GET /articles/ y devuelve una lista de artículos.
def list_articles(session: Session = Depends(get_session)):  # 'session' es la conexión a la base de datos.
    articles = session.exec(
        select(Article)).all()  #Realizamos una consulta a la tabla 'Article' para obtener todos los artículos.
    return articles  #Devolvemos la lista de artículos.


# Ruta para obtener un artículo por su ID
@app.get("/articles/{article_id}", response_model=ArticlePublic)  #El endpoint es GET /articles/{article_id}
def get_article(article_id: int, session: Session = Depends(get_session)):  #Recibimos el 'article_id' como parámetro.
    article = session.get(Article, article_id)  #'session.get' busca el artículo por su 'id'.
    if not article:  #Si no encontramos el artículo, lanzamos un error.
        raise HTTPException(status_code=404, detail="Artículo no encontrado")  # Error 404 si no se encuentra.
    return article  #Devolvemos el artículo encontrado.


#Ruta para crear un nuevo artículo
@app.post("/articles/", response_model=ArticlePublic)  #El endpoint es POST /articles/ para crear un nuevo artículo.
def create_article(article: ArticleCreate, session: Session = Depends(
    get_session)):  #Recibimos los datos del artículo a través de 'ArticleCreate'.
    db_article = Article(title=article.title, content=article.content, autor_id=article.autor_id)  # Creamos un nuevo artículo.
    session.add(db_article)  #Añadimos el nuevo artículo a la sesión de base de datos.
    session.commit()  #Guardamos los cambios en la base de datos.
    session.refresh(db_article)  #Refrescamos el objeto para obtener los datos guardados, como el 'id'.
    return db_article  #Devolvemos el artículo que acabamos de crear.


#Ruta para eliminar un autor
@app.delete("/autors/{autor_id}", response_model=AutorPublic)  #El endpoint es DELETE /autors/{autor_id}
def delete_autor(autor_id: int, session: Session = Depends(get_session)):  # Recibimos el 'autor_id' como parámetro.
    autor = session.get(Autor, autor_id)  #Buscamos al autor por su ID.
    if not autor:  #Si no encontramos el autor, lanzamos un error.
        raise HTTPException(status_code=404, detail="Autor no encontrado")  # Error 404 si no se encuentra.

    session.delete(autor)  #Eliminamos el autor de la base de datos.
    session.commit()  #Guardamos los cambios en la base de datos.
    return autor  #Devolvemos el autor que hemos eliminado.


#Ruta para eliminar un artículo
@app.delete("/articles/{article_id}", response_model=ArticlePublic)  #El endpoint es DELETE /articles/{article_id}
def delete_article(article_id: int,
                   session: Session = Depends(get_session)):  #Recibimos el 'article_id' como parámetro.
    article = session.get(Article, article_id)  #Buscamos el artículo por su ID.
    if not article:  #Si no encontramos el artículo, lanzamos un error.
        raise HTTPException(status_code=404, detail="Artículo no encontrado")  #Error 404 si no se encuentra.

    session.delete(article)  #Eliminamos el artículo de la base de datos.
    session.commit()  #Guardamos los cambios en la base de datos.
    return article  #Devolvemos el artículo que hemos eliminado.
