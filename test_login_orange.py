import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup():
    global driver
    service_obj = Service('C:/chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()


@pytest.mark.smoke
def test_navigate(test_setup):
    # Navigate to url
    driver.get("https://opensource-demo.orangehrmlive.com/")
    assert "login" in driver.current_url


@pytest.mark.smoke
def test_validateLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, 'username').send_keys("Admin")
    driver.find_element(By.NAME, 'password').send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    assert "dashboard" in driver.current_url


def test_invalidLogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, 'username').send_keys("Admin")
    driver.find_element(By.NAME, 'password').send_keys("aPratdmin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    message = driver.find_element(By.CLASS_NAME, 'oxd-text--p').text
    print(message)
    assert "Invalid" in message
    #assert ("message", 'Invalid Credentials') in driver.current_url


