from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

username = input()
password = input()
count = 0

def clickCSSButton(browser, css_selector):
    button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    button.click()

def fillButton(browser, name, key):
    browser.find_element(By.NAME, "\"" + name + "\"").send_keys(key)

def checkDifference(browser):
    global count

    new_count = len(browser.find_elements_by_xpath("//div[@role='dialog']//li"))

    if count != new_count:
        count = new_count
        return True
    else:
        return False

def scroll(browser):
    global count

    while 1:
        browser.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTop=1e100")
        try:
            WebDriverWait(browser, 5).until(checkDifference)
        except:
            break

def getUserList(browser):
    listPATH = "//div[@role='dialog']//li"
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, listPATH)))
    scroll(browser)
    listElements = browser.find_elements(By.XPATH, listPATH)
    
    users = []
    for i in range(len(listElements)):
        try:
            txt = listElements[i].text
            if "Follow" in txt:
                username = txt[:txt.index("\n")]
                users.append(username)
        except Exception as e:
            print(e) 
    return users


def login(browser):
    try:            
        browser.implicitly_wait(30)
        browser.find_element(By.NAME, "username").send_keys(username)
        browser.find_element(By.NAME, "password").send_keys(password)
        browser.find_element(By.NAME, "password").send_keys(u'\ue007')
    except Exception as e:
        print(e) 

def navigation(browser, actions):
    browser.implicitly_wait(30)
    button = browser.find_element(By.XPATH, ("//button[contains(text(),'Not Now')]"))
    actions.move_to_element(button).click().perform()
    browser.implicitly_wait(30)
    button = browser.find_element(By.XPATH, ("//button[contains(text(),'Not Now')]"))
    actions.move_to_element(button).click().perform()
    browser.find_element(By.LINK_TEXT, username).click()

def followers(browser):
    browser.implicitly_wait(30)
    followersCSS = "[href*=\"" + username + "/followers/\"]"
    clickCSSButton(browser, followersCSS)
    browser.implicitly_wait(30)
    followerList = getUserList(browser)
    print(followerList)
    closeCSS = '[aria-label="Close"]'
    clickCSSButton(browser, closeCSS)

def following(browser):
    browser.implicitly_wait(30)
    followingCSS = "[href*=\"" + username + "/following/\"]"
    clickCSSButton(browser, followingCSS)


def __main__():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.instagram.com/accounts/login/')
    actions = ActionChains(browser)
    login(browser)
    navigation(browser, actions)
    followers(browser)
    sleep(1000000)
    browser.close()
    return

__main__()

# 'python3 instagramUnfollower.py' to run
