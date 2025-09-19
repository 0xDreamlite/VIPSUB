import requests
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://hermes--co.com/connectionsws?os_id=2"
OUTPUT_FILE = "sub.txt"

def fetch_links():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(URL, headers=headers, verify=False)
    response.raise_for_status()
    data = response.json()

    links = []
    for item in data.get("data", []):
        ip = item.get("ip", "")
        if ip.startswith(("vless://", "vmess://", "trojan://")):
            links.append(ip)
    return links

def save_links(links):
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            existing = set(line.strip() for line in f.readlines())
    else:
        existing = set()


    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        new_count = 0
        for link in links:
            if link not in existing:
                f.write(link + "\n")
                new_count += 1
        print(f"Added {new_count} new links.")

if __name__ == "__main__":
    try:
        links = fetch_links()
        save_links(links)
    except Exception as e:
        print("Error:", e)
        exit(1)
