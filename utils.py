import json


def get_posts_all() -> list[dict]:
    with open('./data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all() -> list[dict]:
    with open('./data/comments.json', 'r', encoding='utf=8') as file:
        return json.load(file)


def get_users_all() -> list:
    all_users_list = []
    for post in get_posts_all():
        all_users_list.append(post['poster_name'])
    return all_users_list


def get_post_id_all() -> list:
    all_post_id_list = []
    for comment in get_comments_all():
        if comment['post_id'] not in all_post_id_list:
            all_post_id_list.append(comment['post_id'])
    return all_post_id_list


def get_posts_by_user(user_name) -> list[dict]:
    if user_name not in get_users_all():
        raise ValueError('User does not exist')

    user_posts = []

    for post in get_posts_all():
        if user_name == post['poster_name']:
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(post_id: int) -> list[dict]:
    if post_id not in get_post_id_all():
        raise ValueError('Post does not exist')

    post_comments = []

    for comment in get_comments_all():
        if post_id == comment['post_id']:
            post_comments.append(comment)
    return post_comments


def search_for_posts(query) -> list[dict]:
    found_posts = []

    for post in get_posts_all():
        if query in post['content']:
            found_posts.append(post)
    return found_posts


def get_post_by_pk(pk:int) -> dict:
    for post in get_posts_all():
        if pk == post['pk']:
            return post
