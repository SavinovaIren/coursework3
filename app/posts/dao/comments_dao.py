import json


class CommentsDAO:

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

    def get_comments_by_post_id(self, post_id):
        """get_comments_by_post_id(post_id)` – возвращает комментарии определенного поста"""
        posts = self.get_posts_all()
        posts_comments = []
        for post in posts:
            if post["post_id"] == post_id:
                posts_comments.append(post)
        return posts_comments
