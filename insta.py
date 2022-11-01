from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com")
time.sleep(2)

username = "nathan_clrd"
password = ""

cookie_btn = driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
cookie_btn.click()
time.sleep(2)


username_textbox = driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
username_textbox.send_keys(username)

password_textbox = driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password_textbox.send_keys(password)

time.sleep(2)

login_btn = driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
login_btn.click()
log
