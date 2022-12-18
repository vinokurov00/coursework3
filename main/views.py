from flask import Blueprint, render_template, request
from utils import get_posts_all, search_for_posts, get_post_by_pk, get_comments_by_post_id, get_posts_by_user

main_page_blueprint = Blueprint('main_page_blueprint', __name__, template_folder='templates')


@main_page_blueprint.route('/')
def main_page():
    all_posts = get_posts_all()
    return render_template('index.html', posts=all_posts)


@main_page_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    post =  get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments)

@main_page_blueprint.route('/search/')
def search_by_query_page():
    query = request.args.get('s', '')
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts)


@main_page_blueprint.route('/users/<username>')
def search_by_username(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)