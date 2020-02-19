from bs4 import BeautifulSoup as soup
import requests as req
import csv
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#opts=webdriver.FirefoxOptions()
#opts.add_argument('--headless')
driver=webdriver.Firefox(executable_path = 'geckodriver/geckodriver')

driver.get("https://angel.co/login")
driver.find_element_by_css_selector("#user_email").send_keys("nim")
driver.find_element_by_css_selector("#user_password").send_keys("")
driver.find_element_by_css_selector(".c-button").click()
driver.get("https://angel.co/jobs")



page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
btnId=page.find("div",{"id":"main"}).find_all("div",{"class":re.compile('^styles_component*')})[1].find_all("div")[2]["class"][0]
driver.find_element_by_css_selector("."+btnId).click()





page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
clsName=page.find("div",{"class":"select__multi-value__remove"})["class"][0]
driver.find_element_by_css_selector(".{} > svg:nth-child(1) > path:nth-child(1)".format(clsName)).click()

driver.find_element_by_class_name("select__input").send_keys("Kenya")

for i in ["Kenya","Uganda","Tanzania","South Africa","Ghana","Nigeria"]:
    page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
    btnId=page.find("div",{"id":"main"}).find_all("div",{"class":re.compile('^styles_component*')})[1].find_all("div")[2]["class"][0]
    driver.find_element_by_css_selector("."+btnId).click()
    actions = ActionChains(driver)
    actions.send_keys(i)
    actions.pause(3)
    actions.send_keys(Keys.ENTER)
    actions.perform()


driver.find_element_by_xpath('//*[@id="react-select-32-option-0"]')





driver.find_element_by_css_selector("#react-select-3--value > div:nth-child(1)").click()
countries=["Kenya","Uganda","Tanzania","South Africa","Ghana"]
for i in countries:
    driver.find_element_by_css_selector("#locations").send_keys(i)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#react-select-3--option-0"))
    )
    element.click()






print("Starting scroll")
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(10)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            driver.execute_script("window.scrollTo(0, -100);")
            pagelen=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            print('Scrolling at '+str(pagelen))
            if pagelen==lenOfPage:
                match=True
                print("Finished Scrolling")
        elif lastCount>100000:
            match=True
            print("Reached Scrolling Limit")

page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
with open("test.html","w",newline="") as testFile:
    testFile.write(str(page))


page.find_all("")


page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
with open("test.html","w",newline="") as testFile:
    testFile.write(str(page))
with open("angelistJobs_naija.csv","w",newline="") as aFile:
    writer=csv.DictWriter(aFile,fieldnames=["Job","Category","Company","Location","Compensation","Link"])
    writer.writeheader()
    startupRows=page.findAll("div",{"class":re.compile('^styles_width100.*')})
    for k in range(len(startupRows)):
        sJobs=startupRows[k].div.a["href"]
        driver.get("https://angel.co"+sJobs+"/jobs")
        time.sleep(2)
        jPage=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
        cName=jPage.find("div",{"class":re.compile('^name_*')}).div.div.h1.a.text
        jRows=jPage.find_all("div",{"style":"height: auto; opacity: 1;"})
        for j in range(len(jRows)):
            jLink="https://angel.co"+jRows[j].div.a["href"]
            jField=jRows[j].div.a.div.h6.text
            jName=jRows[j].div.a.div.div.h4.text
            jLoc=jRows[j].find("span",{"class":re.compile('^location.*')}).text
            jComp=jRows[j].find("span",{"class":re.compile('^compensation.*')}).text
            writer.writerow({
                "Job":jName,
                "Category":jField,
                "Company":cName,
                "Location":jLoc,
                "Compensation":jComp,
                "Link":jLink
            })
            print(j)
        print(k)


