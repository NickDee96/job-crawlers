from bs4 import BeautifulSoup as soup
from selenium import webdriver
import pandas as pd
import os
import time
import csv
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

background=False
if background ==  True:
    opts=webdriver.FirefoxOptions()
    opts.add_argument('--headless')
else:
    opts=webdriver.FirefoxOptions()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>")            
driver=webdriver.Firefox(executable_path = 'C:\\geckodriver\\geckodriver.exe',firefox_options=opts,firefox_profile=profile)
driver.get('https://www.linkedin.com/uas/login')
driver.find_element_by_id('username').send_keys("nick@braveventurelabs.com")#inserting email   
driver.find_element_by_id('password').send_keys("rWF7mWE9vq")#inserting password
driver.find_element_by_css_selector('.btn__primary--large').click()
try:
    driver.find_element_by_css_selector(".secondary").click()
except NoSuchElementException:
    time.sleep(2)
    driver.find_element_by_css_selector(".secondary").click()
driver.get("https://www.linkedin.com/mwlite/search/jobs?&locationId=&locationName=kenya")
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
