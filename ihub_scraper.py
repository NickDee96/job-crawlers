import requests as req
from bs4 import BeautifulSoup as soup
import csv

def scraper(filename):
    with open(filename,"w",newline="") as iFile:
        writer=csv.DictWriter(iFile,fieldnames=["Job","Company","City","Country","Company Link","Job Link","Job Category","Date"])
        writer.writeheader()
        for i in [1,2]:
            url="https://ihub.co.ke/jobs/{}".format(i)
            page=soup(req.get(url).text,"lxml")
            conts=page.findAll("div",{"class":"row"})
            for j in conts:
                jobName=j.findAll("h3")[0].a.text.strip()
                jobLink=("https://ihub.co.ke"+j.findAll("h3")[0].a["href"])
                compLink=j.findAll("a",{"class":"post-company"})[0]["href"]
                compName=j.findAll("a",{"class":"post-company"})[0].text
                jobCity=j.findAll("div",{"class":"job-location"})[0].text.split(", ")[0]
                jobCountry=j.findAll("div",{"class":"job-location"})[0].text.split(", ")[1]
                jobCat=j.findAll("div",{"class":"job-cat"})[0].text
                date=j.findAll("div",{"class":"job-time"})[0].text
                writer.writerow({
                    "Job":jobName,
                    "Company":compName,
                    "City":jobCity,
                    "Country":jobCountry,
                    "Company Link":compLink,
                    "Job Link":jobLink,
                    "Job Category":jobCat,
                    "Date":date
                })


if __name__ == "__main__":
    scraper("data/ihub.05.02.csv")



