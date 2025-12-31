import sqlite3
import json
import random
import datetime
import hashlib

DB_PATH = "platform.db"
TEAM_ID = "e06e8cc1-454d-4555-9346-b1d2aa212ba1"

def seed_analytics_data():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. Get existing accounts to associate posts with
    accounts = cursor.execute("SELECT * FROM social_accounts").fetchall()
    if not accounts:
        print("No accounts found. Please connect accounts first.")
        return

    # 2. Sample data for content and media
    contents = [
        "在这个快节奏的时代，你是否也在寻找那份属于自己的宁静？✨ #生活美学 #心灵奇旅",
        "3个动作教你高效减脂，收藏起来别吃灰！🔥 #健身打卡 #好身材练出来",
        "最新黑科技推荐：这款AI工具居然能自动帮我剪辑视频？😱 #科技前沿 #设计神器",
        "周末去哪儿？带你打卡这座城市最隐秘的猫咖 🐱 #城市漫游计划 #猫咪日常",
        "今天尝试了跨界联名，效果出乎意料！快来看看这个开箱吧 🎁 #潮流风向标 #开箱视频",
        "深夜食堂：一碗简单的葱油拌面，治愈一天的不开心 🍜 #深夜食堂 #美食教程",
        "关于副业赚钱，我有几点掏心窝子的建议... 💰 #个人成长 #认知变现",
        "挑战24小时不使用手机，我的真实感受是... 📵 #断舍离 #生活记录",
        "这首歌适配所有的旅行Vlog，建议收藏！🎵 #旅行推荐 #氛围感",
        "面试成功的10个小技巧，应届生必看！🎓 #求职指南 #面试经验",
        "带你揭秘大厂员工的代码生活，真的有那么累吗？👨‍💻 #程序员日常 #互联网圈子",
        "如何用手机拍出电影感的照片？这几个构图一定要学！📸 #手机摄影 #摄影教程",
        "沉浸式整理工作台，开启效率满满的一天 ⌨️ #桌面美学 #高效工作",
        "这款游戏的画质简直绝了！快来看看我的实机演示 🎮 #游戏杂谈 #画质体验",
        "教你如何零成本给房间做个大改造 🏠 #家居分享 #软装搭配",
        "如果你最近感到焦虑，不妨听听这段话 🌊 #治愈系 #心态调整",
        "那些年我踩过的穿搭雷区，姐妹们千万别学！🙅‍♀️ #穿搭避雷 #显瘦穿搭",
        "分享一个让你相见恨晚的学习方法 📚 #学习方法 #学霸养成",
        "没想到这些东西混合在一起，味道居然这么神奇？🥤 #饮品DIY #味蕾挑战",
        "这就是我理想的老年生活，哪怕只有一瞬间的自由 🌄 #向往的生活 #自由灵魂"
    ]

    media_templates = [
        {"url": "https://images.unsplash.com/photo-1492691523567-6170c2405ea5?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Photography
        {"url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Studio
        {"url": "https://images.unsplash.com/photo-1493225255756-d9584f8606e9?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Music
        {"url": "https://images.unsplash.com/photo-1516280440614-37939bbacd81?w=400&h=600&fit=crop", "type": "image/jpeg"}, # City
        {"url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Art
        {"url": "https://images.unsplash.com/photo-1551269901-5c5e14c25df7?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Tech
        {"url": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Travel
        {"url": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Desk
        {"url": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Nature
        {"url": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Coding
        {"url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Hardware
        {"url": "https://images.unsplash.com/photo-1527689368864-3a821dbccc34?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Office
        {"url": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Team
        {"url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Chart
        {"url": "https://images.unsplash.com/photo-1454165833221-d7d11de49837?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Strategy
        {"url": "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Modern
        {"url": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Healthy Food
        {"url": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Cooking
        {"url": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Landscape
        {"url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Lake
        {"url": "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Concert
        {"url": "https://images.unsplash.com/photo-1493612276216-ee3925520721?w=400&h=600&fit=crop", "type": "image/jpeg"}, # Coffee
        {"url": "https://images.unsplash.com/photo-1506466010722-395aa2bef877?w=400&h=600&fit=crop", "type": "image/jpeg"}  # Minimalist
    ]

    # 3. Generate 20-30 posts
    now = datetime.datetime.now()
    
    # 清空旧数据确保刷新
    cursor.execute("DELETE FROM posts")
    
    for i in range(30):
        post_id = f"seed_{i}_{int(datetime.datetime.now().timestamp())}"
        account = random.choice(accounts)
        content = random.choice(contents)
        
        # Performance metrics
        # Highly skewed - some big winners
        roll = random.random()
        if roll > 0.95: # 5% chance of viral hit
            views = random.randint(100000, 500000)
            gmv = float(random.randint(5000, 20000))
        elif roll > 0.8: # 15% chance of good performance
            views = random.randint(20000, 80000)
            gmv = float(random.randint(1000, 5000))
        else: # Regular performance
            views = random.randint(500, 5000)
            gmv = float(random.randint(50, 500))
            
        likes = int(views * random.uniform(0.02, 0.08))
        comments = int(likes * random.uniform(0.01, 0.05))
        shares = int(likes * random.uniform(0.005, 0.02))
        
        post_date = (now - datetime.timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))).isoformat()
        
        account_info = [{
            "id": account['id'],
            "type": account['platform'].upper(),
            "name": account['name'],
            "handle": account['handle'],
            "avatar": account['avatar']
        }]
        
        media_info = [random.choice(media_templates)]
        
        cursor.execute("""
            INSERT OR REPLACE INTO posts (id, team_id, content, status, post_date, accounts_json, media_json, views, likes, comments_count, shares, gmv)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            post_id, TEAM_ID, content, "PUBLISHED", post_date, 
            json.dumps(account_info), json.dumps(media_info), 
            views, likes, comments, shares, gmv
        ))

    # 4. Add some more AI Agents to fulfill the "WOW" factor
    new_agents = [
        ("情感短剧脚本师", "短剧,编剧", "擅长反转和爽点设计，分钟万赞教程。", "你是一个资深反转剧编剧...", "heart", "创作者联盟", 45000, 4.9, "¥299/年"),
        ("海外带货助手", "跨境,TikTok", "自动生成英文带货口播稿，并优化海外SEO。", "You are a professional TikTok dropshipping expert...", "shopping-bag", "Global Team", 32000, 4.8, "¥19/月"),
        ("爆款标题生成器", "文案,SEO", "万能标题公式，点击率提升300%。", "你是一个营销大师，专门起爆款标题...", "edit-3", "官方工具", 89000, 4.9, "免费订阅"),
        ("AI 翻译官 (多语种)", "翻译,出海", "保持原意且符合当地表达习惯的精准翻译。", "你是一个精通多国语言的翻译官...", "globe", "官方工具", 56000, 4.7, "官方能力"),
        ("数据分析专家", "运营,策略", "导入历史数据，自动生成下一阶段创作策略。", "你是一个顶尖的数据分析师...", "trending-up", "AI实验室", 12000, 4.8, "¥49/月")
    ]
    
    for agent in new_agents:
        cursor.execute("""
            INSERT INTO ai_agents (name, tags, description, logic, icon, author, usage, rating, price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, agent)

    conn.commit()
    conn.close()
    print("Seed complete! Added 25 posts and 5 new AI agents.")

if __name__ == "__main__":
    seed_analytics_data()
