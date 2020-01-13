from bs4 import BeautifulSoup as soup
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#opts=webdriver.FirefoxOptions()
#opts.add_argument('--headless')
driver=webdriver.Firefox(executable_path = 'C:\\geckodriver\\geckodriver.exe')

driver.get("https://angel.co/login")
driver.find_element_by_css_selector("#user_email").send_keys("nick@braveventurelabs.com")
driver.find_element_by_css_selector("#user_password").send_keys("Mumerowanjeri18")
driver.find_element_by_css_selector(".c-button").click()

driver.get("https://angel.co/companies?locations[]=2241-Kenya")

for i in range(200):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".more"))
        )
        element.click()
        print(i)
    except StaleElementReferenceException:
        time.sleep(3)
        pass

page=soup(driver.execute_script("return document.body.innerHTML"),'lxml')
with open("test.html","w",newline="") as testFile:
    testFile.write(str(page))

with open("KenyanCompaniesAngelist2.csv","w",newline="") as aFile:
    writer=csv.DictWriter(aFile,fieldnames=[
        "Company",
        "Link",
        "Logo",
        "Pitch",
        "Joined",
        "Location",
        "Market",
        "Website",
        "Employees",
        "Stage",
        "Funding Raised"
    ])
    writer.writeheader()
    rows=page.find_all("div",{"data-_tn":"companies/row"})
    for i in range(1,len(rows)):
        compName=rows[i].find("div",{"class":"name"}).a.text.strip()
        compLink=rows[i].find("div",{"class":"name"}).a["href"]
        logoLink=rows[i].find("img",{"class":"angel_image"})["src"]
        compPitch=rows[i].find("div",{"class":"pitch"}).text.strip()
        joined=rows[i].find("div",{"data-column":"joined"}).find("div",{"class":"value"}).text.strip()
        location=rows[i].find("div",{"data-column":"location"}).find("div",{"class":"value"}).text.strip()
        market=rows[i].find("div",{"data-column":"market"}).find("div",{"class":"value"}).text.strip()
        website=rows[i].find("div",{"data-column":"website"}).find("div",{"class":"value"}).text.strip()
        employees=rows[i].find("div",{"data-column":"company_size"}).find("div",{"class":"value"}).text.strip()
        stage=rows[i].find("div",{"data-column":"stage"}).find("div",{"class":"value"}).text.strip()
        funding_raised=rows[i].find("div",{"data-column":"raised"}).find("div",{"class":"value"}).text.strip()
        writer.writerow({
            "Company":compName,
            "Link":compLink,
            "Logo":logoLink,
            "Pitch":compPitch,
            "Joined":joined,
            "Location":location,
            "Market":market,
            "Website":website,
            "Employees":employees,
            "Stage":stage,
            "Funding Raised":funding_raised            
        })
        print(i)


