#coding=utf-8
import urllib
import json

search_string="站在两个世界的边缘"
search_string=urllib.urlencode({"q":"站在两个世界的边缘"})
fd=urllib.urlopen("http://api.douban.com/book/subjects?q=站在两个世界的边缘&alt=json")
data=fd.read()
data=json.loads(data)

for i in data["entry"]:
    title=i["title"]
    print u"书名" + " " + title["$t"]
    for a in i.get("author",[]):
        name=a["name"]
        print u"作者" + " " + name["$t"]