from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException #исключения прописываем, чтобы можно было вылавливать..

def test_site_visit():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/')

    try:
        driver.find_element(By.CSS_SELECTOR, 'header > a > img')
                                        #Locator - адрес элемента на странице сайта
    except NoSuchElementException:
        assert False
    assert True