import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard_elements_and_scroll(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    
    # 1. تسجيل الدخول
    login_page.open()
    login_page.enter_email("admin@admin.com")
    login_page.enter_password("password")
    login_page.click_submit()
    
    # 2. التأكد من فتح الصفحة والـ Navigation
    assert dashboard_page.is_sidebar_visible()
    assert dashboard_page.is_overview_active()
    
    # 3. تنفيذ أمر السكرول لأسفل ثم لأعلى
    dashboard_page.scroll_down_and_up(pause_time=2)