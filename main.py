from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
browser = webdriver.Chrome(service=Service(executable_path=r'C:\Users\abhay\PycharmProjects\chromedriver.exe'),
                           options=options)
browser.maximize_window()
print(browser.command_executor._url)
print(browser.session_id)
