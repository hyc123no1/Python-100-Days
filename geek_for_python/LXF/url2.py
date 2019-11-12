import json
from urllib import request 

def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read().decode('utf-8'))


URL = "http://news-at.zhihu.com/api/4/news/latest"
data = fetch_data(URL)
print(data)