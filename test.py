from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.reed.co.uk/courses/online?page=1")

browser.maximize_window()
title = browser.title

print(title)

