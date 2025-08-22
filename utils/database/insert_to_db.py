import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


def add_to_user(user_id, is_bot, first_name, last_name, username, is_premium):
    cursor.execute(
        "INSERT INTO users (user_id, is_bot, first_name, last_name, username, is_premium) VALUES (?, ?, ?, ?, ?, ?)", (user_id, is_bot, first_name, last_name, username, is_premium))
    conn.commit()

def get_user_by_username(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id =?", (user_id,))
    row = cursor.fetchone()
    return row
    