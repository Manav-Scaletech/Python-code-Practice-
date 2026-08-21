import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PAGE_URL = "https://scaletech.xyz"
API_URL = "https://admin.scaletech.xyz/api/testimonials?populate=*"

chrome_options = Options()
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(options=chrome_options)

try:

    driver.get(PAGE_URL)
   
    time.sleep(2)
    html_source = driver.page_source

    soup = BeautifulSoup(html_source, "html.parser")
    with open("website_selenium.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
  

    driver.get(API_URL)

    json_text = driver.find_element("xpath", "//body").text

 
    api_data = json.loads(json_text)

    with open("data_selenium.json", "w", encoding="utf-8") as json_file:
        json.dump(api_data, json_file, indent=4)
    print("saved")

finally:
 
    driver.quit()
    print("open")
