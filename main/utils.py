import json
from pathlib import Path
from flask import current_app


def load_posts():
    file_path = Path(__file__).resolve().parent.parent / current_app.config['POST_PATH']
    with open(file_path, encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def find_posts(substr):
    posts = []
    for post in load_posts():
        if substr.lower() in post['content'].lower():
            posts.append(post)
    return posts


def save_post(picture_path, post):
    posts = load_posts()
    file_path = Path(__file__).resolve().parent.parent / Path(current_app.config['POST_PATH'])
    save_data = {'pic': str(picture_path), 'content': post}
    posts.append(save_data)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return
