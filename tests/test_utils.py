from utils import *
import pytest

keys_for_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                        "pk"}

keys_for_comments = {"post_id", "commenter_name", "comment", "pk"}


def test_get_posts_all():
    posts = get_posts_all()
    assert type(posts) == list, "Возвращает не список"
    assert len(posts) > 0, "Возвращает пустой список"
    assert set(posts[0].keys()) == keys_for_posts, "Неверный список ключей"


def test_get_posts_by_user():
    posts = get_posts_by_user("larry")
    assert type(posts) == list, "Возвращает не список"
    assert posts[0]["poster_name"].lower() == "larry", "Возвращает посты другого автора"
    assert len(posts) == 2, "Возвращает неправильное количество постов"
    assert set(posts[0].keys()) == keys_for_posts, "Неверный список ключей"


def test_get_posts_by_user_value_error():
    with pytest.raises(ValueError):
        get_posts_by_user("suspicious_person")


def test_get_comments_by_post_id():
    comments = get_comments_by_post_id(1)
    assert type(comments) == list, "Возвращает не список"
    assert comments[0]["post_id"] == 1, "Возвращает комменты с неверным id"
    assert len(comments) == 4, "Возвращает неверное количество комментов"
    assert set(comments[0].keys()) == keys_for_comments, "Неверный список ключей"


def test_get_comments_by_post_id_value_error():
    with pytest.raises(ValueError):
        get_comments_by_post_id(30)


def test_search_for_posts():
    posts = search_for_posts("еда")
    assert type(posts) == list, "Возвращает не список"
    assert len(posts) > 0, "Пост не найден"
    assert "еда" in posts[0]["content"].lower(), "В посте нет ключевого слова"
    assert set(posts[0].keys()) == keys_for_posts, "Неверный список ключей"


def test_get_post_by_pk():
    post = get_post_by_pk(1)
    assert type(post) == dict, "Возвращает не словарь"
    assert post["pk"] == 1, "Возвращает пост с неверным ID"
    assert set(post.keys()) == keys_for_posts, "Неверный список ключей"
