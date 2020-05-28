# Facebook Scrapper

It is a python script made to scrape data from facebook pages and groups. It is based on selenium web driver. It reads data from facebook and enters useful data into excel sheet.

## Usage:

### First Install the basic libraries and driver

- First install the chrome driver. [click here](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/)
```
pip3 install selenium
pip3 install pandas
pip3 install xlswriter
```
### To Run the Script

- to Scrape pages use 
```
python3 pages/scraper.py
```
- to Scrape groups use 
```
python3 groups/scraper.py
```
