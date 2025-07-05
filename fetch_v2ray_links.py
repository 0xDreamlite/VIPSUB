import requests
import re

def fetch_and_extract_links():
    url = "https://hermes--co.com/connectionsws?os_id=2"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.text

        # استخراج لینک‌های vless://
        vless_links = re.findall(r'vless:\/\/[^\s"]+', data)

        # ذخیره در فایل
        with open('links.txt', 'w') as f:
            for link in vless_links:
                f.write(link + '\n')
        print(f"{len(vless_links)} links extracted and saved.")
    except Exception as e:
        print(f"Error fetching or processing data: {e}")

if __name__ == "__main__":
    fetch_and_extract_links()
