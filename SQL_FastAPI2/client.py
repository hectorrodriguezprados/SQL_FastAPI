import requests

BASE_URL = "http://127.0.0.1:8000"

#Función para listar todos los autores
def list_authors():
    response = requests.get(f"{BASE_URL}/autors/")
    if response.status_code == 200:
        return f"Autores: {response.json()}"
    else:
        return f"Error al listar autores: {response.status_code}"

#Función para crear un nuevo autor
def create_author(name: str, bio: str):
    response = requests.post(f"{BASE_URL}/autors/", json={"name": name, "bio": bio})
    if response.status_code == 201:
        return f"Autor creado: {response.json()}"
    else:
        return f"Error al crear autor: {response.status_code}"

#Función para obtener un autor por su ID
def get_author(author_id: int):
    response = requests.get(f"{BASE_URL}/autors/{author_id}")
    if response.status_code == 200:
        return f"Autor encontrado: {response.json()}"
    else:
        return f"Error al obtener autor: {response.status_code}"

#Función para eliminar un autor por su ID
def delete_author(author_id: int):
    response = requests.delete(f"{BASE_URL}/autors/{author_id}")
    if response.status_code == 200:
        return f"Autor eliminado: {response.json()}"
    else:
        return f"Error al eliminar autor: {response.status_code}"

#Función para crear un artículo
def create_article(title: str, content: str, autor_id: int):
    response = requests.post(f"{BASE_URL}/articles/", json={"title": title, "content": content, "autor_id": autor_id})
    if response.status_code == 201:
        return f"Artículo creado: {response.json()}"
    else:
        return f"Error al crear artículo: {response.status_code}"

#Función para listar todos los artículos
def list_articles():
    response = requests.get(f"{BASE_URL}/articles/")
    if response.status_code == 200:
        return f"Artículos: {response.json()}"
    else:
        return f"Error al listar artículos: {response.status_code}"

#Función para obtener un artículo por su ID
def get_article(article_id: int):
    response = requests.get(f"{BASE_URL}/articles/{article_id}")
    if response.status_code == 200:
        return f"Artículo encontrado: {response.json()}"
    else:
        return f"Error al obtener artículo: {response.status_code}"

#xFunción para eliminar un artículo por su ID
def delete_article(article_id: int):
    response = requests.delete(f"{BASE_URL}/articles/{article_id}")
    if response.status_code == 200:
        return f"Artículo eliminado: {response.json()}"
    else:
        return f"Error al eliminar artículo: {response.status_code}"

# Ejemplos de uso
if __name__ == "__main__":
    # Crear autor
    print(create_author("Gabriel García Márquez", "Escritor colombiano"))

    # Listar autores
    print(list_authors())

    # Obtener un autor específico
    print(get_author(1))

    # Crear un artículo
    print(create_article("Cien años de soledad", "El contenido del artículo...", 1))

    # Listar artículos
    print(list_articles())

    # Obtener un artículo específico
    print(get_article(1))

    # Eliminar un autor
    print(delete_author(1))

    # Eliminar un artículo
    print(delete_article(1))
