import requests
import json

API_KEY = "1db8d00b-13aa-4e78-85c0-17e0af6a7f95"
TEAM_ID = "e06e8cc1-454d-4555-9346-b1d2aa212ba1"
BASE_URL = "https://api.bundle.social/api/v1"

def check_remote_posts():
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}/post/?teamId={TEAM_ID}"
    print(f"Checking URL: {url}")
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        print(f"Status Code: {response.status_code}")
        if response.ok:
            data = response.json()
            posts = data if isinstance(data, list) else data.get('data', [])
            print(f"Found {len(posts)} posts remotely.")
            # Print last 3 posts
            for p in posts[:3]:
                print(f"ID: {p.get('id')}, Status: {p.get('status')}, Date: {p.get('postDate')}")
                # Check for the specific content from screenshot if possible
                # Content in screenshot: "Continue the story here..."
        else:
            print(f"Error response: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    check_remote_posts()
