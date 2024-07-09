import sqlite3
import os

# Определение пути к базе данных в текущем каталоге проекта
db_path = os.path.join(os.path.dirname(__file__), 'example.db')

# Подключение к базе данных (или создание базы данных, если она не существует)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Удаление таблицы employee, если она существует
print("Удаление таблицы employee, если она существует...")
cursor.execute('DROP TABLE IF EXISTS employee')
print("Таблица employee удалена, если существовала.")

print("1. Создание таблицы person...")
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
print("Таблица person создана.")

print("2. Переименование таблицы person в employee...")
# 2. Переименование таблицы person в employee
cursor.execute('ALTER TABLE person RENAME TO employee')
print("Таблица person переименована в employee.")

print("3. Удаление столбца email из таблицы employee...")
# 3. Удаление столбца email из таблицы employee
cursor.execute('''
CREATE TABLE employee_new (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')
print("Создана таблица employee_new без столбца email.")

# Копируем данные из старой таблицы в новую
cursor.execute('''
INSERT INTO employee_new (id, first_name, last_name, age)
SELECT id, first_name, last_name, age FROM employee
''')
print("Данные скопированы из таблицы employee в employee_new.")

# Удаляем старую таблицу
cursor.execute('DROP TABLE employee')
print("Таблица employee удалена.")

# Переименовываем новую таблицу
cursor.execute('ALTER TABLE employee_new RENAME TO employee')
print("Таблица employee_new переименована в employee.")

print("4. Заполнение таблицы данными...")
# 4. Заполнение таблицы данными
cursor.execute("INSERT INTO employee (id, first_name, last_name, age) VALUES (1, 'Иван', 'Иванов', 30)")
cursor.execute("INSERT INTO employee (id, first_name, last_name, age) VALUES (2, 'Мария', 'Петрова', 25)")
cursor.execute("INSERT INTO employee (id, first_name, last_name, age) VALUES (3, 'Алексей', 'Смирнов', 22)")
cursor.execute("INSERT INTO employee (id, first_name, last_name, age) VALUES (4, 'Наталья', 'Кузнецова', 45)")
cursor.execute("INSERT INTO employee (id, first_name, last_name, age) VALUES (5, 'Ольга', 'Попова', 35)")
cursor.execute("INSERT INTO employee (id, first_name, last_name, age) VALUES (6, 'Дмитрий', 'Васильев', 40)")
print("Таблица employee заполнена данными.")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("Все действия успешно выполнены.")
