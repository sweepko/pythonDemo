from imp import reload

import requests
from bs4 import  BeautifulSoup
import pymysql.cursors
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root',db='match',charset="utf8")

cur=db.cursor()
html=requests.get('http://lol.te5.com/xinwenzhongxin/').content
# html.encode("utf8")#编码格式
shoup = BeautifulSoup(html,'lxml')
tag=shoup.find(class_='arc_left clearfix mainbg').find_all('a',target='_blank')
for li in tag:
    title = li.get('title')
    image=li.find('dt').find('img').get('data-original')
    content_url=li.get('href')
    data=requests.get(content_url).content
    # page_content=BeautifulSoup(data,'lxml')
    # content=str(page_content.find(class_='con f14'))
    desc=li.find('dd').find('p').text
    timee=li.find('dd').find(class_="title").find('span').text
    sql = """insert into craw_match(crawtitle,crawtime,crawimage,crawcontent,crawdesc) VALUES(%s,%s,%s,%s,%s)"""
    insert_data = (title, timee, image, content_url, desc)
    cur.execute(sql,insert_data);
     # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    db.commit()
    # finally:
    # db.close();
print('数据爬取完成')