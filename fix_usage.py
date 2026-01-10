import sqlite3

conn = sqlite3.connect('platform.db')
cursor = conn.cursor()

# Update all agents with usage > 20000 to something smaller
# We can just scale them down by 10 or set to a random range
cursor.execute("UPDATE ai_agents SET usage = usage / 10 WHERE usage > 20000")
# Ensure some are still reasonably high but below 20000
cursor.execute("UPDATE ai_agents SET usage = 18500 WHERE usage > 20000") # Cap at 18500 just in case

# Alternatively, just set specific ones to nice numbers
cursor.execute("UPDATE ai_agents SET usage = 15600 WHERE name LIKE '%小说%'")
cursor.execute("UPDATE ai_agents SET usage = 9800 WHERE name LIKE '%剪辑%'")
cursor.execute("UPDATE ai_agents SET usage = 8900 WHERE name LIKE '%标题%'")
cursor.execute("UPDATE ai_agents SET usage = 5600 WHERE name LIKE '%翻译%'")
cursor.execute("UPDATE ai_agents SET usage = 12000 WHERE name LIKE '%数据%'")
cursor.execute("UPDATE ai_agents SET usage = 4500 WHERE name LIKE '%短剧编剧%'")
cursor.execute("UPDATE ai_agents SET usage = 3200 WHERE name LIKE '%营销%'")

conn.commit()
conn.close()
print("Updated agent usage in database.")
