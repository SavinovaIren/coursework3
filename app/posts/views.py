from flask import Blueprint, render_template, request

from app.posts.dao.comments_dao import CommentsDAO
from app.posts.dao.posts_dao import PostsDAO
from extentions import *

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO("data/data.json")
comments_dao = CommentsDAO("data/comments.json")


@post_blueprint.route('/')
def all_posts():
    try:
        posts = posts_dao.get_posts_all()
        return render_template('index.html', posts=posts)
    except (FileNotFoundError, TypeError) as error:
        return render_template('error.html', error=error)


@post_blueprint.route('/post/<int:post_id>')
def personal_post(post_id):
    try:
        posts = posts_dao.get_post_by_pk(post_id)
        comments = comments_dao.get_comments_by_post_id(post_id)
    except (FileNotFoundError, JsonDecodeError) as error:
        return render_template('error.html', error=error)
    else:
        if posts is None:
            abort(404)
    comments_count = len(comments)
    return render_template('post.html', posts=posts, comments=comments, comments_count=comments_count)


@post_blueprint.route('/search')
def search_post():
    try:
        query = request.args.get('s', '')
        if query != '':
            posts = posts_dao.search_for_posts(query)
            count = len(posts)
        else:
            posts = []
            count = 0
        return render_template('search.html', posts=posts, query=query, count=count)
    except:
        return 'Поиск по постам'


@post_blueprint.route('/users/<username>')
def user_post(username):
    posts = posts_dao.get_posts_by_user(username)
    count = len(posts)
    return render_template('user-feed.html', posts=posts, count=count)



