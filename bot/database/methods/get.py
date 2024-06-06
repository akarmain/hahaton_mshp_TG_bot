from typing import List, Any
from bot.database.methods import *


def get_user_data(id, cell: str = "*") -> list[Any]:
    """
    1 функция для получения значений из БД
    :param cell:  Значение которое хотим полуить

    :return: Значение из БД
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute(f'SELECT {cell} FROM "users" WHERE "u_id" = ?', (id,))
        return res.fetchall()


def get_user_exists(u_id) -> bool:
    """
    Функция проверяет существует ли пользователь в базе данных.
    :param id: Идентификатор пользователя для проверки.
    :return: True если пользователь существует, иначе False.
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        cur.execute(f'SELECT "u_id" FROM "users" WHERE "u_id" = ?', (u_id,))
        return bool(cur.fetchone())

def get_all_tags() -> list[Any]:
    """
    Получаем все теги из таблицы.

    :return: Значение из БД
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM tags")
        return res.fetchall()

def get_all_task() -> list[Any]:
    """
    Получаем все task из таблицы.

    :return: Значение из БД
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM tasks")
        return res.fetchall()



def get_info_task(id: int) -> list:
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute('SELECT * FROM tasks WHERE "id" = ?', (id,))
        result = res.fetchall()
        return result[0] if result else None


def get_info_tag(id: int) -> list:
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute('SELECT * FROM tags WHERE "id" = ?', (id,))
        result = res.fetchall()
        return result[0] if result else None