import requests
from pathlib import Path

url = 'https://www.douban.com/doulist/178710/'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
res = requests.get(url, headers=headers)
print(res.status_code)
res.encoding = 'utf-8'

path = Path('./douban.html')
with open(path, 'w', encoding='utf-8') as f:
    f.write(res.text)
