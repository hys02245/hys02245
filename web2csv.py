#!/usr/bin/env python
# coding: utf-8

# In[99]:


import time
import csv
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\AMD\Desktop\TEST\chromedriver")
default_url = "http://www.kingbus.com.tw/ticketRoute.php"
driver.get(default_url)

driver.implicitly_wait(5)

driver.find_element_by_id("area").send_keys("台北")
time.sleep(0.1)
driver.find_element_by_id("origin").send_keys("臺北轉運站")
time.sleep(0.1)
driver.find_element_by_id("destination").send_keys("朝馬轉運站")

driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div/div[2]/input[1]').click()

raw = driver.find_elements_by_xpath('//*[@id="wrapper"]/div[2]/div/div[2]/ul/li')

with open(r"C:\Users\AMD\Desktop\TEST\output.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(['route', 'description'])
    
    for route in raw:
        
        row = route.text.split(' ',1)[1].replace(' ','')
        col = row.split('\u3000')
        
        writer.writerow([col[0], col[1]])
driver.quit()


# In[ ]:




