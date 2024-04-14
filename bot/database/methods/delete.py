from bot.database.methods import *


def del_teg(id) -> None:
    """
    1 функция для удаления teg

    :return: None
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        cur.execute(f'DELETE FROM tags WHERE id = ?', (id,))

        # SQL запрос на удаление
def del_task(id) -> None:
    """
    1 функция для удаления  task

    :return: None
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        cur.execute(f'DELETE FROM tasks WHERE id = ?', (id,))

