from flask import Blueprint, jsonify
from app.posts.dao.comments_dao import CommentsDAO
from app.posts.dao.posts_dao import PostsDAO

api_blueprint = Blueprint('api_blueprint', __name__)
posts_dao = PostsDAO("data/data.json")
comments_dao = CommentsDAO("data/comments.json")



@api_blueprint.route("/api/posts/")
def posts_all():
    posts = posts_dao.get_posts_all()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>")
def get_posts_by_pk(post_id):
    post = posts_dao.get_post_by_pk(post_id)
    return jsonify(post)
