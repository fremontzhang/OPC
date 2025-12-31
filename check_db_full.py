import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = "platform.db"

def check_all_recent():
    if not os.path.exists(DB_PATH):
        print("DB not found")
        return
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # 24 hours ago
    threshold = (datetime.utcnow() - timedelta(hours=24)).isoformat()
    
    print(f"Checking posts since {threshold}")
    cursor.execute("SELECT * FROM posts WHERE post_date > ? OR last_sync > ? ORDER BY post_date DESC", (threshold, threshold))
    rows = cursor.fetchall()
    
    if not rows:
        print("No matches in last 24h")
    else:
        for row in rows:
            content = (row['content'] or "")[:30].encode('ascii', 'ignore').decode('ascii')
            print(f"ID: {row['id']}, Status: {row['status']}, Date: {row['post_date']}, Content: {content}")
            
    conn.close()

if __name__ == "__main__":
    check_all_recent()
