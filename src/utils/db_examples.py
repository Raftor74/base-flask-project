from utils.database import db


def get_all_users():
    """ Возвращает всех пользователей из таблицы users """

    # Получение соединения
    connection = db.connection
    # SQL-запрос
    query = "SELECT * FROM `users`"
    # Cursor - специальный объект для работы с БД
    cursor = connection.execute(query)
    # Список всех записей в БД
    db_result = cursor.fetchall()
    # Конвертация записей в список словарей Python
    users = [dict(row) for row in db_result]
    return users


def get_single_user():
    """ Возвращает одну запись пользователя из БД """

    # Получение соединения
    connection = db.connection
    # SQL-запрос
    query = "SELECT * FROM `users`"
    # Cursor - специальный объект для работы с БД
    cursor = connection.execute(query)
    # Одна запись из БД
    db_result = cursor.fetchone()
    user = dict(db_result) if db_result is not None else None
    return user


def insert_new_user():
    """ Создаёт нового пользователя в БД """
    first_name = "Новое имя"
    last_name = "Новая фамилия"
    email = "new_email@test.ru"
    password = "123456"
    # Получение соединения
    connection = db.connection
    # SQL-запрос. Вместо значений используются placeholder'ы
    query = """
        INSERT INTO `users`
        (first_name, last_name, email, password)
        VALUES (?,?,?,?)
        """
    # Подготовленные значения в виде tuple
    values = tuple([first_name, last_name, email, password])
    # Выполняем запрос, передавая сам query и данные
    # Все значения из values подставятся вместо знаков ?
    # Такая подстановка защищает от SQL-инъекций
    cursor = connection.execute(query, values)
    # Записываем изменения в БД
    connection.commit()
    # Возвращаем ID вновь созданной записи
    return cursor.lastrowid
