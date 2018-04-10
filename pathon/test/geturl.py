#导入urllib库，python访问网页必须库
import urllib
import urllib.request 
#时间类库
import time

#定义一个URL数组用来存放捕获的URL地址，也就是需要爬的文字地址路径
url = [''] * 50
#定义link变量，用来记录第几个URL地址
link = 1

#循环捕获博客目录第一页所有的文章链接，并下载

#定义con变量来存储urllib.urlopen打开韩寒博客的目录地址，特别注意下'+str(page)+'，用来变化每一页目录地址的
con = urllib.request.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
#变量title用来存储con变量中找到<a title=开头元素的位置
title = con.find(r'<a title=')
#变量href用来存储con变量中找到href='开头元素的位置
href = con.find(r'href=',title)
#变量html用来存储con变量中找到.html开头元素的位置
html = con.find(r'.html',href)
#存储第一个连接地址
url[0] = con[href + 6:html + 5]
content = urllib.request.urlopen(url[0]).read()
open(r'hanhan/'+url[0][-26:],'w+').write(content)
print('0 have downloaded',url[0])
#循环捕获每一篇文章的地址，并存储在URL数组中
while title != -1 and href != -1 and html != -1 and link < 50:
    #con[href + 6:html + 5]是用来取con字符串href后6位到html倒数5位之间的字符串
 url[link] = con[href + 6:html + 5]
    #打开读取每一篇文章地址，并存储在content中
 content = urllib.request.urlopen(url[link]).read()
    #打开hanhan这个文件夹，如果里面没有url[link][-26:]这个字符串命名的文件，便将content里的内容写入，命名为url[link][-26:]
 open(r'hanhan/'+url[link][-26:],'w+').write(content)
 print(link,'have downloaded',url[link])
 title = con.find(r'<a title=',html)
 href = con.find(r'href=',title)
 html = con.find(r'.html',href)
    #自增记数
 link = link +1
