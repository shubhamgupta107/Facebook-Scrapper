from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from linkHelper import processLink


driver = webdriver.Chrome()

danceL      =    ['Western Dance Academy', 'Classical Dance Academy', 'Bollywood Dance Academy', 'Zumba Academy', 'Bhangra Academy']
yogaL       =    ['Yoga Classes']
foreignL    =    ['French Classes', 'German Classes', 'English Classes']
chessL      =    ['Chess Classes']
singingL    =    ['Singing Classes']
storyL      =    ['Story Telling']

# cities = ['Mumbai, Maharashtra', 'Bangalore, India', 'Delhi, India', 'Kolkata', 'Chennai, India']
# danceL = ['Western Dance Academy India']
# danceL = []
# yogaL = []
cities = ['Bangalore, India']
types = {'dance' : danceL, 'yoga': yogaL, 'foreignLanguage': foreignL, 'chess': chessL, 'singing': singingL, 'story': storyL}
# types = {'dance' : danceL, 'yoga': yogaL}
driver.get('https://www.facebook.com')
time.sleep(20) # Enter username and password

for city in cities:
    toSave = city.partition(' ')[0]
    toSave = toSave[0:len(toSave)-1]
    writer = pd.ExcelWriter('{}.xlsx'.format(toSave), engine='xlsxwriter')  # pylint: disable=abstract-class-instantiated
    for category, titles in types.items():
        total = []
        for title in titles:
            toSearch = title.replace(' ', '%20')
            url = 'https://www.facebook.com/search/pages/?q=' + toSearch
            driver.get(url)
            time.sleep(2)
            try:
                pageButton = driver.find_element_by_xpath("//*[contains(text(), 'Pages')]")
                pageButton.click()
                time.sleep(2)
                locationBox = driver.find_element_by_xpath("//*[contains(text(), 'Location')]")
                locationBox.click()
                inpBox = driver.find_elements_by_tag_name('input')
                box = inpBox[1].send_keys(city)
                time.sleep(4)
                suggestionBox = driver.find_element_by_xpath("//*[contains(text(), '" + city + "')]")
                suggestionBox.click()
            except:
                continue
            for i in range(10):
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(1)
            try:
                profiles = driver.find_elements_by_class_name('sjgh65i0')
            except:
                profiles = None
            
            links = []
            for profile in profiles:
                try:
                    like = profile.find_element_by_class_name('g0qnabr5').text
                    link = profile.find_element_by_tag_name('a')
                    if(like.find('K') != -1):
                        links.append(link.get_attribute('href'))
                except:
                    print("Can't fetch Likes")

            links = list(dict.fromkeys(links))
            
            sub = title.partition(' ')[0]
            for url in links:
                ret = processLink(url, driver) + tuple([sub])
                if(ret[0] is not None):
                    total.append(ret)
                print(ret)
            
        df = pd.DataFrame(total, columns = ['NAME','DESCRIPTION','LIKES','FOLLOW','WEBSITE','PHONE NO.', 'LOCATION', 'URL', 'TYPE'])
        df = df.set_index('NAME')
        df = df.loc[~df.index.duplicated(keep = 'first')]
        df.to_excel(writer, sheet_name = category)
    writer.save()