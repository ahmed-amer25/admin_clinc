import time
import pytest
from pages.clinics_page import ClinicsPage

def test_clinic_profile_actions_and_navigation(driver):
    clinics_page = ClinicsPage(driver)

    # 1. الانتقال المباشر لصفحة العيادة
    target_clinic_url = "https://commacare-medical.quarizm.online/admin/clinics/472"
    clinics_page.open_specific_clinic(target_clinic_url)
    assert "clinics/472" in driver.current_url

    # 2. باقي الأكشنز
    clinics_page.click_hold_button()
    clinics_page.scroll_down_and_up()
    clinics_page.click_all_profile_tabs()
    clinics_page.click_back_to_clinics()