import time
from datetime import datetime
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
                price = cols_data[3].replace("R$", "").replace("\xa0", "").replace(",", ".").strip()
                date_string = cols_data[2]
                dt = datetime.strptime(date_string, "%d/%m/%Y %H:%M")  # assuming the format is DD/MM/YYYY HH:MM
                print(f"Produto: {cols_data[0]}")
                print(f"Preço: {price}")
                print(f"Data e Hora do Preço: {dt.strftime('%Y-%m-%d %H:%M')}")
                print(f"Unid. Padrão: {cols_data[4]}")
                driver.quit()
                break
else:
    print("Table not found.")

driver.quit()