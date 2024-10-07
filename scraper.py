import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

endpoints = {
    'name': 'Product__UpdatedTitle-sc-11dk8zk-9 hxWnoO',
    'quantity': 'bff_variant_text_only plp-product__quantity--box',
    'discount': 'Product__UpdatedOfferTitle-sc-11dk8zk-2 eajROp',
    'discounted_value': 'color: rgb(31, 31, 31); font-weight: 600; font-size: 12px;',
    'actual_value': 'color: rgb(130, 130, 130); font-weight: 400; font-size: 12px; text-decoration-line: line-through;',
    'out': 'AddToCart__UpdatedOutOfStockTag-sc-17ig0e3-4 bxVUKb'
}

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_argument("--window-size=1920,1080")  
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

chrome_path = "/usr/bin/chromium-browser"
chrome_options.binary_location = chrome_path


driver = webdriver.Chrome(service=Service(), options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)


# driver = webdriver.Chrome()

driver.get("https://blinkit.com/s/?q=electronics")

scroll_pause_time = 3
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

products = soup.find_all('a', attrs={'data-test-id': 'plp-product'})

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Quantity', 'Discount', 'Discounted Value', 'Actual Value', 'Product URL', 'Out of Stock'])

    for product in products:
        name = product.find('div', attrs={'class': endpoints['name']})
        print(name.get_text(strip=True))
        
        quantity = product.find('span', attrs={'class': endpoints['quantity']})
        discount = product.find('div', attrs={'class': endpoints['discount']})
        discount_value = product.find('div', style=endpoints['discounted_value'])
        actual_value = product.find('div', style=endpoints['actual_value'])
        out_of_stock = product.find('div', attrs={'class': endpoints['out']})
        url = 'https://blinkit.com' + product['href']

        writer.writerow([
            name.get_text(strip=True) if name else 'None',
            quantity.get_text(strip=True) if quantity else 'None',
            discount.get_text(strip=True) if discount else 'None',
            discount_value.get_text(strip=True) if discount_value else 'None',
            actual_value.get_text(strip=True) if actual_value else 'None',
            url,
            'True' if out_of_stock else 'False'
        ])

driver.quit()
