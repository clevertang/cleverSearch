# -*- coding: utf-8 -*-  
import requests
from scrapy.selector import Selector

__author__ = 'clevertang'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
starturl="http://www.toutiao.com/"
re=requests.get(starturl,headers=headers)
selector=Selector(text=re.text)
print(re.text)
# names=selector.xpath("/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[1]/div/div[2]/div/div[2]/div[1]/a[3]").extract()
# for name in names:
#     print(name)

