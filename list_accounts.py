import sqlite3
import json

def check_accounts():
    conn = sqlite3.connect('platform.db')
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT id, platform, name FROM social_accounts").fetchall()
    accounts = [dict(row) for row in rows]
    print(json.dumps(accounts, indent=2))
    conn.close()

if __name__ == "__main__":
    check_accounts()
