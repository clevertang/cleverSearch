# -*- coding: utf-8 -*-  
__author__ = 'clevertang'
#测试使用selenium来进行模拟登陆等操作

from selenium import webdriver
#scrapy的selector是c写的,比纯python的更快
from scrapy.selector import Selector

# browser=webdriver.Chrome(executable_path="G:/python/selenium/chromedriver.exe")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.13.3hGql9&id=537968028617&cm_id=140105335569ed55e27b&abbucket=19")
# print(browser.page_source)
# t_selector=Selector(text=browser.page_source)
# #之所以选取这个是因为直接访问html source是看不到的,是通过js加载的
# print(t_selector.css(".tm-promo-price .tm-price::text").extract())

#下面用这个来登录下淘宝
# browser.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.50862.754894437.1.qfVJfu&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
# browser.find_element_by_id('J_Quick2Static').click()
# browser.find_element_by_css_selector(".static-form  input[name='TPL_username']").send_keys("唐言若")
# browser.find_element_by_css_selector(".static-form  input[name='TPL_password']").send_keys("xxx")#不给看
# browser.find_element_by_css_selector(".static-form  button.J_Submit").click()


#可以对浏览器进行设置,比如不加载图片等等
# chrome_opt=webdriver.ChromeOptions()
# prefs={"profile.managed_default_content_settings.images":2}
# chrome_opt.add_experimental_option('prefs',prefs)
# browser=webdriver.Chrome(executable_path="G:/python/selenium/chromedriver.exe",chrome_options=chrome_opt)
# browser.get("https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=http%3A%2F%2Fweibo.com%2F&domain=.weibo.com&sudaref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DlKs4yDsZ6Xqtb6xG0gmPNGV63lDy2EDKZT1QzT3u7nW%26wd%3D%26eqid%3Df628d80e00015b7e00000006594b6e8b&ua=php-sso_sdk_client-0.6.23&_rand=1498115726.3058")


#pantomjs,无界面的浏览器,据说多进程下性能下降比较严重,
browser=webdriver.Chrome(executable_path="G:/python/selenium/phantomjs.exe")