import pytest

from app.posts.dao.posts_dao import PostsDAO

keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPostsDao:

    @pytest.fixture()
    def posts_dao(self):
        posts_dao_list = PostsDAO("./data/data.json")
        return posts_dao_list

    def test_get_all(self, posts_dao):
        posts = posts_dao.get_all()
        """ Проверяем, верный ли список кандидатов возвращается """
        assert type(posts) == list, 'возвращается не список'
        assert len(posts) > 0, "возвращается пустой список"

    def test_get_all(self, posts_dao):
        posts = posts_dao.get_all()
        """ Возвращает список со всеми данными"""
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_post_by_pk(self, posts_dao):
        posts = posts_dao.get_post_by_pk(3)
        """ Проверяем, возвращает ли один пост по его идентификатору"""
        assert type(posts) == dict, 'возвращается не список'
        assert posts["pk"] == 3, "возвращается неправильный кандидат"
        assert set(posts.keys()) == keys_should_be, "неверный список ключей"

    users_parametrize = [('leo', {1, 5}), ('johnny', {2, 6}), ('hank', {3, 7}), ('larry', {4, 8})]

    @pytest.mark.parametrize("test_input,expected", users_parametrize)
    def test_get_posts_by_user(self, test_input, expected, posts_dao):
        posts = posts_dao.get_posts_by_user(test_input)
        set_post = set()
        for post in posts:
            set_post.add(post["pk"])

        assert set_post == expected

    query_parametrize = [('тарелка', {1}), ('штуки', {2}), ('елки', {3})]

    @pytest.mark.parametrize("test_input,expected", query_parametrize)
    def test_search_for_posts(self, test_input, expected, posts_dao):
        posts = posts_dao.search_for_posts(test_input)
        set_querly = set()
        for post in posts:
            set_querly.add(post["pk"])
        assert set_querly == expected