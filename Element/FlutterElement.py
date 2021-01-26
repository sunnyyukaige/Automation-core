from Element.FlutterFind import FlutterFind
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from Utilitys.WaitUtils import WaitUtils


class FlutterElement(FlutterFind):
    def __init__(self, driver):
        FlutterFind.__init__(self)
        self.driver = driver
        self.interval = 0.5
        self.timeout = 20

    def find_flutter_element_and_click(self, value):
        try:
            self.driver.find_flutter_element(value).click()
        except Exception as e:
            raise NoSuchElementException

    def flutter_scroll_to_text(self, value):
        try:
            WaitUtils.flutter_wait_for_element(self.driver, value)
            self.driver.execute_script(
                "flutter:scrollIntoView", value, 0.1)
        except Exception as handleRetry:
            try:
                WaitUtils.flutter_wait_for_element(self.driver, value)
                self.driver.execute_script(
                    "flutter:scrollIntoView", value, 0.1)
            except Exception as e:
                raise NoSuchElementException

    def find_flutter_element_sendkeys(self, locator, value):
        try:
            WaitUtils.flutter_wait_for_element(self.driver, value)
            self.driver.elementSendKeys(locator, value)
        except Exception as handleRetry:
            try:
                WaitUtils.flutter_wait_for_element(self.driver, value)
                self.driver.elementSendKeys(locator, value)
            except Exception as e:
                raise NoSuchElementException
