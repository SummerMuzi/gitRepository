from urllib import request
from bs4 import BeautifulSoup
import xlwt

#中国加盟网
target_url = 'http://www.jmw.com.cn/'
#head = {}
header={
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
		}

#head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
download_req = request.Request(url=target_url,headers=header)
download_response = request.urlopen(download_req)
download_html = download_response.read()
soup_texts = BeautifulSoup(download_html,'lxml')
#category = soup_texts.find_all(class_="hangyeBox")
categorys = soup_texts.select('.hangyeBox a')
#print(categorys)

#存入excel 表格
book = xlwt.Workbook()
sheet0 = book.add_sheet('目录')

i=0
for category in categorys:
    #print(category.string+"----"+category.attrs['href'])
    item = category.string
    itemUrl = category.attrs['href']
    sheet0.write(i,0,item)
    sheet0.write(i,1,itemUrl)
    item_req = request.Request(url=itemUrl, headers=header)
    item_response = request.urlopen(item_req)
    item_html = item_response.read()
    item_texts = BeautifulSoup(item_html, 'lxml')


    book.add_sheet(item)
    i += 1

#文件保存
book.save('中国加盟网商家信息.xls')
print('下载完成！')