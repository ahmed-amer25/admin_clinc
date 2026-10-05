import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContractsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    # Locators المطابقة تماماً للواجهة باللغة الإنجليزية
    _CLINIC_TAB = (By.XPATH, "//*[contains(text(), 'Clinic Performance')]")
    _VENDOR_TAB = (By.XPATH, "//*[contains(text(), 'Vendor Performance')]")
    _SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Search') or @type='text']")
    _VIEW_DETAILS_BTN = (By.XPATH, "//a[contains(@href, '/admin/contracts/')]")
    _BACK_TO_CONTRACTS_BTN = (By.XPATH, "//a[contains(@href, '/admin/contracts')]")

    def open_contracts_page(self, url="https://commacare-medical.quarizm.online/admin/contracts"):
        self.driver.get(url)
        time.sleep(5)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo({top: 400, behavior: 'instant'});")
        time.sleep(1)

    def select_clinic_contracts_tab(self):
        """الضغط على تابة Clinic Performance"""
        try:
            tab = self.wait.until(EC.element_to_be_clickable(self._CLINIC_TAB))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            self.driver.execute_script("arguments[0].click();", tab)
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ تعذر الضغط على Clinic Performance: {e}")

    def select_vendor_contracts_tab(self):
        """الضغط على تابة Vendor Performance"""
        try:
            tab = self.wait.until(EC.element_to_be_clickable(self._VENDOR_TAB))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            self.driver.execute_script("arguments[0].click();", tab)
            time.sleep(1) # إعطاء مهلة لتحميل جدول الموردين
        except Exception as e:
            print(f"⚠️ تعذر الضغط على Vendor Performance: {e}")

    def search_by_name(self, query_text):
        """تفريغ الحقل والسيرش مع إطلاق أحداث Vue"""
        try:
            inputs = self.driver.find_elements(*self._SEARCH_INPUT)
            # استهداف حقل البحث الخاص بالجدول (الحقل الثاني في الشاشة)
            search_box = inputs[-1] if inputs else None
            if search_box:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_box)
                search_box.click()
                
                search_box.send_keys(Keys.CONTROL + "a")
                search_box.send_keys(Keys.BACKSPACE)
                self.driver.execute_script("arguments[0].value = '';", search_box)
                
                search_box.send_keys(query_text)
                
                self.driver.execute_script("""
                    var el = arguments[0];
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                """, search_box)
                time.sleep(1.5)
        except Exception as e:
            print(f"⚠️ تعذر إجراء السيرش لـ {query_text}: {e}")

    def open_first_contract_profile(self):
        try:
            btn = self.wait.until(EC.presence_of_element_located(self._VIEW_DETAILS_BTN))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(1.5)
        except Exception as e:
            print(f"⚠️ تعذر فتح البروفايل: {e}")

    def click_back_to_contracts(self):
        try:
            back_btn = self.wait.until(EC.presence_of_element_located(self._BACK_TO_CONTRACTS_BTN))
            self.driver.execute_script("arguments[0].click();", back_btn)
        except Exception:
            self.driver.back()
        time.sleep(1)