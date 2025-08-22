import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


# Создание таблицы users, если она еще не существует
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT UNIQUE,
        is_bot INTEGER,
        first_name TEXT,
        last_name TEXT,
        username TEXT NOT NULL UNIQUE,
        is_premium INTEGER
        
    );
"""
)


# Сохранение изменений (коммит)
conn.commit()
print("Таблица 'users' успешно создана (или уже существовала).")
conn.close()