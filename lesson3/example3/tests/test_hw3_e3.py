import pytest
import requests, pytest
from playwright.sync_api import Page, expect
from playwright.async_api import async_playwright

def test_check_site_registration(page: Page):
    page.goto('https://victoretc.github.io/selenium_waits/')
    expect(page.locator('h1')).to_have_text('Практика с ожиданиями в Selenium')
    page.locator("//button[@id='startTest']").click()
    page.locator("//input[@type='text']").type('login')
    page.locator("//input[@type='password']").type('password')
    page.locator("input[type='checkbox']").click()
    page.locator("//button[@id='register']").click()
    expect(page.locator("//div[@id='loader']")).to_have_css('class','')
    expect(page.locator("//p[@id='successMessage']")).to_have_text('Вы успешно зарегистрированы!')

def test_add_elements(page: Page):
    page.goto('https://the-internet.herokuapp.com/add_remove_elements/')
    page.locator("//button[@onclick='addElement()']").click()
    expect(page.locator("//button[@class='added-manually']")).to_be_visible()
    page.locator("//button[@class='added-manually']").click()
    expect(page.locator("//button[@class='added-manually']")).to_have_count(0)

def test_basic_auth(page: Page):
    page.goto('https://admin:admin@the-internet.herokuapp.com/basic_auth')
    expect(page.locator("//h3")).to_have_text('Basic Auth')

def test_broken_images(page: Page):
    page.goto('https://the-internet.herokuapp.com/broken_images')
    try:
        images = page.query_selector_all('//img')
        broken_images = [img for img in images if (requests.head('https://the-internet.herokuapp.com/' + img.get_attribute("src")).status_code != 200)]
        assert len(broken_images) == 0
    except AssertionError:
        print(f'Broken images found: {[img.get_attribute("src") for img in broken_images]}')
        pytest.xfail("Expected failure in test.")

def test_checkbox_clicking(page: Page):
    page.goto('https://the-internet.herokuapp.com/checkboxes')
    checkboxes = page.locator("//input[@type='checkbox']")
    checkboxes.nth(0).click()
    checkboxes.nth(1).click()
    expect(checkboxes.nth(0)).to_be_checked()
    expect(checkboxes.nth(1)).not_to_be_checked()



