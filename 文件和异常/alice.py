# filename = "../alice.txt"
#
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "对不起 " + filename + ' 不能打开'
#     print(msg)
# else:
#      # 计算文件大致包含多少单词
#      words = contents.split()
#      num_words = len(words)
#      print("文件 " + filename + " 有 " + str(num_words) + " 单词。")


def func(li):
    return li[1::2]


def func1(k):
    if len(k) > 5:
        print("大于5位")
    else:
        print("不大于5位")


func1([1, 2, 3, 4, 5, 3])


