from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


nameX = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[1]/h1'
descX1 = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/span'
# //*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/span
descX2 = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/span'
membersX1 = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/h1/div/span'
membersX2 = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/h1/div/span'
postADayX1 = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/span'
postADayX2 = '//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div[4]/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/span'
# It will return a tuple
def processLink(url, driver):
    driver.get(url + 'about/')
    delay = 5
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, nameX)))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    name = desc = members = postADay = None
    try:
        name = driver.find_element_by_xpath(nameX).text
    except:
        name = None
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'See more')]").click()
        try:
            desc = driver.find_element_by_xpath(descX1).text.replace('\n', ' ')
        except:
            try:
                desc = driver.find_element_by_xpath(descX2).text.replace('\n', ' ')
            except:
                print("Can't fetch some description")
    
    except:
        try:
            desc = driver.find_element_by_xpath(descX1).text
        except:
            desc = None
    
    try:
        members = driver.find_element_by_xpath(membersX1).text[2:]
    except:
        try:
            members = driver.find_element_by_xpath(membersX2).text[2:]
        except:
            members = None

    try:
        postADay = (int(driver.find_element_by_xpath(postADayX1).text.partition(' ')[0]) + 29) // 30
    except:
        try:
            postADay = (int(driver.find_element_by_xpath(postADayX2).text.partition(' ')[0]) + 29) // 30
        except:
            postADay = None
    
    return (name, desc, members, postADay, url)