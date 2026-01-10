import sqlite3
import json

conn = sqlite3.connect('platform.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

print("--- AI Agents Table ---")
rows = cursor.execute("SELECT id, name, usage FROM ai_agents").fetchall()
for row in rows:
    print(f"ID: {row['id']}, Name: {row['name']}, Usage: {row['usage']}")

conn.close()
