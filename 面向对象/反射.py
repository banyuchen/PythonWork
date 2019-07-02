# 用字符串类型的名字去操作变量
# name = 1
# eval("print(name)") # 存在安全隐患


# 反射 就没有安全问题


# 反射对象中的属性和方法
class A:
    def func(self):
        print("in func")


# a = A()
# a.name = "alex"
# 反射对象的属性
# ret = getattr(a, "name") # 通过变量名的字符串形式取到的值
# print(ret)

# 反射对象的方法
# ret = getattr(a, "func")
# ret()


# 反射类的属性

# 反射类的方法


# 反射模块的属性和方法
# import my
# print(getattr(my, "day"))
#
# getattr(my, "wahah")()


import sys
year = 2019


def Year():
    return "2019"


# 反射当前模块的变量
print(sys.modules["__main__"].year)
# 反射当前模块的方法
print(sys.modules[__name__].Year())

import time
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(getattr(time, "strftime")("%Y-%m-%d %H:%M:%S"))
