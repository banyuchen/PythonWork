"""
正则表达式 ---- 字符串匹配
"""

# 一个中括号匹配一个字符

import re

ret = re.search('a', 'ab dfasd  aae')
print(ret.group())

