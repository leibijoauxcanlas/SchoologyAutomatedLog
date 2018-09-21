import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =  webdriver.Chrome('/Users/bijoux/Desktop/chromedriver/chromedriver')
schoology = driver.get('http://www.schoology.com')
time.sleep(2)
login = driver.find_element_by_id('login-header')
login.click()
emailinput = driver.find_element_by_xpath('//input[@name= "mail"]').send_keys('emailhere@email.com')
passwordinput = driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('passwordhere')
driver.find_element_by_xpath('//input[@class="form-submit"]').click()
time.sleep(5)
driver.find_element_by_xpath('//a[@aria-controls="course-menu-dropdown"]').click()
time.sleep(3)
driver.find_element_by_xpath('//a[@href="/course/1560268205"]').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@href="/course/1560268205/updates"]').click()
time.sleep(2)
driver.find_element_by_xpath('//iframe[@id="edit-body_ifr"]').click()
time.sleep(2)
browser.close()
