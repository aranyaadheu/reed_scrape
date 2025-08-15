from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

def extract_data(page_no):
    url = f"https://www.reed.co.uk/courses/online?page={page_no}"
    driver.get(url)
    time.sleep(2) 

    titles = driver.find_elements(By.CSS_SELECTOR, "div.top-col > h2 > a") #selects pages all 25 titles. 
    providers = driver.find_elements(By.CSS_SELECTOR, "div.top-col > div.provider-name") # all 25 providers name of a single page at once. 
    students = driver.find_elements(By.CSS_SELECTOR, "div:nth-child(3) > div.bottom-col > ul > li:nth-child(1) > span")

    for i in range(len(titles)):
        f = {
            "Title": titles[i].text.strip(),
            "Provider": providers[i].text.strip() if i < len(providers) else "",
            "URL": titles[i].get_attribute("href"),
            "Students": students[i].text.strip() if i < len(students) else "",
        }
        
        lst.append(f)
    return lst

lst = []

for i in range(1, 11):
    extract_data(i)


df = pd.DataFrame(lst)
df.to_csv("all_courses_info.csv")

driver.quit()

print("Saved to all_courses_info.csv")
