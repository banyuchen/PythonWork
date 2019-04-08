import json

filename = "number.json"
try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    print("找不到" + filename + "文件。")
else:
    print(numbers)


