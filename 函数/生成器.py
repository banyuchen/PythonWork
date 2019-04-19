# 只要含有yield关键字的函数都是生成器函数
# yield不能与return公用
# 生成器函数 ： 在执行之后会返回一个生成器


def generator():
    """生成器函数"""
    for i in range(100):
        yield print("这是第%s", i)


ret = generator()
for i in ret:
    pass

