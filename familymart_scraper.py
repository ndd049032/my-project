from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import csv
import logging
import time
import random

# 設置日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def wait_and_get_element(driver, by, value, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        logging.warning(f"元素未在 {timeout} 秒內加載: {value}")
        return None

def get_product_info(driver, url):
    product = {}
    try:
        driver.get(url)
        logging.info("正在加載頁面...")
        time.sleep(random.uniform(2, 5))  # 隨機延遲 2 到 5 秒

        # 提取產品名稱
        name_element = wait_and_get_element(driver, By.CSS_SELECTOR, 'h1')
        if name_element:
            product['name'] = name_element.text.strip()
            logging.info(f"找到產品名稱: {product['name']}")

        # 提取產品詳情
        detail_element = wait_and_get_element(driver, By.CLASS_NAME, 'product__detail')
        if detail_element:
            product['detail'] = detail_element.text.strip()
            logging.info("找到產品詳情")

        # 提取成分來源
        ingredients_element = wait_and_get_element(driver, By.CSS_SELECTOR, '.ingredients')  # 這裡根據實際情況調整
        if ingredients_element:
            product['ingredients'] = ingredients_element.text.strip()
            logging.info("找到成分來源")

        # 提取營養信息
        nutrition_info = driver.find_elements(By.CSS_SELECTOR, '.resume__info p')
        if nutrition_info:
            for info in nutrition_info:
                parts = info.text.split()
                if len(parts) >= 2:
                    key = parts[0]
                    value = ' '.join(parts[1:])
                    product[key] = value.strip()
            logging.info("找到營養信息")

        # 提取過敏原
        allergens = driver.find_elements(By.CSS_SELECTOR, '.tag-list li span')
        if allergens:
            product['allergens'] = [allergen.text for allergen in allergens]
            logging.info(f"找到過敏原: {len(product['allergens'])}項")

        # 提取標章
        certifications = driver.find_elements(By.CSS_SELECTOR, '.tag-list li span')
        if certifications:
            product['certifications'] = [cert.text for cert in certifications]
            logging.info(f"找到標章: {len(product['certifications'])}項")

        # 提取供應商信息
        supplier_info = driver.find_elements(By.CSS_SELECTOR, '.resume__desc dt, .resume__desc dd')
        if supplier_info:
            for i in range(0, len(supplier_info), 2):
                key = supplier_info[i].text
                value = supplier_info[i + 1].text
                product[f'supplier_{key}'] = value
            logging.info("找到供應商信息")
        
    except TimeoutException:
        logging.error("頁面加載超時")
    except NoSuchElementException as e:
        logging.error(f"未找到元素: {e}")
    except Exception as e:
        logging.error(f"發生錯誤: {e}")
    
    return product

def save_to_csv(product, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for key, value in product.items():
            if isinstance(value, list):
                writer.writerow([key, ', '.join(value)])
            else:
                writer.writerow([key, value])

def main():
    url = "https://foodsafety.family.com.tw/Web_FFD_2022/product/0058818"
    driver = setup_driver()
    try:
        product = get_product_info(driver, url)
        if product:
            save_to_csv(product, '產品信息.csv')
            logging.info(f"成功爬取產品信息，已保存到 產品信息.csv")
        else:
            logging.error("未能爬取到產品信息")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
