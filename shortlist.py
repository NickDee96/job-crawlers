from bs4 import BeautifulSoup as soup
from selenium import webdriver
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


driver=webdriver.Firefox(executable_path = 'C:\\geckodriver\\geckodriver.exe')
driver.get('https://www.shortlist.net/webportal/#/dashboard/all-jobs')
driver.find_element_by_css_selector('#googleBtn > span:nth-child(1)').click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[1])
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#identifierId"))
    )
element.send_keys("nick@braveventurelabs.com")
driver.find_element_by_css_selector("#identifierNext > span:nth-child(3)").click()
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
try:
    element.send_keys("KnightRift!475")
except ElementNotInteractableException:
    time.sleep(2)
    element.send_keys("KnightRift!475")
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#passwordNext > span:nth-child(3) > span:nth-child(1)"))
    )
try:
    element.click()
except ElementClickInterceptedException:
    time.sleep(2)
    element.click()
driver.switch_to_window(driver.window_handles[0])
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/snack-bar-container/app-gdpr-dialog/div/p[2]/a').click()

def scraper1(driver):
        #driver.find_element_by_xpath('/html/body/div[2]/div/div/snack-bar-container/app-gdpr-dialog/div/p[2]/a').click()
        f=open('jobRoles.csv','w',newline='')
        f.write('"'+'Role'+'"'+','+
                '"'+'Company'+'"'+','+
                '"'+'Location'+'"'+','+
                '"'+'Company Link'+'"'+','+
                '"'+'Role Link'+'"'+'\n')
        page=soup(driver.page_source,'lxml')
        containers=page.findAll('div',{'class':'job-details'})

        for i in containers:
            roleName=''
            compName=''
            jobLoc=''
            compLink=''
            roleLink=''
            roleName=i.div.a['title']
            roleLink=('https://www.shortlist.net/webportal/'+i.div.a['href'])
            compName=i.findAll('a',{'class':'company-name'})[0].span.text
            compLink=i.findAll('a',{'class':'company-name'})[0]['href']
            jobLoc=i.findAll('p',{'class':'job-location'})[0].text
            f.write(
                '"'+roleName+'"'+','+
                '"'+compName+'"'+','+
                '"'+jobLoc+'"'+','+
                '"'+compLink+'"'+','+
                '"'+roleLink+'"'+'\n'
        )
        f.close()

scraper1(driver)

driver=webdriver.Firefox(executable_path = 'C:\\geckodriver\\geckodriver.exe')
f=open('roles.csv','a',newline='')
f.write(
        '"'+'Role'+'"'+','+
        '"'+'Company'+'"'+','+
        '"'+'Location'+'"'+','+
        '"'+'Role Link'+'"'+'\n'

)

for i in range(1270,1400):
    try:
        driver.delete_all_cookies()
        link=('https://www.shortlist.net/webportal/#/job-details/'+str(i))
        driver.get(link)
        time.sleep(5)
        page=soup(driver.page_source,'lxml')
        if len(page.findAll('mat-card-title',{'class':'mat-card-title'}))==0:
            #model1
            container=page.findAll('section',{'id':'jbpost-cover'})
            jobName=container[0].findAll('h1',{'class':'text-center'})[0].text
            compName=container[0].div.div.h3.text
            jobLoc=container[0].findAll('h4',{'_ngcontent-c5':''})[0].text
        else:
            #model2
            compName=page.findAll('mat-card-title',{'class':'mat-card-title'})[0].text.split(' is')[0]
            page.findAll('mat-card-content',{'class':'md-content-intro'})
            t1=page.findAll('mat-card-content',{'class':'md-content-intro'})[0].div.div.text
            if t1=='':
                containers=page.findAll('mat-card-content',{'class':'md-content-intro'})[0].findAll('li')
                for i in containers:
                    if 'Role' in i.text:
                        jobName=i.text.split(': ')[1].strip()
                    elif 'Position' in i.text:
                        jobName=i.text.split(': ')[1].strip()
                    elif 'Location' in i.text:
                        jobLoc=i.text.split(': ')[1].strip()
            else:
                containers=page.findAll('mat-card-content',{'class':'md-content-intro'})[0].findAll('div')
                for i in containers:
                    if 'Role' in i.text:
                        jobName=i.text.split(': ')[1].strip()
                    elif 'Position' in i.text:
                        jobName=i.text.split(': ')[1].strip()
                    elif 'Location' in i.text:
                        jobLoc=i.text.split(': ')[1].strip()
        print(jobName,compName,jobLoc,link)
        f.write('"'+jobName+'"'+','+
        	'"'+compName+'"'+','+
        	'"'+jobLoc+'"'+','+
        	'"'+link+'"'+'\n'
        )
    except:
            pass 
f.close()

                
driver=webdriver.Firefox(executable_path = 'C:\geckodriver\geckodriver.exe')
driver.get('https://www.shortlist.net/webportal/#/job-details/481')
time.sleep(5)
page=soup(driver.page_source,'lxml')
if len(page.findAll('mat-card-title',{'class':'mat-card-title'}))==0:
        #model1
        container=page.findAll('section',{'id':'jbpost-cover'})
        jobName=container[0].findAll('h1',{'class':'text-center'})[0].text
        compName=container[0].div.div.h3.text
        jobLoc=container[0].findAll('h4',{'_ngcontent-c5':''})[0].text
else:
        #model2
        compName=page.findAll('mat-card-title',{'class':'mat-card-title'})[0].text.split(' is')[0]
        t=page.findAll('mat-card-content',{'class':'md-content-intro'})



page=soup(req.get("https://www.shortlist.net/webportal/#/job-details/1390").text,"lxml")

