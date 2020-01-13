import requests as req
from bs4 import BeautifulSoup as soup
import csv

murl="https://www.careers24.com/jobs/se-it/?pagesize=100&sort=dateposted&page={}"

with open("careers24.csv","w",newline="") as jFile:
    writer=csv.DictWriter(jFile,fieldnames=["JobTitle","Description","Company","Job Link","Industry","Employment Type","Location","Compensation","Date posted"])
    writer.writeheader()
    for j in range(1,18):
        url=murl.format(j)
        page=soup(req.get(url).text,"lxml")
        containers=page.find_all("div",{"class":"row job_search_wrapper"})
        for i in containers:
            jLink=("https://www.careers24.com"+i.div.h4.a["href"])
            jName=i.div.h4.a.span.text
            mContainers=i.find_all("div",{"class":"job_search_content"})[0].find_all("p")
            jLoc=mContainers[0].text.strip()
            jIndustry=mContainers[1].text.strip()
            jCompensation=mContainers[2].text.strip()    
            etype=mContainers[3].text.strip()
            sContainer=i.find_all("div",{"class":"job_search_summary"})[0]    
            jSum=sContainer.p.span.text
            try:
                cName=sContainer.find_all("span",{"class":"schema"})[0].text
            except IndexError:
                cName=""
            try:
                date=sContainer.find_all("span",{"class":"schema"})[1]["content"]
            except (IndexError,KeyError):
                date=""
            print(jName+"  "+str(containers.index(i)))
            writer.writerow({
                "JobTitle":jName,
                "Description":jSum,
                "Company":cName,
                "Job Link":jLink,
                "Industry":jIndustry,
                "Employment Type":etype,
                "Location":jLoc,
                "Compensation":jCompensation,
                "Date posted":date
            })

