def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "对不起 " + filename + ' 找不到'
        print(msg)
    else:
        # 计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print("文件 " + filename + " 有 " + str(num_words) + " 单词。")


filenames = ["../alice.txt", "alice.txt"]
for filename in filenames:
    count_words(filename)

    