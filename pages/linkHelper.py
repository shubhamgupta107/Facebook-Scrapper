from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


nameX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/h1/span'
descX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/span/span'
peopleLikeX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/span/span[1]'
peopleFollowX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'
websiteX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[6]/div/div/div[2]/div/div/span/span/a'
phoneNoX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[7]/div/div/div[2]/div/div/span/span'
locationX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/span/a/span/div'
# It will return a tuple
def processLink(url, driver):
    driver.get(url)
    delay = 5
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, nameX)))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    name = desc = peopleLike = peopleFollow = website = phoneNo = location = None
    try:
        name = driver.find_element_by_xpath(nameX).text
    except:
        name = None
    try:
        desc = driver.find_element_by_xpath(descX).text
    except:
        desc = None
    try:
        peopleLike = driver.find_element_by_xpath(peopleLikeX).text
    except:
        peopleLike = None
    try:
        peopleFollow = driver.find_element_by_xpath(peopleFollowX).text
    except:
        peopleFollow = None
    try:
        website = driver.find_element_by_xpath(websiteX).text
    except:
        website = None
    try:
        phoneNo = driver.find_element_by_xpath(phoneNoX).text
    except:
        phoneNo = None
    try:
        location = driver.find_element_by_xpath(locationX).text
    except:
        location = None
    if(peopleFollow is not None):
        if(peopleFollow[0:3] == 'http'):
            website = peopleFollow
    if(phoneNo is not None):
        if(phoneNo[0] < '0' or phoneNo[0] > '9'):
            phoneNo = None
    return (name, desc, peopleLike, peopleFollow, website, phoneNo, location, url)