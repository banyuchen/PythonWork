
'''
函数值 = lambda 参数  :返回值
# 参数可以有多个，用逗号隔开
# 匿名函数不管逻辑多复杂，只能写一行，且逻辑行结束后的内容就是返回值
# 返回值和正常的函数一样可以是任意数据类型
'''

# add = lambda x, y: x+y
# print(add(10, 12))

# t1 = (("a"), ("b"))
# t2 = (("c"), ("d"))
# ret = zip(t1, t2)


# def func(tup):
#     return {tup[0]: tup[1]}
#
#
# for i in map(lambda tup: {tup[0]: tup[1]}, ret):
#     print(i)
#
#
# names = ['alex', 'wupeiqi', 'yuanbao', 'nazha']
#
# ret = map(lambda first_name: first_name+'_sb', names)   # 迭代器
#
# print(list(ret))
#
# for x in ret:
#     print('----------------'+x)

# nums = [1, 3, 4, 5, 6, 7, 8]
#
#
# def func(num):
#     return num % 2 == 0
#
#
# ret = filter(func, nums)
#
# for i in ret:
#     print(i)

####################################################################################################################################################################################################
# def calculate_pages(lines, size):
#     """计算页数"""
#     pages, mod = divmod(lines, size)
#     if mod > 0:
#         pages += 1
#     return {'pages': pages, "mod": mod}
#
#
# def page_legal(page, lines):
#     """判断输入是否合法"""
#     d = calculate_pages(len(lines), 5)
#     try:
#         if int(page) > d['pages']:
#             print("文件没有这么长")
#             return
#         elif int(page) < 0:
#             print("请输入正数")
#             return
#         else:
#             read_file(int(page), lines, d["pages"], d["mod"])
#     except ValueError:
#         print("输入格式有误，请输入数字")
#
#
# def read_file(page, lines, pages, mod):
#     """读取文件内容"""
#     if page == pages:
#         for i in range(mod):
#             print(lines[i + (page - 1) * 5])
#     else:
#         for i in range(5):
#             print(lines[i + ((page - 1) * 5)])
#
#
# while True:
#     page = input("请输入页码")
#     # 读取文件
#     with open('file.txt') as f_obj:
#         lines = f_obj.readlines()
#     page_legal(page, lines)
