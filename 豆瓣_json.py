import requests
from pathlib import Path

url = 'https://movie.douban.com/j/chart/top_list?'
p = {
    'type': 13,
    'interval_id': '100:90',
    'action':'',
    'start': 0,
    'limit': 20
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
cookie={
    'cookie':'ll="118318"; bid=Yue_aMwP-C8; _pk_id.100001.4cf6=95323664e249629c.1729344849.; _vwo_uuid_v2=D608A3EEE1C9384989630EA3F4807CFCA|438ee136b7da317337437812206f0b0e; __utmc=30149280; __utmz=30149280.1729433565.2.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmc=223695111; __utmz=223695111.1729433567.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1729437442%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.1899258195.1729344846.1729433565.1729437442.3; __utmb=30149280.0.10.1729437442; __utma=223695111.1243052146.1729344849.1729433567.1729437442.3; __utmb=223695111.0.10.1729437442'
}
res = requests.get(url, params=p, headers=headers)
print(res.status_code)
res.encoding='utf-8'


path = '../douban.json'
with open(path, 'w', encoding='utf-8') as f:
    f.write(res.text)

#obj = re.compile(r'', re.S)
#sth = obj.finditer(res.text)