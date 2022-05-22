import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_all(self):
        '''Загружает данные из файла и возвращает обычный list'''
        with open(f'{self.path}', 'r', encoding='utf-8') as file:
            _data = json.load(file)
            return _data

    def get_posts_all(self):
        """ Возвращает список со всеми данными"""
        posts = self.get_all()
        return posts

    # get_posts_by_user(user_name)` – возвращает посты определенного пользователя
    def get_posts_by_user(self, user_name):
        posts = self.get_posts_all()
        user_posts = []
        for post in posts:
            if post['poster_name'] == user_name:
                user_posts.append(post)
        return user_posts



    # search_for_posts(query) – возвращает список постов по ключевому слову
    def search_for_posts(self, query):
        posts = self.get_posts_all()
        query_list = []
        for post in posts:
            if query.lower() in post["content"].lower():
                query_list.append(post)
        return query_list

    # get_post_by_pk(pk) – возвращает один пост по его идентификатору
    def get_post_by_pk(self, pk):
        posts = self.get_posts_all()
        for post in posts:
            if post["pk"] == pk:
                return post
