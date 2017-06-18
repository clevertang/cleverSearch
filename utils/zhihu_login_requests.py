# -*- coding: utf-8 -*-  
__author__ = 'clevertang'

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib          #对兼容性代码的尝试,py2和3不一样

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print ("cookie未能加载")

agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    'User-Agent': agent,
    # 'Pragma':'no-cache'
}

def is_login():
    #通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/question/56250357/answer/148534773"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code  != 200:
        return False
    else:
        return True

def get_xsrf():
    #获取xsrf code
    response = session.get("https://www.zhihu.com", headers=header)
    # s='<input type="hidden" name="_xsrf" value="6b73fd452420cfbffe17e7c251d0b46f"/>'

    match_obj = re.findall('.*name="_xsrf" value="(.*?)".*', response.text)

    if match_obj:
        return (match_obj[0])
    else:
        return ""
    print(match_obj)


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))
    print ("ok")


def get_captcha():
    import time
    t=str(int(time.time()*1000))
    captcha_url="https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t=session.get(captcha_url,headers=header)
    with open('captcha.jpg','wb') as f:
        f.write(t.content)
        f.close()
    from PIL import  Image
    try:
        im=Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass
    captcha=input("请输入验证码\n")
    return captcha


def zhihu_login(account, password):
    #知乎登录
    if re.match("^1\d{10}",account):
        print ("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "phone_num": account,
            "password": password,
            "captcha":get_captcha()
        }
    else:
        if "@" in account:
            #判断用户名是否为邮箱
            print("邮箱方式登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "email": account,
                "password": password,
                "captcha":get_captcha()
            }

    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()
# get_captcha()
# zhihu_login("961577196@qq.com", "tx123321z")
get_index()
print(is_login())

