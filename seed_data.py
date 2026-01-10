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
        "In this fast-paced era, are you also looking for your own peace? ✨ #LifeAesthetics #SoulJourney",
        "3 moves to teach you efficient fat loss, save it and don't let it gather dust! 🔥 #FitnessCheckIn #GoodBody",
        "Latest tech recommendation: This AI tool can actually edit videos for me automatically? 😱 #TechFrontier #DesignTool",
        "Where to go for the weekend? Take you to check out the most hidden cat cafe in the city 🐱 #CityRoaming #CatLife",
        "Tried a crossover collaboration today, the effect was unexpected! Come and see this unboxing 🎁 #TrendSetter #UnboxingVideo",
        "Midnight Diner: A simple bowl of scallion oil noodles cures all unhappiness 🍜 #MidnightDiner #FoodTutorial",
        "About making money on the side, I have a few sincere suggestions... 💰 #PersonalGrowth #CognitionRealization",
        "Challenge 24 hours without using a mobile phone, my real feelings are... 📵 #Declutter #LifeRecord",
        "This song fits all travel Vlogs, recommended to save! 🎵 #TravelRecommendation #Atmosphere",
        "10 tips for successful interviews, a must-see for fresh graduates! 🎓 #JobGuide #InterviewExperience",
        "Reveal the code life of big factory employees, is it really that tired? 👨‍💻 #ProgrammerDaily #InternetCircle",
        "How to take movie-like photos with a mobile phone? You must learn these compositions! 📸 #MobilePhotography #PhotographyTutorial",
        "Immersive workmanship arrangement, open a day full of efficiency ⌨️ #DesktopAesthetics #EfficientWork",
        "The picture quality of this game is simply amazing! Come and see my real machine demo 🎮 #GameTalk #QualityExperience",
        "Teach you how to make a big transformation of the room with zero cost 🏠 #HomeSharing #SoftDecoration",
        "If you feel anxious recently, you might as well listen to this passage 🌊 #Healing #MentalityAdjustment",
        "The dressing minefields I stepped on in those years, sisters must not learn! 🙅‍♀️ #DressingAvoidance #SlimmingDressing",
        "Share a learning method that makes you regret not knowing it earlier 📚 #LearningMethod #ScholarDevelopment",
        "I didn't expect these things mixed together, the taste is actually so magical? 🥤 #DrinkDIY #TasteBudChallenge",
        "This is my ideal old age life, even if only for a moment of freedom 🌄 #YearningLife #FreeSoul"
    ]

    media_templates = [
        {"url": "cover1.png", "type": "image/png"},
        {"url": "cover2.png", "type": "image/png"},
        {"url": "cover3.png", "type": "image/png"},
        {"url": "cover4.png", "type": "image/png"},
        {"url": "cover5.png", "type": "image/png"},
        {"url": "cover11.png", "type": "image/png"},
        {"url": "cover7.png", "type": "image/png"},
        {"url": "cover8.png", "type": "image/png"},
        {"url": "cover9.png", "type": "image/png"}
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

    new_agents = [
        ("短剧编剧助手", "短剧,脚本", "擅长情节反转与戏剧性设计，爆款教程。", "你是一位资深短剧编剧...", "heart", "创作者联盟", 4500, 4.9, "$299/year"),
        ("跨境销售助手", "跨境,TikTok", "自动生成英文销售脚本并优化SEO。", "你是专业的TikTok代发货专家...", "shopping-bag", "全球团队", 3200, 4.8, "$19/month"),
        ("爆款标题生成器", "文案,SEO", "万能标题公式，点击率提升300%。", "你是营销大师，专攻爆款标题...", "edit-3", "官方工具", 8900, 4.9, "免费订阅"),
        ("AI翻译官（多语言）", "翻译,出海", "精准翻译保留原意与本土化习语。", "你是精通多国语言的翻译官...", "globe", "官方工具", 5600, 4.7, "官方能力"),
        ("数据分析专家", "运营,策略", "导入历史数据，自动生成下阶段策略。", "你是顶级数据分析师...", "trending-up", "AI实验室", 12000, 4.8, "$49/month")
    ]
    
    for agent in new_agents:
        # 检查是否已存在同名智能体，避免重复插入
        exists = cursor.execute("SELECT 1 FROM ai_agents WHERE name = ?", (agent[0],)).fetchone()
        if not exists:
            cursor.execute("""
                INSERT INTO ai_agents (name, tags, description, logic, icon, author, usage, rating, price)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, agent)

    conn.commit()
    conn.close()
    print("Seed complete! Added 25 posts and 5 new AI agents.")

if __name__ == "__main__":
    seed_analytics_data()
