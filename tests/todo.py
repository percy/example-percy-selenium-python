from selenium import webdriver
from percy import percySnapshot
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(options=chrome_options)

browser.get('http://localhost:8000')
browser.implicitly_wait(10)

newTodoInput = browser.find_element_by_class_name('new-todo')
percySnapshot(browser=browser, name='Empty Todo State')

newTodoInput.send_keys('Try Percy')
newTodoInput.send_keys(Keys.ENTER)
percySnapshot(browser=browser, name='With a Todo')

todoToggle = browser.find_element_by_class_name('toggle')
todoToggle.click()
percySnapshot(browser=browser, name='Completed Todo')

browser.quit()
