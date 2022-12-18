from flask import Blueprint, jsonify
import logging
from utils import get_posts_all, get_post_by_pk

logging.basicConfig(filename="logs/api.log", format="%(asctime)s [%(levelname)s] %(message)s")

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts_json():
    return jsonify(get_posts_all())


@api_blueprint.route('/api/posts/<int:postid>/', methods=['GET'])
def get_post_by_id_json(postid):
    return jsonify(get_post_by_pk(postid))