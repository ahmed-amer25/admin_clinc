import time
import pytest
from pages.contracts_page import ContractsPage

def test_contracts_flow(driver):
    contracts_page = ContractsPage(driver)

    # 1. فتح صفحة العقود والنزول لأسفل
    contracts_page.open_contracts_page()
    contracts_page.scroll_down()

    # 2. اختيار تابة عقود العيادات والبحث
    contracts_page.select_clinic_contracts_tab()
    contracts_page.search_by_name("شركة رونق التخصصي الطبي")

    # 3. اختيار تابة عقود الموردين والبحث
    contracts_page.select_vendor_contracts_tab()
    contracts_page.search_by_name("HealthCare Solutions5")