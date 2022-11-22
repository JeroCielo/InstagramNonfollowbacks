from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

username = input("Instagram Username or Email or Phone: ")
password = input("Instagram Password: ")

def clickCSSButton(browser, css_selector):
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    button.click()

def fillButton(browser, name, key):
    browser.find_element(By.NAME, "\"" + name + "\"").send_keys(key)

def login(browser):
    try:            
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys(username)
        browser.find_element(By.NAME, "password").send_keys(password)
        browser.find_element(By.NAME, "password").send_keys(u'\ue007')
    except Exception as e:
        print(e) 

def navigation(browser):
    browser.implicitly_wait(30)
    profile_css = 'alt="' + username + '\'s profile picture"'
    clickCSSButton(browser, profile_css)

def __main__():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.instagram.com/accounts/login/')
    login(browser)
    browser.find_element(By.NAME, "alt=\"" + username + "'s profile picture\"").send_keys(u'\ue007')
    navigation(browser)
    sleep(100)
    browser.close()
    return

__main__()
