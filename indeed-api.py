import requests as req
import csv
import sys
import pandas as pd
fieldnames=[
        "jobtitle",
        "company",
        "city",
        "state",
        "country",
        "language",
        "formattedLocation",
        "source",
        "date",
        "snippet",
        "url",
        "onmousedown",
        "latitude",
        "longitude",
        "jobkey",
        "sponsored",
        "expired",
        "indeedApply",
        "formattedLocationFull",
        "formattedRelativeTime",
        "stations"]
url="http://api.indeed.com/ads/apisearch?publisher=9091824477922251&q=a&sort=&radius=&st=&jt=&start={}&limit=25&fromage=7&filter=1&latlong=1&co={}&chnl=&userip=1.2.3.4&format=json&useragent=Mozilla/%2F4.0(Firefox)&v=2"
countries=["ZA","MA","EG","NG"]
with open("jobs2.csv","w",newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for j in range(len(countries)):
        try:
            code=countries[j].lower()
        except AttributeError:
            code="na"
        location=req.get(url.format(0,code)).json()["results"][0]["country"]
        length=req.get(url.format(0,code)).json()["totalResults"]
        if location=="US":
            print("passed for {}".format(countries[j]))
            pass
        else:
            print("Getting for {}".format(code))
            for i in range(0,length,25):
                mUrl=url.format(i,code)
                data=req.get(mUrl).json()
                for j in data["results"]:
                    writer.writerow(j)
                print(i) 


