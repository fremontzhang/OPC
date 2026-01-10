import sqlite3
import os
import json

DB_PATH = "platform.db"

def check_posts():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Check recent posts
    print("\nRecent 5 posts:")
    cursor.execute("SELECT id, status, post_date, content FROM posts ORDER BY post_date DESC LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        # Avoid printing full content if it has emojis that GBK can't handle
        content = row['content']
        safe_content = content[:30].encode('ascii', 'ignore').decode('ascii')
        print(f"ID: {row['id']}, Status: {row['status']}, Date: {row['post_date']}, Content: {safe_content}...")
        
    conn.close()

if __name__ == "__main__":
    check_posts()
