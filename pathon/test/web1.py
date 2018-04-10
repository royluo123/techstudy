import urllib.request

webURL = "http://www.python.org"
localURL = "index.html"
#通过URL打开远程页面
u = urllib.request.urlopen(webURL)
buffer = u.read()
print (u.info())
print ("从%s读取了%d 字节数据.\n" % (u.geturl(),len(buffer) ))

#通过URL打开本地页面
#u = urllib.urlopen(localURL)
#buffer = u.read()
#print u.info()
#print "从%s读取了%d 字节数据.\n" % (u.geturl(),len(buffer) )
