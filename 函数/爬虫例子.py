import re
from urllib.request import urlopen


def get_page(url):
    response = urlopen(url)
    return response.read().decode('utf-8')


def parse_page(s):
    # ret = re.findall(
    #     '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
    #    '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>',s,re.S)
    # return ret
    com = re.compile(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)
    rets = com.finditer(s)
    for ret in rets:
        yield {
            "id": ret.group("id"),
            "title": ret.group("title"),
            "rating_num": ret.group("rating_num"),
            "comment_num": ret.group("comment_num"),
        }


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = get_page(url)
    ret = parse_page(response_html)

    f = open('move_info7', 'a', encoding='utf8')

    for obj in ret:
        print(obj)
        data = str(obj)
        f.write(data + '\n')
    f.close()


count = 0
for i in range(10):   # 10页
    main(count)
    count += 25

