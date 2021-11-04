import urllib.request
import urllib.parse

# 获取get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码

# 获取post请求

# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen(url='http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
#     print(response.read().decode('utf-8'))
# except Exception as e:
#     print("time out!")
#     pass

# response = urllib.request.urlopen('http://www.baidu.com')
# response = urllib.request.urlopen('http://douban.com')
# print(response.getheaders())  # 获取头部
# print(response.getheader('Server'))

# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
#
# }
# data=bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# url = 'http://httpbin.org/post'
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


# 防止被识别出是爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
    "Host":"movie.douban.com"
    }
url = 'https://movie.douban.com/top250?start='
req = urllib.request.Request(url=url, headers=headers)  # 用Request才能加入headers
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding":"gzip, deflate, br",
#     "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Cache-Control":"max-age=0",
#     "Connection":"keep-alive",