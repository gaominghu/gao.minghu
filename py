from urllib.request import urlopen
import requests

from bs4 import BeautifulSoup
from random import random
import time

root_url = r'http://www.kfc.com.cn/kfccda/storelist/index.aspx'

#response=requests.get("http://www.kfc.com.cn/kfccda/storelist/index.aspx")
#print (response.text)

html = urlopen("http://www.kfc.com.cn/kfccda/storelist/index.aspx").read().decode('utf-8')
soup = BeautifulSoup(html,"html.parser")
titles=soup.select("ul[class='shen_info'] a") # CSS 选择器
print(titles)
for title in titles:
    print(title.get_text(),title.get('cityid'))# 标签体、标签属性


def post2url(url, post_data):
    req =requests.get(
        url=root_url,
        headers={'Content-Type': 'text/xml'},
        data=post(post_data)
    )
    req.h('User-Agent', 'Mozilla/5.0(Windows NT 6.2; WOW64; rv:42.0) gecko/20100101 Firefox/42.0')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_header('Control-Cache', 'no-cache')
    req.add_header('Accept', '*/*')
    req.add_header('Connection', 'Keep-Alive')
    h = urlopen(req).read().decode('utf-8')
    return h
class FeatureCreator(object):
    def __init__(self):
        self.number = random() * 2

        i = 0
        root_s = bf(urllib2.urlopen(root_url).read())
        shen_info = root_s.find('ul', attrs={'class': 'shen_info'})
        for shen in shen_info.findAll('li'):
            i = i + 1
            if i > 1:
                break
            shen_name = shen('strong')[0].getText()
            for a in shen.findAll('a'):
                cityid, cityname = a['cityid'], a['rel'][a]
                root_postquery = r'http://www.kfc.com.cn/kfccda/aspx/GetStorelist.ashx?op=cname'
                post_data = {
                    'cname': cityname.encode('utf-8'),
                    'pid': '',
                    'pageIndex': '1',
                    'pageSize': '1000'
                }
            time.sleep(self.number)
            h_cityStores = post2url(root_postquery, post_data)
