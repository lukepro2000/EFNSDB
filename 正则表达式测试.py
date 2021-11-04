import re
p=re.compile('luke(.+)asd')
s = 'lukeasdsadas123dsad123asd'

print(p.findall(s))