import time, requests, pytest
from http.client import responses

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

def test_add_elements(driver, wait):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    driver.find_element('xpath', "//button[@onclick='addElement()']").click()
    assert driver.find_element('xpath', "//button[@class='added-manually']").is_displayed()
    time.sleep(1)
    driver.find_element('xpath', "//button[@class='added-manually']").click()
    time.sleep(1)
    assert len(driver.find_elements('xpath', "//button[@class='added-manually']")) == 0

def test_basic_auth(driver, wait):
    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
    # prompt = driver.switch_to.alert
    # prompt.send_keys("admin:admin")
    # prompt.accept()
    message = driver.find_element('xpath', "//p").text.strip()
    assert message == "Congratulations! You must have the proper credentials."

@pytest.mark.xfail
def test_broken_images(driver, wait):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    images = driver.find_elements('xpath', '//img')
    broken_images = [img for img in images if (requests.head(img.get_attribute("src")).status_code != 200)]
    assert len(broken_images) == 0, f'Broken images found: {[img.get_attribute("src") for img in broken_images]}'


def test_checkbox_clicking(driver, wait):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    first = driver.find_elements('xpath', "//input[@type='checkbox']")[1]
    first.click()
    second = driver.find_elements('xpath', "//input[@type='checkbox']")[0]
    second.click()
    time.sleep(1)
    assert second.is_selected()
    assert not first.is_selected()
