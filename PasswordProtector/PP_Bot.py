from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from password import InstaP as i
from password import LMS as l
class Instagram:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com')
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
        sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(10)
class LMS:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://learn.iiitb.net')
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[1]/input').send_keys(username)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/div[2]/input').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[1]/form/button').click()
        sleep(10)
        sleep(10)
#Instagram(i.userName,i.password)
LMS(l.userName, l.password)