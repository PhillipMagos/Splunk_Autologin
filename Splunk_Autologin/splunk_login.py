from selenium import webdriver 
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys

from User_Info import password
# print(password)
from User_Info import USER
# print(USER)


driver= webdriver.Chrome()

url = 'https://splunk.listrak.com/en-US/app/search/data_export__custom_export?form.environment_dropdown_token=machinename!%3D*dev*%20machinename!%3D*stg*&form.data_export_time_token.earliest=-24h%40h&form.data_export_time_token.latest=now'
driver.get(url)
sleep(2)
x3 = driver.find_element('xpath', '/html/body/div[2]/div/div/div[1]/form/fieldset/div[1]/input').send_keys(USER)
sleep(2)
b = driver.find_element('id', 'password').send_keys(password)
sleep(2)
submit = driver.find_element('xpath', '/html/body/div[2]/div/div/div[1]/form/fieldset/input[1]').click()