import bs4 as bs
import csv
import urllib.request
url=urllib.request.urlopen("https://hasjob.co/").read()
soup=bs.BeautifulSoup(url,'xml')
span=soup.find_all('span')
url_detail=list()
postname_data=list()
location_data=list()
jpost_date=list()
c_name=list()
print(soup.title.string)
for url_link in soup.find_all('a',{'class','stickie'}):
 url_detail.append(url_link.get('href'))
for post in soup.find_all('span',{'class','headline'}):
  postname_data.append(post.get_text())
for location in soup.find_all('span',{'class','annotation top-left'}):
    location_data.append(location.get_text())
for date in soup.find_all('span',{'class','annotation top-right'}):
    jpost_date.append(date.get_text())
for name in soup.find_all('span',{'class','annotation bottom-right'}):
     c_name.append(name.get_text())
row_title=list()
row_data=list()
length=len(url_detail)
row_title=['Company_name','Url','Posted_date','location','Postname']
i=0
while i < length:
  row_data.append(url_detail[i]+","+postname_data[i]+","+location_data[i]+","+jpost_date[i]+","+c_name[i])
  i+=1

f= open('assigndata.csv','wb')
csv_writer = csv.writer(f)
#csv_writer.writerow()
for str in row_data:
 csv_writer.writerow(bytes(str,encoding="ascii",errors="ignore"))
f.close()