import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClinicsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    _HOLD_BTN = (By.XPATH, "//button[contains(., 'Hold') or contains(., 'تعليق')]")
    _CANCEL_MODAL_BTN = (By.XPATH, "//button[contains(., 'إلغاء') or contains(., 'Cancel')]")
    _UNHOLD_BTN = (By.XPATH, "//button[contains(., 'Activate') or contains(., 'تفعيل') or contains(., 'Unhold')]")
    _PROFILE_TABS = (By.XPATH, "//button[contains(@role, 'tab')] | //div[contains(@class, 'tab')]//button")
    _BACK_TO_CLINICS_BTN = (By.XPATH, "//a[contains(@href, '/admin/clinics') or contains(., 'العيادات')] | //button[contains(., 'العيادات')]")

    def open_specific_clinic(self, clinic_url):
        self.driver.get(clinic_url)
        time.sleep(1.5)

    def scroll_down_and_up(self):
        """النزول لأسفل الصفحة ثم العودة للقمة"""
        self.driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'instant'});")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo({top: 0, behavior: 'instant'});")
        time.sleep(0.5)

    def click_hold_button(self):
        """الضغط على زر تعليق العيادة ثم الضغط على إلغاء في الرسالة التأكيدية"""
        try:
            # 1. الضغط على زر Hold/تعليق
            btn = self.wait.until(EC.element_to_be_clickable(self._HOLD_BTN))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)

            # 2. الضغط على زر إلغاء في Modal المؤكد
            cancel_btn = self.wait.until(EC.element_to_be_clickable(self._CANCEL_MODAL_BTN))
            self.driver.execute_script("arguments[0].click();", cancel_btn)
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ تعذر الضغط على زر Hold أو Cancel: {e}")

    def click_unhold_button(self):
        """الضغط على زر إعادة التفعيل Unhold / Activate"""
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self._UNHOLD_BTN))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ تعذر الضغط على زر Unhold: {e}")

    def click_all_profile_tabs(self):
        """التنقل بين جميع تابات بروفايل العيادة"""
        try:
            tabs = self.driver.find_elements(*self._PROFILE_TABS)
            for tab in tabs:
                if tab.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
                    self.driver.execute_script("arguments[0].click();", tab)
                    time.sleep(0.8)
        except Exception as e:
            print(f"⚠️ تنبيه أثناء التنقل بين التابات: {e}")

    def click_back_to_clinics(self):
        """الرجوع إلى قائمة العيادات الرئيسية"""
        try:
            back_btn = self.wait.until(EC.element_to_be_clickable(self._BACK_TO_CLINICS_BTN))
            self.driver.execute_script("arguments[0].click();", back_btn)
            time.sleep(1.5)
        except Exception as e:
            print(f"⚠️ تعذر الرجوع لصفحة العيادات: {e}")