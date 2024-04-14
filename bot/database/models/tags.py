from bot.database import main_set, get_all_tags, del_teg


def all_tags():
    """
    Получаем все теги из таблицы.
    """
    ans = []
    for i in get_all_tags():
        ans.append(i[1])
    return ans


class Tags:
    def __init__(self, t_id: int = None, name: str = None, author: int = None):
        self.id = t_id
        self.name = name
        self.author = author
    def add(self):
        # Используем главную функцию для добавления нового тега в таблицу `tags`
        main_set('tags', self.id, self.name, self.author)


    def all_tags(self):
        ans = []
        for i in get_all_tags():
            if i[2] == self.author:
                ans.append([i[0], i[1]])
        return ans


    def del_me(self):
        del_teg(self.id)