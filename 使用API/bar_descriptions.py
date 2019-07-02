from urllib import request,parse

url = ""
headers = {
      #伪装一个火狐浏览器
      "User-Agent":'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
      "host":'httpbin.org'
  }
dict = {
      "name":"Germey"
}
data = bytes(parse.urlencode(dict),encoding="utf8")
req=request.Request(url=url,data=data,headers=headers,method="POST")  # 利用更强大的 Request 类来构建一个请求
response = request.urlopen(req)
print(response.read().decode("utf-8"))