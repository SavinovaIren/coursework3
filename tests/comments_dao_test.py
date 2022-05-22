import pytest

from app.posts.dao.comments_dao import CommentsDAO

keys_should_be = {"post_id", "commenter_name", "comment","pk"}

class TestCommentsDao:

    @pytest.fixture()
    def comments_dao(self):
        comments_dao_list = CommentsDAO("./data/comments.json")
        return comments_dao_list


    def test_get_all(self, comments_dao):
        comments = comments_dao.get_all()
        """ Проверяем, верный ли список кандидатов возвращается """
        assert type(comments) == list, 'возвращается не список'
        assert len(comments) > 0, "возвращается пустой список"


    def test_get_all(self, comments_dao):
        comments = comments_dao.get_all()
        """ Возвращает список со всеми данными"""
        assert set(comments[0].keys()) == keys_should_be, "неверный список ключей"

    users_parametrize = [(1, {"Очень здорово!", ":)", "Класс!", "Интересно. А где это?"}), (2, {"Класс!", "Хе хе !", "Забавное фото!", "Часть вижу такие фото у друзей! Это новый тренд?"}), (3, {"Выглядит неплохо )", "Каждый раз захожу в ленту и от тебя что то классное!", "!!!", "Так так, продолжай)"})]

    @pytest.mark.parametrize("test_input,expected", users_parametrize)
    def test_get_comments_by_post_id(self, test_input, expected, comments_dao):
        comments = comments_dao.get_comments_by_post_id(test_input)
        set_comment = set()
        for comment in comments:
            set_comment.add(comment["comment"])

        assert set_comment == expected
