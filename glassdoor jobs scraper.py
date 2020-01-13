from bs4 import BeautifulSoup as soup
import pandas
import requests as req
import math
import random
from datetime import datetime, timedelta

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
f=open('07-01.csv','a')
fileHeaders=('Job Name'+','+'Company'+','+'Link'+','+'Location'+','+'\n')
#f.write(fileHeaders)   
for i in range(1,16):
    url=('https://www.glassdoor.com/Job/nairobi-jobs-SRCH_IL.0,7_IC2896002_IP'+str(i)+'.htm?radius=25&fromAge=7')
    page=soup(req.get(url,headers=random.choice(headers)).text,'lxml')
    #jobLen=page.findAll('p',{'class':'jobsCount'})[0].text.split('\xa0')[0]
    jContainers=page.findAll('div',{'class':'jobContainer'})
    for j in jContainers:
        try:
            jobLink=('https://www.glassdoor.com'+j.a['href'])
            jobName=j.a.text
            compName=j.div.div.text
            jobLoc=j.findAll('span',{'class':'subtle loc'})[0].text
            f.write(jobName.replace(',','|')+','+compName.replace(',','|')+','+jobLink.replace(',','|')+','+jobLoc.replace(',','|')+','+'\n')
        except IndentationError:
            pass
    print('page '+str(i)+' is done \n')  
    print(url)  
f.close()
