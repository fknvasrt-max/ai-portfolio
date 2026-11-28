import os
import requests
import pandas as pd

with open(".env", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        os.environ.setdefault(name.strip(), value.strip())

api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    raise SystemExit("没有读到 DEEPSEEK_API_KEY，请检查桌面上的 .env 文件。")

df = pd.read_excel("sales_summary.xlsx")
table_text = df.to_string(index=False)

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
}
payload = {
    "model": "deepseek-flash",
    "messages": [
        {
            "role": "system",
            "content": "你是销售日报助理。根据汇总表写简短、具体的点评，不要编造表里没有的数字。",
        },
        {
            "role": "user",
            "content": "请根据下面这张销售汇总表，写一段中文日报点评，指出谁卖得好、哪个地区或日期表现如何，不超过 200 字。\n\n"
            + table_text,
        },
    ],
    "thinking": {"type": "disabled"},
    "stream": False,
}

response = requests.post(url, headers=headers, json=payload, timeout=60)
response.raise_for_status()
data = response.json()
comment = data["choices"][0]["message"]["content"]
print("日报点评：")
print(comment)