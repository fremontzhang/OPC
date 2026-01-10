import sqlite3
import os

DB_PATH = "platform.db"

def check_posts():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check schema
    cursor.execute("PRAGMA table_info(posts)")
    columns = cursor.fetchall()
    print("Posts Table Schema:")
    for col in columns:
        print(col)
        
    # Check recent posts
    print("\nRecent 5 posts:")
    cursor.execute("SELECT * FROM posts ORDER BY post_date DESC LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    conn.close()

if __name__ == "__main__":
    check_posts()
