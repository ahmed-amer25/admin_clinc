# في ملف conftest.py
import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # تسجيل الدخول الموحد للجلسة
    login_page = LoginPage(driver)
    login_page.open("https://commacare-medical.quarizm.online/auth/admin-login")
    login_page.enter_email("admin@admin.com")
    login_page.enter_password("password")
    login_page.click_submit()
    time.sleep(5) # الانتظار في الداش بورد
    
    yield driver
    driver.quit()