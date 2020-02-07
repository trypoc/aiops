import os
import time
from selenium import webdriver
chrome_path="C:\\Users\\MF35121T\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.implicitly_wait(5000)

driver.get('http://10.210.16.96:8780/konakart/Welcom.action')
driver.implicitly_wait(5)


#Computer Peripherals
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/a[1]").click()
driver.implicitly_wait(5)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li[2]/a").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li[1]/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(50)


#Games
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/a[2]").click()
driver.implicitly_wait(5)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li[2]/a").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(50)


#DVD
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/a[3]").click()
driver.implicitly_wait(5)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li[2]/a").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li[1]/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(50)


#Software
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/a[4]").click()
driver.implicitly_wait(5)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li/a/span").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li[1]/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(50)

#Electronics
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/a[5]").click()
driver.implicitly_wait(5)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li[3]/a").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li[1]/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(50)


#Homes & Garden
driver.get('http://10.210.16.96:8780/konakart/Home-%26-Garden/1_24_-1_-1.action')
driver.implicitly_wait(50)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li[2]/a").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li[1]/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(50)


#Gifts
driver.get('http://10.210.16.96:8780/konakart/Gifts/1_21_-1_1.action')
driver.implicitly_wait(5)
#Product
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/ul/li/a/span").click()
driver.implicitly_wait(5)
#Product Name
driver.find_element_by_xpath("/html/body/div[4]/div/div[5]/div/div[2]/ul/li/div/a").click()
driver.implicitly_wait(5)
#Add to cart
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div[2]/div[1]/form/div[6]/a").click()
driver.implicitly_wait(5)

#Shopping cart
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/span[2]").click()
driver.implicitly_wait(50)

#CheckOut
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/form/div/a/span").click()
driver.implicitly_wait(50)

#Login
driver.find_element_by_name("loginUsername").send_keys("johnsmith@gmail.com")
driver.implicitly_wait(100)
driver.find_element_by_name("password").send_keys("Wipro@123")
driver.implicitly_wait(100)
driver.find_element_by_id("continue-button").click()
driver.implicitly_wait(100)

#Confirm Order
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/form/div[3]/a/span").click()
driver.implicitly_wait(100)

#Continue
driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div[1]/div/form/div[2]/div[2]/a/span").click()
driver.implicitly_wait(100)

#Log OFF
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div[1]/span[2]/a").click()
driver.implicitly_wait(100)

#Continue
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/div/form/div[2]/a/span").click()
driver.implicitly_wait(100)


driver.quit()