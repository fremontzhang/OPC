import sqlite3

conn = sqlite3.connect('platform.db')
cursor = conn.cursor()

# 规范化智能体名称
renames = {
    "AI小说助手": "AI创作助手",
    "剪辑大师": "短剧剪辑大师"
}

for old_name, new_name in renames.items():
    cursor.execute("UPDATE ai_agents SET name = ? WHERE name = ?", (new_name, old_name))

# 重新排序智能体，AI创作助手排在第一位
agents_order = [
    "AI创作助手",
    "短剧剪辑大师", 
    "短剧编剧助手",
    "跨境销售助手",
    "爆款标题生成器",
    "AI翻译官",
    "数据分析专家",
    "情感短剧脚本师"
]

for idx, name in enumerate(agents_order):
    cursor.execute("UPDATE ai_agents SET id = ? WHERE name = ?", (idx + 1, name))

conn.commit()
conn.close()
print("Sorting complete! AI Novel Assistant is now first.")
