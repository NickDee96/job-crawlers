import requests as req
from bs4 import BeautifulSoup as soup
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Firefox(executable_path = 'geckodriver/geckodriver')


url="https://www.careerjunction.co.za/jobs/information-technology?page=1"


driver.get(url)

with open("CareerJunction.25.10.csv","a",newline="") as tFile:
    writer=csv.DictWriter(tFile,fieldnames=["Job Title","Company","Location","Job Link","Employment Type","Compensation","Date Posted"])
    writer.writeheader()
    for i in range(1,71):
        page=soup(driver.page_source,"lxml")
        containers=page.find_all("div",{"class":"cardContentJob jsCardContentJob"})
        for j in containers:
            try:
                jTitle=j.find_all("span",{"itemprop":"title"})[0].text
                jLink=("https://www.careerjunction.co.za"+j.find_all("a",{"class":"noUnderline jobTitle"})[0]["href"])
                cName=j.find_all("span",{"itemprop":"hiringOrganization"})[0].text
                eType=j.find_all("span",{"itemprop":"employmentType"})[0].text
                jLocation=j.find_all("span",{"itemprop":"jobLocation"})[0].text
                compensation=j.find_all("span",{"itemprop":"baseSalary"})[0].text
                date=j.find_all("span",{"itemprop":"datePosted"})[0].text
                writer.writerow({
                    "Job Title":jTitle,
                    "Company":cName,
                    "Location":jLocation,
                    "Job Link":jLink,
                    "Employment Type":eType,
                    "Compensation":compensation,
                    "Date Posted":date
                })
            except IndexError:
                pass
        driver.find_element_by_css_selector("a.pageNumber:nth-child(4)").click()
    driver.quit()


