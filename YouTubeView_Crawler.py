# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:24:52 2020

@author: CW
"""
import requests
from bs4 import BeautifulSoup
import datetime


url = "https://www.youtube.com/watch?v=AkfMX-MtT4E"
request = requests.get(url)
print(request.encoding)  #查看網頁返回的字符集類型
print(request.apparent_encoding)

content = request.content

soup = BeautifulSoup(content.decode('utf-8','ignore'), "html.parser")

#view = soup.find("link", {"rel": "alternate"})
selectview = soup.select(".watch-view-count")
view = selectview[0].text
for tag in soup.find_all("meta"):
    if tag.get("name", None) == "title":
        title = tag.get("content", None)
        print(title)
print(view)
#print(title)   
updateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')


url = 'https://script.google.com/macros/s/AKfycbyofM1g1RCPLEHMKjvGy9JrYvcRjLzF9B717zRv6y7TKxeCkv4w/exec'
parameter = {
"method": "write",
"updateTime": updateTime,
"title": title,
"view": view

}
r = requests.post(url, data=parameter)
print (r.text)
