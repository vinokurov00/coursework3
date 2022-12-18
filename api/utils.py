import json


def get_posts_all() -> list[dict]:
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_post_by_pk(pk:int) -> dict:
    for post in get_posts_all():
        if pk == post['pk']:
            return post
