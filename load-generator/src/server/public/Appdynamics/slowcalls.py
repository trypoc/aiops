import os
from selenium import webdriver
chrome_path="C:\\Program Files (x86)\\Python 3.6.1 (64-bit)\\Scripts\\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.implicitly_wait(10)
for i in range(1,10):
	driver.get('http://10.210.16.246:8780/konakart/Games/1_2_-1_-1.action')
	driver.implicitly_wait(10)
	driver.get('http://10.210.16.246:8780/konakart/DVD-Movies/1_3_-1_-1.action')
	driver.implicitly_wait(10)