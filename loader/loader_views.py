# Импортируем класс блюпринта, шаблонизатор, request, функции и JSONDecodeError
import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request
from loader.utility_loader import save_picture, func_add_post

# Создаем новый блюпринт, выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_loader')


# Создаем вьюшку с загрузкой поста
@loader_blueprint.route('/post')
def loader_page():
    return render_template("post_form.html")


# Создаем вьюшку с загрузкой фото и текста для поста
@loader_blueprint.route('/post', methods=['POST'])
def add_page_post():
    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        return "Нет картинки и/или текста"

    if picture.filename.split(".")[-1] not in ["jpeg", "png"]:
        logging.info("Загруженный файл не картинка")
        return "Неверное расширение файла"

    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        return "Файл не найден."
    except JSONDecodeError:
            return "Некорректный файл."

    post: dict = func_add_post({'pic': picture_path, 'content': content})
    return render_template("post_uploaded.html", post=post)
