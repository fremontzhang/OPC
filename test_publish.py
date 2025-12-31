
import requests
import json
import sys

# Ensure UTF-8 output if possible, but let's just remove emojis
def test_publish():
    url = "http://127.0.0.1:5000/api/publish"
    video_url = "https://beidou-file-test-v1.oss-cn-beijing.aliyuncs.com/syl/%E3%80%8ASo%2C%20Whose%20Ring%20...%E3%80%8B.mp4"
    
    payload = {
        "content": "Test video from AI agent #TikTok #AI",
        "accountIds": ["4a9ca68c-3daa-4000-8597-d1b869339a78"],
        "mediaUrls": [video_url]
    }
    
    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, json=payload)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Body:")
        try:
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except:
            print(response.text)
            
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    test_publish()
