import json
from flask import current_app


def load_posts():
    with open(current_app.config['POST_PATH'], encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def find_posts(substr):
    posts = []
    for post in load_posts():
        if substr.lower() in post['content'].lower():
            posts.append(post)
    return posts


def save_post(post):
    posts = load_posts()
    posts.append(post)
    with open(current_app.config['POST_PATH'])
