# Импортируем класс блюпринта, шаблонизатор, функции и JSONDecodeError
import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request

# Создаем новый блюпринт, выбираем для него имя
from main.utility_main import get_post_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_main')


# Создаем вьюшку для странички main
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


# Реализуем поиск и вывод постов при обращении на search>
@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info("Выполняю поиск")
    try:
        posts = get_post_by_word(search_query)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден."
    except JSONDecodeError:
        return "Некорректный файл."
    return render_template("post_list.html", query=search_query, posts=posts)
