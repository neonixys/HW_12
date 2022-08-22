# Импортируем json
import json

from main.utility_main import load_posts


def save_picture(picture):
    """Функция, которая сохраняет фото по пути /uploads/images"""
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)
    return path


def func_add_post(post):
    """Функция, которая загрузит данные в файл"""
    posts = load_posts()
    posts.append(post)
    with open("posts.json", "w", encoding="utf8") as json_file:
        json.dump(posts, json_file)
    return post
