import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage

def test_admin_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    
    # تسجيل دخول ناجح
    login_page.enter_email("admin@admin.com")
    login_page.enter_password("password")
    login_page.click_submit()
    
    WebDriverWait(driver, 10).until(lambda d: "admin-login" not in d.current_url)
    assert "admin-login" not in driver.current_url

def test_admin_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    
    # تجربة كلمة مرور خاطئة
    login_page.enter_email("admin@admin.com")
    login_page.enter_password("wrong_password_123")
    login_page.click_submit()
    
    # التأكد من بقاء المستخدم في نفس الصفحة وعدم الدخول
    assert "admin-login" in driver.current_url