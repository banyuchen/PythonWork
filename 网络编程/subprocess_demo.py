import requests
headers = {
    'x-Ticket': 'b966c05ab3b07187b608068354729809'
}
url = 'http://wx.hangzhoujihui.com/api/index/index/round'
data = {
    "lng": "120.184003",
    "lat": "30.236686",
    "city": "杭州市",
    "orderby": "1"
    }
s = requests.Session()
response = s.post(url = url, data=data, headers=headers)

print(response.text)  # 响应内容