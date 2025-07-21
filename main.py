from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver,10)

#open Louis Vuitton main page
driver.get('https://us.louisvuitton.com/eng-us/homepage')


#close cookie window
cookie = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ucm-openButton.ucm-choice__yes")))
cookie.click()

#click menu tab
menu_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.lv-header-icon-burger__bars')))
menu_tab.click()

#click the Women tab
man_tab = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Men']")))
man_tab.click()


driver.find_element(By.ID, "m-category-cat10037-button").click()
sleep(1)
driver.find_element(By.XPATH, "//a[@href='/eng-us/men/shoes/all-shoes/_/N-t118ht95']").click()
sleep(3)

#click Accessories
Accessories = wait.until(EC.element_to_be_clickable((By.ID,'w-category-cat10155-button')))
Accessories.click()

#click Scarves
Scarves = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[href*='accessories/scarves']")))
Scarves.click()
















# email = driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']")
# email.send_keys('american.luca@gmail.com')
# # email.send_keys(Keys.ENTER)
# sleep(2)
#
# password = driver.find_element(By.XPATH, "//input[@aria-label='Password']")
# password.send_keys('<PASSWORD>')
# # password.send_keys(Keys.ENTER)
# sleep(2)
