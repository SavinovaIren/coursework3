from run import app

keys_should_be = {"content", "likes_count", "pic", "pk", "poster_avatar", "poster_name", "views_count"}


class TestApi:

    def test_app_all_posts_list(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, 'Получен не список'

    def test_app_all_posts_keys(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert set(response.json[0].keys()) == keys_should_be, "неверный список ключей"

    def test_app_post_by_pk(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert type(response.json) == dict, 'Получен не словарь'

    def test_app_post_by_pk_keys(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert set(response.json.keys()) == keys_should_be, "неверный список ключей"
