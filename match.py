from urllib import request
import requests
from bs4 import BeautifulSoup
import os
import re
from bs4 import BeautifulSoup
def getMatch():
    response = requests.get('http://www.wanplus.com/')
    response.encoding = "utf-8"  # 编码格式
    shoup = BeautifulSoup(response.text, 'html.parser')
    # print(shoup.text)
    data = shoup.decode('utf-8')
    # print(data)
    # reg=r'<li><a href="(.*?)" target="_blank" class="index-video"><img onerror="this.src=(.*?)" src="(.*?)" class="hot_img" alt="(.*?)" width="320px" height="180px">' \
    #     r'</a>' \
    #     r'<div class="text">' \
    #     r'<div class="text_t"><h3><em class="team-logo lg2"></em><a href="(.*?)" target="_blank">(.*?)</a></h3>' \
    #     r'<p><a class="name" target="_blank">(.*?)</a>(.*?)</p></div>' \
    #     r'<p class="text_b">(.*?)</p></div></li>';
    reg=r'<a href="/lol/live/165680" target="_blank">.*?</a>'
    match_list=re.findall(reg,shoup.text,re.S);
    print(match_list)
    # return match_list

# for content_url1,im,image,aa,content_url,title,person,time,desc   in getMatch():
#     print(image,content_url,title,person,time,desc);
#     break

getMatch()
