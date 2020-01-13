from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests as req
import csv

driver=webdriver.Firefox(executable_path='geckodriver/geckodriver')
driver.get("https://www.fuzu.com/categories/it-software")
for i in range(70):
    try:
        driver.find_element_by_xpath("/html/body/div[2]/section/div[1]/div/div[2]/div/div/div[2]/a").click()
    except NoSuchElementException:
        break
#driver.find_element_by_xpath("/html/body/div[2]/section/div[1]/div/div[2]/div/div/div[1]/div[2]/div/span[2]").click()
page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
driver.quit()
pButtons=page.findAll("h3",{"class","font-18 slim-titles job-titles"})
with open("fuzu.csv","w",newline="") as fFile:
    writer=csv.DictWriter(fFile,fieldnames=["Job","Job Link","Company","Company Link","Salary Range","Contract Type"])
    writer.writeheader()
    for i in pButtons:
        jLink=("https://www.fuzu.com"+i.span.a["href"])
        jName=i.span.a.text
        print("Getting for {}".format(jName))
        page2=soup(req.get(jLink).text,"lxml")
        cName=page2.find_all("div",{"class","mb-500"})[0].a.text
        cLink=("https://www.fuzu.com"+page2.find_all("div",{"class","mb-500"})[0].a["href"])
        sRange=page2.find_all("div",{"class","flex-full"})[0].findAll("p")[0].text.split(" | ")[0].replace("Salary range:\xa0","")
        cType=page2.find_all("div",{"class","flex-full"})[0].findAll("p")[0].text.split(" | ")[1].replace("Contract type:\xa0","")
        uDict={
            "Job":jName,
            "Job Link":jLink,
            "Company":cName,
            "Company Link":cLink,
            "Salary Range":sRange,
            "Contract Type":cType
        }
        writer.writerow(uDict)
