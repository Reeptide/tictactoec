from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-infobars")
import time
driver_path = 'chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service= service , options=chrome_options)
username = 'narendharsalt'
password = 'gayathri143'

def instagram_login(username , password):
    driver.get("https://www.instagram.com")
    #time.sleep(2)
    username_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    submit_xpath = '//*[@id="loginForm"]/div/div[3]/button'
    notnow_xpath = "//div[contains(text(), 'Not now')]"
    notif_xpath = '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
    username_inp = driver.find_element(By.XPATH , username_xpath)
    username_inp.send_keys(username)
    password_inp = driver.find_element(By.XPATH , password_xpath)
    password_inp.send_keys(password)
    button = driver.find_element(By.XPATH , submit_xpath)
    button.click()
  
    WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, notnow_xpath))
    )
    not_now = driver.find_element(By.XPATH, notnow_xpath)
    not_now.click()
    WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, notif_xpath))
    )
    notif = driver.find_element(By.XPATH, notif_xpath)
    notif.click()
    reelbtn_xpath = "//a[contains(@href, '/reels/')]"
    WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.XPATH , reelbtn_xpath))
    )
    reelbtn = driver.find_element(By.XPATH , reelbtn_xpath)
    reelbtn.click()
    return driver
    

instagram_login(username , password)
  
def fetchUserReels(driver , target):

    reelbtn_xpath = "//a[contains(@href, '/reels/')]"
    
    WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.XPATH , reelbtn_xpath))
    )
    reelbtn = driver.find_element(By.XPATH , reelbtn_xpath)

    reelbtn.click()
    time.sleep(10)
    action  = ActionChains(driver)
    while True:
        time.sleep(3)
        
        time.sleep(3)
        action.send_keys(Keys.ARROW_DOWN).perform()

        time.sleep(1)
        
    
fetchUserReels(driver)