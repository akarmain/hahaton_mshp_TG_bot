from bot.database import main_set, get_all_tags, get_all_task, get_info_task, del_task, update_tag
from bot.database.models.tags import Tags


class Tasks:
    def __init__(self, t_id: int = None,
                 title: str = None,
                 time_over: str = None,
                 description: str = None,
                 tags: str = None,
                 complexity: str = None,
                 author: int = None,
                 ):
        self.id = t_id
        self.title = title
        self.description = description
        self.time_over = time_over
        self.complexity = complexity
        self.tags = tags
        self.author = author
        """"""

    def add(self):
        # Используем главную функцию для добавления нового тега в таблицу `tags`
        main_set('tasks', self.id,
                 self.title, self.description,
                 self.time_over, self.complexity,
                 self.tags, self.author)


    def all(self):
        ans = []
        for i in get_all_task():
            if i[6] == str(self.author):
                ans.append([i[0], i[1]])
        return ans

    def info(self):

        return get_info_task(self.id)

    def del_me(self):
        del_task(self.id)

    def add_tag(self, tags):
        update_tag(tags, self.id)
