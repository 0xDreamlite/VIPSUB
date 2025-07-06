import requests
import re

URL = "https://hermes--co.com/connectionsws?os_id=2"
OUTPUT_FILE = "links.txt"

def fetch_links():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    links = []
    for item in data.get("data", []):
        ip = item.get("ip", "")
        if ip.startswith("vless://") or ip.startswith("vmess://") or ip.startswith("trojan://"):
            # فقط لینک‌های v2ray مد نظر
            links.append(ip)

    return links

def save_links(links):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")

if __name__ == "__main__":
    try:
        links = fetch_links()
        save_links(links)
        print(f"Saved {len(links)} links.")
    except Exception as e:
        print("Error:", e)
        exit(1)
