filename = "../alice.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "对不起 " + filename + ' 不能打开'
    print(msg)
else:
     # 计算文件大致包含多少单词
     words = contents.split()
     num_words = len(words)
     print("文件 " + filename + " 有 " + str(num_words) + " 单词。")


