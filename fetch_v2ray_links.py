import requests
from datetime import datetime

url = "https://hermes--co.com/connectionsws?os_id=2"
response = requests.get(url)
data = response.json()

# لینک‌های v2ray جدید از API
new_links = []
for item in data.get("data", []):
    link = item.get("file1", "")
    if link.startswith("vless://") or link.startswith("vmess://"):
        new_links.append(link)

# خواندن لینک‌های قبلی از فایل (اگر فایل وجود داشته باشه)
try:
    with open("links.txt", "r", encoding="utf-8") as f:
        existing_lines = f.readlines()
except FileNotFoundError:
    existing_lines = []

# فیلتر کردن فقط لینک‌ها (حذف خطوط خالی و خطوط تاریخ)
existing_links = set(line.strip() for line in existing_lines if line.strip() and not line.startswith("# Updated at"))

# اضافه کردن لینک‌های جدید اگر تکراری نبودن
added = 0
for link in new_links:
    if link not in existing_links:
        existing_links.add(link)
        added += 1

# نوشتن مجدد فایل با لینک‌های قبلی + جدید + خط زمان به‌روزرسانی
with open("links.txt", "w", encoding="utf-8") as f:
    for link in sorted(existing_links):
        f.write(link + "\n")

print(f"{added} new links added, total {len(existing_links)} links saved.")
