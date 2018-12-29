# coding=utf-8

import requests
import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#
# }
#
# # result = requests.get('https://sz.zu.ke.com/zufang/',headers = headers)
# # print(result.text)
# url = ['https://sz.zu.ke.com//apartment/4631.html',
#     'https://sz.zu.ke.com//apartment/3770.html',
#     'https://sz.zu.ke.com//apartment/4213.html',
#     'https://sz.zu.ke.com//apartment/4213.html',
#     'https://sz.zu.ke.com//apartment/12642.html',
#     'https://sz.zu.ke.com//apartment/12791.html',
# ]
# # print(url[1])
# for data in range(0,len(url)):
#     # print(url[data])
#     result = re.findall(r'http.*?com//(.*?)/.*',url[data],re.S)
#     # print(result[0])
#     if result[0] == 'apartment':
#         print(result)

list = ["a 1 "," ","b",""]
for i in list:
    i = i.strip()
    if i != '':
        print(i)




