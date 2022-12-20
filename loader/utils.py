from flask import current_app
from pathlib import Path


def save_picture(picture):
    file_path = Path(current_app.config['UPLOAD_FOLDER']) / Path(picture.filename)
    picture.save(Path(__file__).resolve().parent.parent / file_path)
    return file_path


