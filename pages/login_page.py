import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    _EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'], input[name='email']")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password'], input[name='password']")
    _SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, url="https://commacare-medical.quarizm.online/auth/admin-login"):
        self.driver.get(url)

    def enter_email(self, email):
        field = self.wait.until(EC.visibility_of_element_located(self._EMAIL_INPUT))
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_submit(self):
        btn = self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BTN))
        btn.click()
        # انتظار حتى يتم تحويل الصفحة وتأكيد الجلسة
        time.sleep(5)