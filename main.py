from selenium import webdriver 
import time 
from bs4 import BeautifulSoup
import csv
# Base URL of Yahoo Finance
URL = "https://finance.yahoo.com/"

# Currency 
BTC_EUR = "BTC-EUR"

# Start the Driver
driver = webdriver.Chrome(executable_path = r"C:\Users\thiag\Documents\chrome-web-driver\chromedriver.exe")

# Hit the url of Yahoo Finance and wait for 2 seconds.
driver.get(URL)
time.sleep(2)

#
# Click on 'I agree' button and wait for a second.
# driver.find_element_by_xpath("//button[@value='agree']").click()
# time.sleep(1)

# Enter name of company in searchbox, and wait for 2 seconds.
driver.find_element_by_xpath("//input[@placeholder = 'Search for news, symbols or companies']").send_keys("BTC-EUR")
time.sleep(2)

# Click on Search icon and wait for 2 seconds.
driver.find_element_by_xpath("//button[@id= 'header-desktop-search-button']").click()
time.sleep(2)

# Driver clicks on Historical Data tab and sleeps for 2 seconds.
driver.find_element_by_xpath("//span[text() = 'Historical Data']").click()
time.sleep(2)

# Driver scrolls down three times to load the table.
driver.execute_script("window.scrollBy(0,700)")
time.sleep(2)

# Fetch the webpage and store in a variable.
webpage = driver.page_source

# Web page fetched from driver is parsed using Beautiful Soup.
HTMLPage = BeautifulSoup(driver.page_source, 'html.parser')

# Table is searched using class and stored in another variable.
Table = HTMLPage.find('table', class_='W(100%) M(0)')

# List of all the rows is store in a variable 'Rows'.
Rows = Table.find_all('tr', class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')

# Empty list is created to store the data
extracted_data = []

# Loop to go through each row of table
btc_file = open('eur_btc_rates.csv', 'w', newline="")
writer = csv.writer(btc_file)
writer.writerow(["Date","Close"])
for i in range(0, 10):
  Values = Rows[i].find_all('td')
  
  # Values "Date" and "Close" are extracted and stored in dictionary
  if len(Values) == 7:
   date = Values[0].find('span').text.replace(',', '').strip()
   close = Values[4].find('span').text.replace(',', '').strip()

  
  writer.writerow([date,close])

btc_file.close()
driver.close()