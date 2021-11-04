'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的属性结构，每个系欸DNA都是python对象，所有对象可以归纳为4种
-Tag 标签及其内容：拿到它所找到的第一个内容
-NavigableString
-BeautifulSoup 整个文档
-Comment
'''
import re

from bs4 import BeautifulSoup

file = open('./baidu.html', 'rb')  # 打开
html = file.read()  # 读取
bs = BeautifulSoup(html, 'html.parser')  # 解析html类型 使用html.parser解析器

# Tag
# print(bs.title)
# print()
# print(bs.a)
# print()
# print(bs.head)
# print(type(bs.head))

# NavigableString
# print(bs.title.string)
# print(type(bs.title.string))

# 属性 键值对的形式
# print(bs.a.attrs)
# print(type(bs.a.attrs))

# BeautifulSoup
# print(type(bs))
# print(bs.attrs)
# print(bs.name)
# print(bs)

# Comment 是一种特殊的NavigableString 不包含注释
# print(bs.a.string)
# print(type(bs.a.string))

# -----------------------------------------
# 文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])

# -----------------------------------------
# 文档的搜索 比遍历更经常用
'''1.find_all() 字符串过滤：会查找字符串完全匹配的内容'''
# t_list = bs.find_all('a')  # 找到所有a标签 用列表的形式返回

# 正则表达式搜索:使用search()方法来匹配内容
# t_list = bs.find_all(re.compile('a'))

# 方法：传入一个函数（方法），根据函数的要求来搜索(了解)
# def name_is_exists(tag):
#     return tag.has_attr('name')
#
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)
#
# print(t_list)

'''2.kwargs 参数'''
# t_list = bs.find_all(id='head')
#
# t_list = bs.find_all(class_='mnav')
# t_list = bs.find_all(class_=True)
#
# t_list = bs.find_all(href="http://news.baidu.com")
#
# for item in t_list:
    # print(item)

'''3.text参数'''
# t_list = bs.find_all(text='hao123')
# t_list = bs.find_all(text=['hao123', '地图', '贴吧'])
# t_list = bs.find_all(text=re.compile('\d'))  # 应用正则表达式来查找特定文本的内容（标签里的字符串）

# for item in t_list:
#     print(item)

'''4.limit参数'''
# t_list = bs.find_all('a', limit=3)
#
# for item in t_list:
#     print(item)

'''css选择器'''
# t_list = bs.select('title')  # 通过标签来查找
#
# t_list = bs.select('.mnav')  # 通过类名来查找
#
# t_list = bs.select('#ul')  # 通过id来查找
#
# t_list = bs.select('a[class="bri"]')  # 通过属性来查找
#
# t_list = bs.select('head>title')  # 通过子标签来查找
#
# t_list = bs.select('.mnav ~ .bri')  # 通过兄弟标签来查找
# print(t_list[0].get_text())  # 拿到文本
#
# for item in t_list:
#     print(item)
