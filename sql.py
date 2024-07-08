import sqlite3
import os

# Определение пути к базе данных в текущем каталоге проекта
db_path = os.path.join(os.path.dirname(__file__), 'example1.db')

# Подключение к базе данных (или создание базы данных, если она не существует)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Создание таблицы person
cursor.execute('''
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    email TEXT
)
''')

# 2. Переименование таблицы person в employee
cursor.execute('ALTER TABLE person RENAME TO employee')

# 3. Удаление столбца email из таблицы employee
cursor.execute('''
CREATE TABLE employee_new (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')
cursor.execute('''
INSERT INTO employee_new (id, first_name, last_name, age)
SELECT id, first_name, last_name, age FROM employee
''')
cursor.execute('DROP TABLE employee')
cursor.execute('ALTER TABLE employee_new RENAME TO employee')

# 4. Заполнение таблицы данными
employees = [
    (1, 'John', 'Doe', 30),
    (2, 'Jane', 'Smith', 25),
    (3, 'Emily', 'Jones', 22),
    (4, 'Michael', 'Brown', 45),
    (5, 'Jessica', 'Davis', 35),
    (6, 'Daniel', 'Wilson', 40)
]

cursor.executemany('''
INSERT INTO employee (id, first_name, last_name, age)
VALUES (?, ?, ?, ?)
''', employees)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Все действия успешно выполнены.")
