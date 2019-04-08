filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("我喜欢Python语言.\n")
    file_object.write("人生苦短，我用Python.\n")


with open(filename) as file_object:
    print(file_object.read())

