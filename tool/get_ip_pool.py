# -*- coding: utf-8 -*-  
__author__ = 'clevertang'
import requests
import urllib
from urllib import request
from scrapy.selector import Selector
import MySQLdb
 #从西刺上获取免费的ip代理


conn=MySQLdb.connect(host="localhost",user="root",passwd="tx123321z",db="article_spider",charset="utf8")
cursor=conn.cursor()

def crawl_ips():
    headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
    for i in range(1,2093):
        re=requests.get("http://www.xicidaili.com/nn/{0}".format(i),headers=headers)
        # print(re.text)
        selector=Selector(text=re.text)
        all_trs=selector.css("#ip_list tr")
        ip_list=[]
        for tr in all_trs[1:]:
            speed_str=tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed=float(speed_str.split("秒")[0])
                all_text=tr.css("td::text").extract()
                ip=all_text[0]
                port=all_text[1]
                type=all_text[5]
                ip_list.append((ip,port,type,speed))

        for ip_info in ip_list:
            cursor.execute(
                "insert into proxy_ip(ip,port,type,speed) VALUES('{0}','{1}','{2}',{3})".format(
                    ip_info[0], ip_info[1], ip_info[2], ip_info[3]
                )

            )
            conn.commit()






    #urllib方法
    # req = urllib.request.Request("http://www.xicidaili.com/nn/", headers=headers)
    # re=request.urlopen(req)
    # print(re.read().decode("utf-8"))


class GetIP(object):
    def delete_ip(self,ip):
        #删除不能用的ip
        delete_sql="""
        delete from proxy_ip where ip='{0}'
        """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True
    def judge_ip(self,ip,port):
        #判断ip是否可用
        http_url="https://www.baidu.com"
        proxy_url="http://{0}:{1}".format(ip,port)
        try:
            proxy_dict={
                "http":proxy_url
            }
            response=requests.get(http_url,proxies=proxy_dict)
            # return True
        except Exception as e:
            print("不可用")
            self.delete_ip(ip)
            return False
        else:
            code=response.status_code
            if code>=200 and code<300:
                print("有效")
                return True
            else:
                print("无效")
                self.delete_ip(ip)
                return False
    def get_random_ip(self):
        #从数据库中随机获取一个可用的ip
        random_sql="""
        SELECT ip,port FROM proxy_ip
        ORDER BY RAND()
        LIMIT  1
        """
        result=cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip=ip_info[0]
            port=ip_info[1]
            judge_re=self.judge_ip(ip,port)
            if judge_re:
                return "http://{0}:{1}".format(ip,port)
            else:
                return self.get_random_ip()
# print(crawl_ips())
crawl_ips()
# if __name__=="__main__":
#     get_ip=GetIP()
#     get_ip.get_random_ip()