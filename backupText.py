import os
import sqlite3

DATABASE = 'instance/blog2.db'
BACKUP_DIRECTORY = 'static/TEXT_bak'

def backup_database_to_text_files():
    # Ensure the backup directory exists
    if not os.path.exists(BACKUP_DIRECTORY):
        os.makedirs(BACKUP_DIRECTORY)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT title, content FROM post')
        posts = cursor.fetchall()

        for title, content in posts:
            # Replace any invalid characters for filenames
            safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
            filename = f"{safe_title}.txt"
            filepath = os.path.join(BACKUP_DIRECTORY, filename)

            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)

            print(f"Backed up post: {title} to {filepath}")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    backup_database_to_text_files()
