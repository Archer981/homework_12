from flask import current_app
from pathlib import Path
import logging

logging_file = Path(__file__).resolve().parent.parent / Path('basic.log')
# logging.basicConfig(filename=logging_file, level=logging.INFO)
logging.basicConfig(handlers=[logging.FileHandler(filename=logging_file, encoding='utf-8', mode='w')], level=logging.INFO)


class PictureExtensionIncorrect(Exception):
    pass


def save_picture(picture):
    file_path = Path(current_app.config['UPLOAD_FOLDER']) / Path(picture.filename)
    picture.save(Path(__file__).resolve().parent.parent / file_path)
    return file_path


def is_picture(picture):
    allowed_extensions = ['jpg', 'png']
    picture_extension = picture.filename.split('.')[-1].lower()
    if picture_extension not in allowed_extensions:
        logging.info('Загруженный файл - не картинка (расширение не jpeg и не png)')
        raise PictureExtensionIncorrect('Загруженный файл - не картинка (расширение не jpeg и не png)')
    return
