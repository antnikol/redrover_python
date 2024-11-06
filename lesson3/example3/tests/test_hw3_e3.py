import pytest
from playwright.sync_api import Page, expect

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