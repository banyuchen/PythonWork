def tail(filename):
    f = open(filename, encoding='utf-8')
    while True:
        line = f.readline().strip()
        if line:
            yield line


g = tail('file.txt')
for i in g:
    print(i)