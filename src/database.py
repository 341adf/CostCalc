import sqlite3


def create_tables():
    'Создает таблицы expenses и income в базе данных, если они еще не существуют.'

    connect = sqlite3.connect('data/finanse.db')
    c = connect.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              category TEXT,
              amount REAL,
              description TEXT
            )
    ''')

    c.income('''
        CREATE TABLE IF NOT EXISTS income (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              sourse TEXT,
              amount REAL,
              description TEXT
            )
    ''')

    connect.commit()
    connect.close()

def add_expense(date, category, amount, description):
    'Добавляет новый расход в таблицу expenses'
    connection = sqlite3.connect('data/finance.db')
    c = connection.cursor()
    c.execute('INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)',
              (date, category, amount, description))
    connection.commit()
    connection.close()

def add_income(date, source, amount, description):
    'Добавляет новый расход в таблицу income'
    connection = sqlite3.connect('data/finance.db')
    c = connection.cursor()
    c.execute('INSERT INTO income (date, source, amount, description) VALUES (?, ?, ?, ?)',
            (date, source, amount, description))

    connection.commit()
    connection.close()

def get_expenses_by_category():
    """
    Возвращает сумму расходов по каждой категории.
    
    :return: Список кортежей, где каждый кортеж содержит категорию и сумму расходов
    по этой категории.
    """
    connection = sqlite3.connect('data/finance.db')
    c = connection.cursor()
    c.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    data = c.fetchall()

    connection.close()
    return data

def get_expenses_data():
    """
    Возвращает все данные из таблицы 'expenses'.
    
    :return: Список кортежей, где каждый кортеж содержит данные о расходе
    """
    conn = sqlite3.connect('data/finance.db')  # Подключаемся к базе данных
    c = conn.cursor()  # Создаем курсор для выполнения SQL-запросов

    # Выбираем все данные из таблицы 'expenses'
    c.execute('SELECT * FROM expenses')
    data = c.fetchall()  # Получаем все результаты запроса

    conn.close()  # Закрываем соединение с базой данных
    return data

def get_income_data():
    """
    Возвращает все данные из таблицы 'income'.

    :return: Список кортежей, где каждый кортеж содержит данные о доходе.
    """

    connection = sqlite3.connect('data/finance.db')
    c = connection.cursor()

    c.execute('SELECT * FROM income')
    data = c.fetchall()

    connection.close()
    return data
