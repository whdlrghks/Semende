#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 13:13:27 2018

@author: ikhwan
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import re

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)




driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')


driver.get('https://www.shilladfs.com/estore/kr/ko/login')
driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/div[2]/div/a').click()
driver.implicitly_wait(2)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]

driver.switch_to_window(window_after)

driver.find_element_by_name('j_username').send_keys('john6939')
driver.find_element_by_name('j_password').send_keys('whdlrghks1!')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div/div/div[2]/div[1]/a').click()
driver.implicitly_wait(2)
driver.switch_to_window(window_before)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[1]/ul/li[3]/a').click()
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

reserved = soup.find("dl",{"class":"save"}).find("dd").find("div").find("span").find("em")
price = remove_html_tags(str(reserved))
print(price)





driver = webdriver.Chrome('/Users/ikhwan/capstone/chromedriver')

driver.get("https://www.shilladfs.com/estore/kr/ko/login")
driver.find_element_by_name('loginLpId').send_keys('john6939')
driver.find_element_by_name('password').send_keys('whdlrghks1!')

driver.implicitly_wait(3)

from selenium import webdriver
from bs4 import BeautifulSoup


try:
    print(driver.current_url)
except :
    driver.switch_to_window(window_before)
    print(driver.current_url)

