import requests as req
from bs4 import BeautifulSoup as soup
import csv
from selenium import webdriver

url="https://www.dice.com/jobs?location=India&latitude=20.593684&longitude=78.96288000000004&countryCode=IN&locationPrecision=Country&radius=30&radiusUnit=mi&page=1&pageSize=20&facets=employmentType%7CpostedDate%7CworkFromHomeAvailability%7CemployerType&language=en"
page=soup(req.get(url).text,"lxml")
driver = webdriver.PhantomJS(executable_path="C:\\PhantomJs\\bin\phantomjs\\phantomjs.exe")
driver.get(url)
with open("diceIndiaJobs.csv","w",newline="") as dFile:
    writer=csv.DictWriter(dFile,fieldnames=["Job Title","Job Link","Company Name","Company Link","Location","Job Type","Date Posted","Description"])
    writer.writeheader()
    page=soup(driver.page_source,"lxml")
    containers=page.find_all("dhi-search-card",{"data-cy":"search-card"})
    for i in containers:
        jTitle=i.find_all("h5")[0].a.text
        jLink=i.find_all("h5")[0].a["href"]
        compName=i.find_all("div",{"class":"card-company"})[0].find_all("a",{"class":"ng-star-inserted"})[0].text
        compLink=i.find_all("div",{"class":"card-company"})[0].find_all("a",{"class":"ng-star-inserted"})[0]["href"]
        Loc=i.find_all("div",{"class":"card-company"})[0].find_all("span",{"data-cy":"search-result-location"})[0].text
        jobtype=i.find_all("span",{"data-cy":"search-result-employment-type"})[0].text
        date_posted=i.find_all("span",{"class":"posted-date"})[0].text
        dscptn=i.find_all("div",{"class":"card-description"})[0].text
        upDict={
            "Job Title":jTitle,
            "Job Link":jLink,
            "Company Name":compName,
            "Company Link":compLink,
            "Location":Loc,
            "Job Type":jobtype,
            "Date Posted":date_posted,
            "Description":dscptn
        }
        writer.writerow(upDict)

driver.quit()
len(containers)
with open("test.html","w") as tFile:
    tFile.write(str(driver.page_source))