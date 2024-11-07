import requests
from selene import browser, have, be
from selene.core.query import attribute


def test_check_site_registration():
    browser.open('https://victoretc.github.io/selenium_waits/')
    browser.element('h1').should(have.exact_text('Практика с ожиданиями в Selenium'))
    browser.element("//button[@id='startTest']").click()
    browser.element("//input[@type='text']").type('login')
    browser.element("input[type='password']").type('password')
    browser.element("input[type='checkbox']").click()
    browser.element("//button[@id='register']").click()
    browser.element("//div[@id='loader']").should(have.attribute('class').value(''))
    browser.element("//p[@id='successMessage']").should(have.text('Вы успешно зарегистрированы!'))

def test_add_elements():
    browser.open('https://the-internet.herokuapp.com/add_remove_elements/')
    browser.element("//button[@onclick='addElement()']").click()
    browser.element("//button[@onclick='addElement()']").click()
    browser.element("//button[@onclick='addElement()']").click()
    browser.element("//button[@class='added-manually']").should(be.visible)
    browser.element("//button[@class='added-manually']").click()
    browser.all("//button[@class='added-manually']").should(have.size(2))
    browser.element("//button[@class='added-manually']").click()
    browser.element("//button[@class='added-manually']").click()
    browser.all("//button[@class='added-manually']").should(have.size(0))

def test_basic_auth():
    browser.open('https://admin:admin@the-internet.herokuapp.com/basic_auth')
    browser.element("//h3").should(have.text('Basic Auth'))

def test_broken_images():
    browser.open('https://the-internet.herokuapp.com/broken_images')
    images = browser.all('img')
    images.should(have.size(4))
    broken_images = [img for img in images if (requests.head(img.get(attribute('src'))).status_code != 200)]
    assert len(broken_images) == 0, f"Broken images found: {[img.get(attribute('src')) for img in broken_images]}"

def test_checkbox_clicking():
    browser.open('https://the-internet.herokuapp.com/checkboxes')
    checkboxes = browser.all("//input[@type='checkbox']")
    checkboxes[0].click()
    checkboxes[1].click()
    checkboxes[0].should(be.selected)
    checkboxes[1].should(have._not_.css_class('checked'))