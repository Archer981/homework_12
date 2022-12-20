import json
from pathlib import Path
from flask import current_app
import logging

logging_file = Path(__file__).resolve().parent.parent / Path('basic.log')
logging.basicConfig(handlers=[logging.FileHandler(filename=logging_file, encoding='utf-8', mode='w')], level=logging.INFO)


def load_posts():
    file_path = Path(__file__).resolve().parent.parent / current_app.config['POST_PATH']
    try:
        with open(file_path, encoding='utf-8') as file:
            posts = json.load(file)
    except:
        # print('Файл posts.json отсутствует или не хочет превращаться в список')
        logging.warning('Файл posts.json отсутствует или не хочет превращаться в список')
        return
    return posts


def find_posts(substr):
    posts = []
    loaded_posts = load_posts()
    if not loaded_posts:
        return
    for post in loaded_posts:
        if substr.lower() in post['content'].lower():
            posts.append(post)
    if not posts:
        logging.info('Посты по указанным критериям не найдены')
    return posts


def save_post(picture_path, post):
    posts = load_posts()
    if not posts:
        return
    file_path = Path(__file__).resolve().parent.parent / Path(current_app.config['POST_PATH'])
    save_data = {'pic': str(picture_path), 'content': post}
    posts.append(save_data)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return True
