import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

initial_url = "https://coamo.com.br/preco-do-dia"
City = "ABELARDO LUZ"

driver = webdriver.Chrome()
driver.get(initial_url)

time.sleep(2)

dropdown = Select(driver.find_element(By.XPATH, '//select[@data-v-063c5833]'))

dropdown.select_by_visible_text(City)

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

table_element = soup.find("table", {"data-v-063c5833": ""})

if table_element:
    rows = table_element.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 5:
            cols_data = [col.text.strip() for col in cols]
            if cols_data[0].strip() == "SOJA":
                price = cols_data[3].replace("R$", "").replace("\xa0", "").strip()
                print(f"Produto: {cols_data[0]}")
                print(f"Preço: R${price}")
                print(f"Data e Hora do Preço: {cols_data[2]}")
                driver.quit()
                break
else:
    print("Table not found.")

driver.quit()