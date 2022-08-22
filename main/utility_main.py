# Импортируем json
import json


def load_posts():
    """Функция, которая загрузит данные из файла"""
    with open("posts.json", "r", encoding="utf8") as json_file:
        return json.load(json_file)


def get_post_by_word(word):
    """Функция, которая находит пост по слову"""
    search_list = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            search_list.append(post)
            continue
    return search_list
