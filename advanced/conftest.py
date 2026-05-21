"""PER-8195 — pytest fixtures: HTTP server for the TodoMVC app, headless
firefox driver. Server roots two directories up so the basic TodoMVC files
served at /index.html land at http://localhost:8006/."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import functools
import os
import pytest
from selenium.webdriver import Firefox, FirefoxOptions

PORT = int(os.environ.get("PORT_NUMBER", "8006"))
TEST_URL = f"http://localhost:{PORT}"
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


@pytest.fixture(scope="session")
def http_server():
    handler = functools.partial(SimpleHTTPRequestHandler, directory=APP_ROOT)
    httpd = HTTPServer(("localhost", PORT), handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield httpd
    httpd.shutdown()


@pytest.fixture(scope="session")
def driver(http_server):
    options = FirefoxOptions()
    options.add_argument("-headless")
    if os.environ.get("FIREFOX_BINARY"):
        options.binary_location = os.environ["FIREFOX_BINARY"]
    browser = Firefox(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
