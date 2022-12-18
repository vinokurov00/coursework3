import pytest
from app import app


expected_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_all_posts_json():
    response = app.test_client().get("/api/posts/")
    posts = response.json
    assert type(posts) == list, "Вернулся не список"
    assert set(posts[0].keys()) == expected_keys, "Некорректные ключи"


def test_get_post_by_id_json():
    response = app.test_client().get("/api/posts/1/")
    post = response.json
    assert type(post) == dict, "Вернулся не словарь"
    assert set(post.keys()) == expected_keys, "Некорректные ключи"
