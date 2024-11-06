import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_check_site_registration(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.find_element('css selector', 'h1').text == 'Практика с ожиданиями в Selenium'
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='startTest']"))).click()
    driver.find_element('xpath', "//input[@type='text']").send_keys('login')
    driver.find_element('css selector', "input[type='password']").send_keys('password')
    driver.find_element('css selector', "input[type='checkbox']").click()
    driver.find_element('xpath', "//button[@id='register']").click()
    assert "" in driver.find_element('xpath', "//div[@id='loader']").get_attribute("class")
    assert wait.until(EC.text_to_be_present_in_element(('xpath', "//p[@id='successMessage']"), "Вы успешно зарегистрированы!"))

def test_check_site_registration_implicitly(driver):
    driver.implicitly_wait(10)
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.find_element('css selector', 'h1').text == 'Практика с ожиданиями в Selenium'
    driver.find_element(By.XPATH, "//button[@id='startTest']").click()
    driver.find_element('xpath', "//input[@type='text']").send_keys('login')
    driver.find_element('css selector', "input[type='password']").send_keys('password')
    driver.find_element('css selector', "input[type='checkbox']").click()
    driver.find_element('xpath', "//button[@id='register']").click()
    assert "" in driver.find_element('xpath', "//div[@id='loader']").get_attribute("class")
    for _ in range(5):
        if driver.find_element(By.XPATH, "//p[@id='successMessage']").text == "Вы успешно зарегистрированы!":
            break
        time.sleep(1)
    assert driver.find_element(By.XPATH, "//p[@id='successMessage']").text == "Вы успешно зарегистрированы!"


def test_check_site_registration_sleep(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    time.sleep(5)
    assert driver.find_element('css selector', 'h1').text == 'Практика с ожиданиями в Selenium'
    driver.find_element(By.XPATH, "//button[@id='startTest']").click()
    driver.find_element('xpath', "//input[@type='text']").send_keys('login')
    driver.find_element('css selector', "input[type='password']").send_keys('password')
    driver.find_element('css selector', "input[type='checkbox']").click()
    driver.find_element('xpath', "//button[@id='register']").click()
    assert "" in driver.find_element('xpath', "//div[@id='loader']").get_attribute("class")
    time.sleep(5)
    assert wait.until(EC.text_to_be_present_in_element(('xpath', "//p[@id='successMessage']"), "Вы успешно зарегистрированы!"))
