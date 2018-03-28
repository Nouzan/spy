from urllib import request
from bs4 import BeautifulSoup
import time
import csv
import codecs


URL = "http://femhzs.mofcom.gov.cn/fecpmvc/pages/fem/CorpJWList_nav.pageNoLink.html?sp="  # 要爬取的url
result = []  # 保存结果

for i in range(2805)[:1]:  # 循环每一页
    req = request.Request(URL + str(i))  # 生成请求对象
    req.add_header('User-Agent', 'Mozilla/6.0')  # 添加头部
    data = request.urlopen(req).read()  # 发起请求
    soup = BeautifulSoup(data, "html.parser")  # BeautifulSoup~
    # print(soup.select('tbody tr'))
    for tr in soup.select('tbody tr'):  # 循环每一个tr
        country = tr.select('td')[-1].text  # 获取倒数第一个td的内容，即国家信息
        country = country.strip()  # 去除多余空格
        if(country not in result):
            # print(country)
            result.append(country)  # 保存到result
    # time.sleep(1)

with codecs.open('result.csv', "w", 'GBK') as f:
    writer = csv.writer(f)
    for row in result:
        print(row)
        writer.writerow([row])
