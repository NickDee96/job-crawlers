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
results=page.find_all("div",{"data-test":re.compile('StartupResult')})

with open("data/angelist/AngelListings.csv","w",encoding="utf-8",newline="") as aFile:
    writer=csv.DictWriter(aFile,fieldnames=["Job Title","Company","Location","Salary","Job_link","Company Link"])
    writer.writeheader()
    for i in range(len(results)):
        comp_name=results[i].find("a",{"class":re.compile('^name_*')}).text
        comp_link="https://angel.co"+results[i].find("a",{"class":re.compile('^name_*')})["href"]
        listings=results[i].find("div",{"class":re.compile('^listings_*')}).find_all("div",{"class":re.compile('^listing_*')})
        for j in range(len(listings)):
            job_link="https://angel.co"+listings[j].a["href"]
            job_title=listings[j].find("span",{"class":re.compile('^title_*')}).text
            try:
                salary=listings[j].find("div",{"class":re.compile('^salaryEstimate*')}).text
                location=listings[j].find("span",{"class":"__halo_fontSizeMap_size--sm"}).text.strip(salary)
            except AttributeError:
                salary=""
                location=""
            writer.writerow({
                "Job Title":job_title,
                "Company":comp_name,
                "Location":location,
                "Salary":salary,
                "Job_link":job_link,
                "Company Link":comp_link
            })
            print("{}  ------>>  {}".format(comp_name,job_title))