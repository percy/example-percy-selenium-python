from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.keys import Keys
from percy import percy_snapshot

# start the example app in another thread
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
thread = Thread(target=httpd.serve_forever)
thread.setDaemon(True)
thread.start()

# launch firefox headless
ff_options = FirefoxOptions()
ff_options.add_argument('-headless')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = Firefox(options=ff_options)

# go to the example app
browser.get('http://localhost:8000')
browser.implicitly_wait(10)
# perform actions: add a todo and mark it completed
new_todo_input = browser.find_element(By.CLASS_NAME, 'new-todo')
new_todo_input.send_keys('Try Percy')
new_todo_input.send_keys(Keys.ENTER)
todo_toggle = browser.find_element(By.CLASS_NAME, 'toggle')
todo_toggle.click()

# single Percy snapshot for the final state
percy_snapshot(browser, 'Final Todo State')

# clean up
browser.quit()
httpd.shutdown()
