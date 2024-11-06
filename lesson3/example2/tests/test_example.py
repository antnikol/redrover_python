from selene import browser, have


def test_visible_after_with_explicit_waits_with_selene():
    browser.open('https://demoqa.com/dynamic-properties')
    browser.element('//button[text()="Visible After 5 Seconds"]'). \
        should(have.exact_text('Visible After 5 Seconds'))

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