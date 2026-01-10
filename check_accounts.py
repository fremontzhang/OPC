import requests
import json

def get_accounts():
    try:
        url = "http://127.0.0.1:5000/api/accounts"
        print(f"Fetching accounts from {url}...")
        resp = requests.get(url)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            accounts = resp.json()
            print(f"Found {len(accounts)} accounts:")
            for acc in accounts:
                print(f"ID: {acc.get('id')}, Name: {acc.get('name')}, Platform: {acc.get('platform')}, Type: {acc.get('type')}")
        else:
            print("Failed.")
            print(resp.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_accounts()
