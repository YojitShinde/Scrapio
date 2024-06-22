from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def scrape():
    website = 'https://checkvisaslots.com/latest-us-visa-availability.html'

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(website)

    driver.implicitly_wait(10)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.visa_type')))

    table = driver.find_element(By.XPATH,'//*[@id="table_H_1B_Regular_"]/tbody')
    print(table.text)

    # For beautifying the table format.

    # data = []
    # row = []

    # for tr in table.find_elements(By.XPATH,'//tr'):
    #     for td in tr.find_elements(By.XPATH,'//td'):
    #         row.append(td.text)
    #     data.append(row)
    #     break

    # print(data)

    with open('H1-B Slots.txt', 'w') as file:
        file.write('Location | Earliest Date | Total Dates | Last Seen At | Relative Time\n')
        file.write(table.text)

    time.sleep(10)

    driver.quit()