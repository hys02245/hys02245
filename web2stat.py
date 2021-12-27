#!/usr/bin/env python
# coding: utf-8

# In[46]:


import time
import csv
import pymongo
from selenium import webdriver

#取得資料

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

#存至資料庫

client = pymongo.MongoClient()

mydb = client["mydb"]

mycol = mydb["KKMT"] 

for route in raw:
    row = route.text.split(' ',1)[1].replace(' ','')
    col = row.split('\u3000')
    data = {'route' : col[0], 'description' : col[1]}
    mycol.insert_one(data)
    
driver.quit()

#統計長度

y = mycol.find({'route':{'$regex':".*埔里.*"}})
print("Route 中含有 埔里 的資料筆數 : ", len(list(y)))


# In[ ]:





# In[ ]:




