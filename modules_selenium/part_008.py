# coding: utf8
""" 
@File: part_008.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/12/9 20:20
"""

from selenium import webdriver

webdriver.FirefoxOptions().binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
executable_path = r'./driver/firefox_107_0_1_x86_64/win/geckodriver.exe'
driver = webdriver.Firefox(executable_path=executable_path)
driver.get(url='https://baidu.com')
baidu_cookies = {data.get('name'): data.get('value') for data in driver.get_cookies()}
print(baidu_cookies)
driver.quit()


