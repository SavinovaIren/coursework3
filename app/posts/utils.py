import json


class Posts:

    # get_posts_all() – возвращает посты
    def get_posts_all():
        with open('data/data.json', 'r', encoding='utf-8') as file:
            global posts = json.load(file)
            return posts

    # get_posts_by_user(user_name) – возвращает посты определенного пользователя
    def get_posts_by_user(user_name):
        for post in posts:
            if user_name == post["poster_name"]:
                return





# get_comments_by_post_id(post_id) – возвращает комментарии определенного поста
def get_comments_by_post_id(post_id):
    pass


# search_for_posts(query) – возвращает список постов по ключевому слову
def search_for_posts(query):
    pass


# get_post_by_pk(pk) – возвращает один пост по его идентификатору
def get_post_by_pk(pk):
    pass
