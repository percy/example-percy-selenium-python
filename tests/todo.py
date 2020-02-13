from selenium import webdriver
from percy import percySnapshot
from multiprocessing import Process
from selenium.webdriver.common.keys import Keys
from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
def start_server():
    httpd.serve_forever()

server = Process(target=start_server)
server.start()

browser = webdriver.Firefox()

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
server.terminate()
