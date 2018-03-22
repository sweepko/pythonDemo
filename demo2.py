import urllib.request
import re
def getNovelList():
    response=urllib.request.urlopen("http://www.quanshuwang.com/list/1_1.html");
    html=response.read();
    html=html.decode("gbk").encode("utf-8").decode("utf-8");
    reg=r'<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">';
    urlList=re.findall(reg,html);
    return urlList;
def getChapterList(url):
    response=urllib.request.urlopen(url).read();
    html=response.decode("gbk").encode("utf-8").decode("utf-8");
    reg=r'<a href="(.*?)"  class="l mr11">';
    url=re.findall(reg,html)[0]
    response = urllib.request.urlopen(url).read()
    html = response.decode("gbk").encode("utf-8").decode("utf-8")
    reg=r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    urlList=re.findall(reg,html);
    return urlList
def getChapterContent(url):
    response=urllib.request.urlopen(url).read()
    html=response.decode("gbk").encode("utf-8").decode("utf-8")
    reg=r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">style6\(\);</script>'
    content=re.findall(reg,html,re.S)[0];
    print(content)
    # return  content
for title,url in getNovelList():
    for chapterUrl,chapterTitle in getChapterList(url):
        getChapterContent(chapterUrl)
        break;
    break;

