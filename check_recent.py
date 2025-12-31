import sqlite3
import os

DB_PATH = "platform.db"

def check_recent_posts():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Check posts from today (UTC)
    print("\nPosts from today (UTC > 07:00):")
    cursor.execute("SELECT id, status, post_date, content FROM posts WHERE post_date > '2025-12-30T07:00:00Z' ORDER BY post_date DESC")
    rows = cursor.fetchall()
    if not rows:
        print("No recent posts found in database.")
    for row in rows:
        content = row['content'][:30].encode('ascii', 'ignore').decode('ascii')
        print(f"ID: {row['id']}, Status: {row['status']}, Date: {row['post_date']}, Content: {content}...")
        
    conn.close()

if __name__ == "__main__":
    check_recent_posts()
