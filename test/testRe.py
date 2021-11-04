'''
. 表示任何单个字符
[] 字符集，对单个字符给出取值范围 如[a-z]
[^ ] 非字符集，对单个字符给出排除范围 如[^abc]表示非a非b非c得单个字符
* 前一个字符0次或无限次扩展
+ 前一个字符1次或无限次扩展
？ 前一个字符0次或1次扩展
| 左右表达式任意一个
{m,n} 前一个字符m到n次扩展
^ 匹配字符串开头
$ 匹配字符串结尾
() 分组标记 内部只能使用|操作符
\d 数字
\w 单词字符

标志修饰符
re.I 大小写不敏感
re.L 本地化识别匹配
re.M 多行匹配 影响^、$
re.S 使.匹配包括换行在内得所有字符
re.U 根据Unicode字符解析字符 影响\w \W \b \B
re.X
'''
import re

# 有模式对象
# pat = re.compile('AA')  # 此处得AA是正则表达式，用来验证其他的字符串
# pat.search('BDC')  # search字符串被校验得内容
# m = pat.search('ABCAAABCAAABCAA')
# print(m)

# 没有模式对象
# m = re.search('asd', 'Aasd')
# print(m)

print(re.findall('[A-Z]+', 'ASDaDKJABa')[0])  # 前面字符串是规则，后面字符串是被校验得字符串

# print(re.sub('a','A',r'laksndl')) #找到a用A替换
