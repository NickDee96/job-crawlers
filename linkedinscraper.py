from bs4 import BeautifulSoup as soup
from selenium import webdriver
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
import requests as req
import csv


#driver=webdriver.Firefox(executable_path='C:\\geckodriver\\geckodriver.exe')
#driver.get('https://www.linkedin.com/uas/login')
#driver.execute_script("document.getElementsByName('session_key')[0].value='nick@braveventurelabs.com'")#inserting email   
#driver.execute_script("document.getElementsByName('session_password')[0].value='rWF7mWE9vq'")#inserting email
#driver.find_element_by_css_selector('.btn__primary--large').click()
#driver.get('https://www.linkedin.com/jobs/search/?distance=25&f_TPR=r604800&keywords=&location=Kenya&locationId=ke%3A0')
#page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
#containers=page.findAll('li',{'class':'occludable-update'})

#f=open('linkedinJobs.csv','a',newline='')
#f.write(
#    '"'+'Role'+'"'+','+
#    '"'+'Company'+'"'+','+
#    '"'+'Location'+'"'+'\n'
#)
#for j in range(0,700,20):
#    link=('https://www.linkedin.com/jobs/search/?distance=25&f_TPR=r604800&keywords=&location=Kenya&locationId=ke%3A0&start={}'.format(str(j)))
#    driver.get(link)
#    page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
#    containers=page.findAll('li',{'class':'occludable-update'})
#    for i in range(0,len(containers)):
#        try:
#            role=containers[i].findAll('h3')[0].text.strip()
#            company=containers[i].findAll('h4')[0].text.strip()
#            Location=containers[i].findAll('h5')[0].text.strip()
#            print(
#                '"'+role+'"'+','+
#                '"'+company+'"'+','+
#                '"'+Location+'"'+'\n'
#            )
#            f.write(
#                '"'+role+'"'+','+
#                '"'+company+'"'+','+
#                '"'+Location+'"'+'\n'
#            )
#        except IndexError:
#            pass
#f.close()


class jContainer:
    def __init__(self,i):
        self.name=i.div.h3.text
        self.link=i.a['href']
        try:
            self.company=i.div.h4.a.text
            self.compLink=i.div.h4.a['href']
        except AttributeError:
            self.company=i.div.h4.text
            self.compLink=''
        self.location=i.div.div.span.text
        self.date=i.div.div.time['datetime']
        self.out= {'Job':self.name,
                'Job Link':self.link,
                'Company':self.company,
                'Company Link':self.compLink,
                'Location':self.location,
                'Date posted':self.date}
                


cookie="AQEDAStgW9sFQHE9AAABbkaSr1wAAAFuap8zXE0AvCTHUvWXU-U5rCFNfLnCZaYel45mVTZWjxEgBwq_nEIrUrnQLqPg-ywnjozoLK1UvJLCJOF15M6QB11NTnfSEmGGMMK64OSjuk4dFkGexO131XMd"
url="https://www.linkedin.com/mwlite/search/jobs?locationId=ke:0&f_F=mgmt,it,bd&f_TP=1%2C2"
background=False
def getJobs(url):
    if background ==  True:
        opts=webdriver.FirefoxOptions()
        opts.add_argument('--headless')
    else:
        opts=webdriver.FirefoxOptions()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>")            
    driver=webdriver.Firefox(executable_path = 'C:\\geckodriver\\geckodriver.exe',firefox_options=opts,firefox_profile=profile)
    driver.get('https://www.linkedin.com')
    ## Adding the LinkedIn session cookie
    driver.add_cookie({
        "name": "li_at",
        "value": cookie,
        "domain":".www.linkedin.com"
    })
    driver.get(url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".secondary"))
    )
    try:
        element.click()
    except ElementClickInterceptedException:
        time.sleep(5)
        element.click()
    elem=driver.find_element_by_css_selector("#search-alert-container")
    actions = ActionChains(driver)
    actions.move_to_element(elem).send_keys(Keys.SPACE)
    for i in range(200):
        actions.perform()
        print(i)
    page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
    results=page.find_all("li",{"class":"entity-item"})
    with open("LinkedIn.csv","w",newline="") as jFile:
        writer=csv.DictWriter(jFile,fieldnames=["Job","Company","Location","Days posted"])
        writer.writeheader()
        for i in results:
            try:
                date=i.find_all("div",{"class":"job-list-date small"})[0].text
            except IndexError:
                date=""
            compName=i.find_all("dd",{"class":"headline"})[0].text
            jName=i.find_all("dt",{"class":"name"})[0].text
            try:
                jLoc=i.find_all("div",{"class":"location"})[0].text
            except IndexError:
                jLoc=""
            writer.writerow({
                "Job":jName,
                "Company":compName,
                "Location":jLoc,
                "Days posted":date
            })
            print(jName)









