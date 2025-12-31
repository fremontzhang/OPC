import requests
import json

# 测试发布 - 使用本地视频文件
API_BASE = "http://localhost:5000"

# 1. 准备本地视频文件（请替换为你的视频文件路径）
video_path = r"C:\Users\孙云龙\Downloads\test_video.mp4"  # 修改为实际路径

# 2. 选择要发布的账号ID（从前端复制）
account_ids = ["your_tiktok_account_id"]  # 从浏览器控制台获取

# 3. 发布内容
content = "🌟 Continue the story here\n👉 🎭 Find the full series on the \"goodnovel\" app\n🔍 Look up \"553086\", to enjoy every episode!"

# 4. 发送发布请求
print("开始上传本地视频并发布...")

with open(video_path, 'rb') as video_file:
    files = {
        'media': ('video.mp4', video_file, 'video/mp4')
    }
    
    data = {
        'content': content,
        'accountIds': json.dumps(account_ids)
    }
    
    response = requests.post(
        f"{API_BASE}/api/publish",
        files=files,
        data=data,
        timeout=600  # 10分钟超时
    )
    
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
