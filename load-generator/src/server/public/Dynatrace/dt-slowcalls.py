import os 
from selenium import webdriver
chrome_path="C:\\Users\\MF35121T\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://10.210.16.8:8780/konakart/Welcom.action')
driver.implicitly_wait(10)
for i in range (0,20):    
	driver.get('http://10.210.16.8:8780/konakart/Games/1_2_-1_-1.action')  
	driver.implicitly_wait(10)
	driver.get('http://10.210.16.8:8780/konakart/DVD-Movies/1_3_-1_-1.action')    
	driver.implicitly_wait(10)
driver.quit()