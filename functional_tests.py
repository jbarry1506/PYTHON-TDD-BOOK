import selenium
from selenium import webdriver
import vars


browser = webdriver.Firefox()

browser.get(vars.my_localhost)

try:
    assert 'Django' in browser.title
    print("Django success")
except:
    print("Django didn't work")

browser.quit()