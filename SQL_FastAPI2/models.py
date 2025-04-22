from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

#Modelo de Autor
class Autor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  #Identificador único del autor
    name: str
    bio: str

    #Relación con los artículos: un autor puede tener muchos artículos
    articles: List["Article"] = Relationship(back_populates="autor")

#Modelo de Artículo
class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  #Identificador único del artículo
    title: str  #Título del artículo
    content: str  #Contenido del artículo
    autor_id: int = Field(foreign_key="autor.id")  #Relación con el autor (clave foránea)

    #Relación inversa: cada artículo pertenece a un autor
    autor: Optional[Autor] = Relationship(back_populates="articles")

#Modelo para representar un autor en la salida pública
class AutorPublic(SQLModel):
    id: int  # Identificador único del autor
    name: str  # Nombre del autor
    bio: str  # Biografía del autor

#Modelo para representar un artículo en la salida pública
class ArticlePublic(SQLModel):
    id: int  # Identificador único del artículo
    title: str  # Título del artículo
    content: str  # Contenido del artículo
    autor_id: int  # Identificador del autor que escribió el artículo

#Crear un autor
class AutorCreate(SQLModel):
    name: str  # Nombre del autor
    bio: str  # Biografía del autor

#Crear un artículo
class ArticleCreate(SQLModel):
    title: str
    content: str
    autor_id: int
