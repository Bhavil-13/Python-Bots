from selenium import webdriver
from time import sleep
from password import ipw, iun

class InstaPP:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        login_field = self.driver.find_element_by_xpath("//input[@name=\"iun\"]").send_keys(iun)

InstaPP(iun, ipw)