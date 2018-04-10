import re  
import urllib.request 
 
#----------模拟浏览器的行为，向谷歌翻译发送数据，然后抓取翻译结果，这就是大概的思路-------
def Gtranslate(text):  

    #text 输入要翻译的英文句子  
 Gtext=text

    #hl:浏览器、操作系统语言，默认是zh-CN
    #ie:默认是UTF-8
    #text：就是要翻译的字符串
    #langpair:语言对，即'en'|'zh-CN'表示从英语到简体中文  
 values={'hl':'zh-CN','ie':'UTF-8','text':Gtext,'langpair':"'en'|'zh-CN'"}  
    #URL用来存储谷歌翻译的网址
 url='http://translate.google.cn/'  
    #将values中的数据通过urllib.urlencode转义为URL专用的格式然后赋给data存储
    #urlencode返回的可能是str，必须调用encode保证能给Post方法使用
 data = urllib.parse.urlencode(values)
 data = data.encode('utf-8')
    #然后用URL和data生成一个request
 req = urllib.request.Request(url,data)
    #伪装一个IE6.0浏览器访问，如果不伪装，谷歌将返回一个403错误
 browser='Mozilla/4.0 (Windows; U;MSIE 6.0; Windows NT 6.1; SV1; .NET CLR 2.0.50727)'  
 req.add_header('User-Agent',browser)  

    #向谷歌翻译发送请求  
 response = urllib.request.urlopen(req)

    #读取返回页面，然后我们就从这个HTML页面中截取翻译过来的字符串即可
 html=response.read().decode('utf-8')

    #使用正则表达式匹配<=TRANSLATED_TEXT=)。而翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
 p=re.compile(r"(?<=TRANSLATED_TEXT=).*?;")  
 m=p.search(html)  
 chineseText=m.group(0).strip(';')  
 return chineseText 
  
if __name__ == "__main__":   
    #Gtext为待翻译的字符串 
 #Gtext='you should believe yourself,you are the best one! and we sure that you will do something making us being proud of you'
 print('Please input the text to translate:')  
 Gtext=input();
 print('The input text: %s' % Gtext)  
 chineseText=Gtranslate(Gtext).strip("'")  
 print('Translated End,The output text: %s' % chineseText)
