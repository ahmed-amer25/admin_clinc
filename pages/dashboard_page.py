import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    _NAV_SIDEBAR = (By.CSS_SELECTOR, ".layout-sidebar")
    _OVERVIEW_TAB = (By.CSS_SELECTOR, ".layout-sidebar a[href='/']")

    def is_sidebar_visible(self) -> bool:
        element = self.wait.until(EC.visibility_of_element_located(self._NAV_SIDEBAR))
        return element.is_displayed()

    def is_overview_active(self) -> bool:
        element = self.wait.until(EC.visibility_of_element_located(self._OVERVIEW_TAB))
        return "router-link-active" in element.get_attribute("class")

    def scroll_down_and_up(self, pause_time=2):
        # السكرول لأسفل
        self.driver.execute_script("""
            window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});
            let scrollableDiv = document.querySelector('main, .layout-wrapper, #__nuxt');
            if (scrollableDiv) {
                scrollableDiv.scrollTo({top: scrollableDiv.scrollHeight, behavior: 'smooth'});
            }
        """)
        time.sleep(pause_time)
        
        # السكرول لأعلى
        self.driver.execute_script("""
            window.scrollTo({top: 0, behavior: 'smooth'});
            let scrollableDiv = document.querySelector('main, .layout-wrapper, #__nuxt');
            if (scrollableDiv) {
                scrollableDiv.scrollTo({top: 0, behavior: 'smooth'});
            }
        """)
        time.sleep(pause_time)

    def get_current_url(self) -> str:
        return self.driver.current_url