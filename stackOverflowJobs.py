from bs4 import BeautifulSoup as soup
import pandas
import requests as req
import math
import random
import pandas as pd
from datetime import datetime, timedelta
import csv


headers=(
    {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'},
    {'user-agent':'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'},
    {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'},
    {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'},
    {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'},
    {'user-agent':'Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; http://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0'},
    {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'},
    {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'},
    {'user-agent':'Mozilla/5.0 (X11; od-database-crawler) Gecko/20100101 Firefox/52.0'},
    {'user-agent':'Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.2.16) Gecko/20110323 Ubuntu/10.04 (lucid) Firefox/3.6.16'},
)

url="https://stackoverflow.com/jobs?sort=i&pg={}"

with open("stack.csv","w",newline="") as tFile:
    writer=csv.DictWriter(tFile,fieldnames=["Job Title","Company","Location","Remote","Relocation","Compensation","tags"])
    writer.writeheader()
    for k in range(38): 
        page=soup(req.get(url.format(k),headers=random.choice(headers)).text,"lxml")
        containers=page.find_all("div",{"class":"-job-summary"})
        for i in containers:
            title=i.div.h2.text.strip()
            date=i.find_all("span",{"class":"ps-absolute"})[0].text.strip()
            company=i.find_all("div",{"class":"-company"})[0].span.text.strip()
            location=i.find_all("div",{"class":"-company"})[0].find_all("span",{"class":"fc-black-500"})[0].text.strip().strip("- \r\n")
            try:
                visa=i.find_all("span",{"class":"-visa"})[0].text.strip()
            except IndexError:
                visa=""
            try:
                remote=i.find_all("span",{"class":"-remote"})[0].text.strip()
            except IndexError:
                remote=""
            try:
                relocation=i.find_all("span",{"class":"-relocation"})[0].text.strip()
            except IndexError:
                relocation=""
            try:
                compensation=i.find_all("span",{"class":"-salary"})[0].text.strip()
            except IndexError:
                compensation=""
            tagCont=i.find_all("a",{"class","post-tag job-link no-tag-menu"})
            tags=[]
            for j in tagCont:
                tags.append(j.text)
            writer.writerow({
                "Job Title":title,
                "Company":company,
                "Location":location,
                "Remote":remote,
                "Relocation":relocation,
                "Compensation":compensation,
                "tags":",".join(tags)
            })


