from sqlmodel import Session, select
from database import engine
from models import Autor, Article


#Crear algunos autores y artículos para poblar la base de datos
def create_autors_and_articles():
    #Creación de autores
    autor_1 = Autor(name="Gabriel García Márquez", bio="Escritor colombiano, autor de Cien Años de Soledad")
    autor_2 = Autor(name="Isabel Allende", bio="Escritora chilena, autora de La Casa de los Espíritus")

    #Creación de artículos asociados a los autores
    article_1 = Article(title="Cien Años de Soledad", content="Una obra maestra del realismo mágico", autor_id=autor_1.id)
    article_2 = Article(title="El Amor en los Tiempos del Cólera", content="Otra gran novela de Gabo", autor_id=autor_1.id)
    article_3 = Article(title="La Casa de los Espíritus", content="Historia de una familia chilena", autor_id=autor_2.id)

    #Abrir una sesión para interactuar con la base de datos
    with Session(engine) as session:
        session.add(autor_1)
        session.add(autor_2)
        session.add(article_1)
        session.add(article_2)
        session.add(article_3)
        session.commit()


#Actualizar la biografía de un autor
def update_autor():
    with Session(engine) as session:
        statement = select(Autor).where(Autor.name == "Gabriel García Márquez")
        autor = session.exec(statement).first()

        if autor:
            print("Antes de actualizar:", autor)
            autor.bio = "Ganador del Nobel de Literatura en 1982"
            session.add(autor)
            session.commit()
            session.refresh(autor)
            print("Después de actualizar:", autor)


#Eliminar un artículo
def delete_article():
    with Session(engine) as session:
        statement = select(Article).where(Article.title == "La Casa de los Espíritus")
        article = session.exec(statement).first()

        if article:
            print("Eliminando artículo:", article)
            session.delete(article)
            session.commit()



def main():
    create_autors_and_articles()  #Crear autores y artículos
    update_autor()  #Actualizar autor
    delete_article()  #Eliminar artículo


if __name__ == "__main__":
    main()
