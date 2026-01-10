import sqlite3

DB_PATH = "platform.db"

def clean_agents():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 删除所有现有智能体
    cursor.execute("DELETE FROM ai_agents")
    
    # 只保留精选的中文智能体，去除重复
    agents = [
        ("AI小说助手", "小说,创作", "专业小说创作助手，擅长各类题材", "你是一位资深小说作家...", "book-open", "官方团队", 156000, 4.9, "官方能力"),
        ("剪辑大师", "剪辑,视频", "智能视频剪辑，自动生成爆款效果", "你是专业的视频剪辑师...", "film", "官方团队", 98000, 4.8, "官方能力"),
        ("短剧编剧助手", "短剧,脚本", "擅长情节反转与戏剧性设计，爆款教程", "你是一位资深短剧编剧...", "heart", "创作者联盟", 45000, 4.9, "¥299/年"),
        ("跨境销售助手", "跨境,TikTok", "自动生成多语言销售脚本并优化SEO", "你是专业的TikTok跨境电商专家...", "shopping-bag", "全球团队", 32000, 4.8, "¥19/月"),
        ("爆款标题生成器", "文案,SEO", "万能标题公式，点击率提升300%", "你是营销大师，专攻爆款标题...", "edit-3", "官方工具", 89000, 4.9, "免费订阅"),
        ("AI翻译官", "翻译,出海", "精准翻译保留原意与本土化习语", "你是精通多国语言的翻译官...", "globe", "官方工具", 56000, 4.7, "官方能力"),
        ("数据分析专家", "运营,策略", "导入历史数据，自动生成下阶段策略", "你是顶级数据分析师...", "trending-up", "AI实验室", 12000, 4.8, "¥49/月"),
        ("情感短剧脚本师", "短剧,情感", "专注情感类短剧创作，催泪爆款", "你是情感短剧编剧专家...", "heart", "创作者联盟", 28000, 4.7, "¥199/年"),
    ]
    
    for agent in agents:
        cursor.execute("""
            INSERT INTO ai_agents (name, tags, description, logic, icon, author, usage, rating, price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, agent)
    
    conn.commit()
    conn.close()
    print(f"Clean complete! Now only {len(agents)} Chinese agents remain.")

if __name__ == "__main__":
    clean_agents()
