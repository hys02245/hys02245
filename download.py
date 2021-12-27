#!/usr/bin/env python
# coding: utf-8

# In[124]:


import time
from selenium import webdriver
import os
import urllib

chromeOptions = webdriver.ChromeOptions()

prefs = {"profile.default_content_settings.popups" : 0,
         "download.default_directory" : r"C:\Users\AMD\Desktop\TEST\q2test",
         "profile.default_content_setting_values.automatic_downloads" : 1}

chromeOptions.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(r"C:\Users\AMD\Desktop\TEST\chromedriver", chrome_options = chromeOptions)

default_url = "https://www.ceec.edu.tw/xmfile?xsmsid=0J052424829869345634"

driver.get(default_url)

driver.implicitly_wait(5)

next_bottom = 1

start = time.time()

while next_bottom == 1 :
    
    for i in range(1, (len(driver.find_elements_by_class_name("title"))) ) :
    
        if (int(driver.find_elements_by_class_name("date")[i].text.split('-')[0])-109) < 1 :
        
            year = driver.find_elements_by_class_name("title")[i].text.split("學")[0]
        
            path = r"C:\Users\AMD\Desktop\TEST\q2test" + "\\" + year
        
            folder = os.path.exists(path)
        
            if not folder :
                os.makedirs(path)
        
            folder_subject = driver.find_elements_by_class_name("title")[i].text
        
            sub_path = path + "\\" + folder_subject
        
            sub_folder = os.path.exists(sub_path)
        
            if not sub_folder :
                os.makedirs(sub_path)
        
            locations_father = driver.find_elements_by_class_name("download")[i]
        
            locations = locations_father.find_elements_by_css_selector('ul>li>a')
        
            for locate in locations : 
            
                if locate.get_attribute("class") == "file_ext file_pdf" :   
                
                    link = locate.get_attribute("href")
                
                    title = locate.get_attribute("title")
                
                    urllib.request.urlretrieve(link, sub_path + '\\' + title + '.pdf')
                    
    next_bottom = len(driver.find_elements_by_class_name("next"))
    
    if next_bottom == 1 :
        
        driver.find_element_by_class_name("next").click()
        time.sleep(0.5)
        
end = time.time()

print("從開始到結束所需秒數 :" , end - start)

driver.close()

