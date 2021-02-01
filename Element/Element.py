__author__ = 'sunny.yu'

from selenium.common.exceptions import WebDriverException, NoSuchElementException
from Element.Waitor import Waitor
from Element.Find import Find
from Utilitys.Logging import general_log_decorator
from Utilitys.WaitUtils import WaitUtils


class Element(Find):

    def __init__(self, driver):
        Find.__init__(self)
        self.driver = driver
        self.interval = 0.5
        self.timeout = 20

    def wait_for(self):
        return Waitor(self, self.interval, self.timeout)

    def get_interval(self):
        return self.interval

    def get_timeout(self):
        return self.timeout

    def set_interval(self, interval):
        self.interval = interval

    def set_timeout(self, timeout):
        self.timeout = timeout

    @general_log_decorator
    def find_element_click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
        except Exception as handleRetry:
            WaitUtils.wait_for_element_clickable(self.driver, by, value)
            self.driver.find_element(by, value).click()

    @general_log_decorator
    def find_element_send_keys(self, by, value, keys):
        try:
            self.driver.find_element(by, value).send_keys(keys)
        except Exception as handleRetry:
            WaitUtils.wait_for_element_visible(self.driver, by, value)
            self.driver.find_element(by, value).send_keys(keys)

    @general_log_decorator
    def find_element_set_value(self, by, value, keys):
        try:
            self.driver.find_element(by, value).set_value(keys)
        except Exception as handleRetry:
            WaitUtils.wait_for_element_visible(self.driver, by, value)
            self.driver.find_element(by, value).set_value(keys)

    @general_log_decorator
    def drag_and_drop(self, origin_el, destination_el):
        pass

    @general_log_decorator
    def make_sure_element_exist(self, by, value, interval=5, timeout=20):
        try:
            self.driver._appium_context().find_element(by, value)
            return True
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_present(self.driver._appium_context(), by, value, interval=interval,
                                                   timeout=timeout)
                return True
            except Exception:
                return False

    @general_log_decorator
    def check_element_visible(self, by, value):
        try:
            return self.driver._appium_context().find_element(by, value).is_displayed()
        except Exception as handleRetry:
            try:
                self._refresh()
                return self.driver._appium_context().find_element(by, value).is_displayed()
            except Exception as e:
                return False

    @general_log_decorator
    def clear_element_value(self, by, value):
        try:
            self.driver.find_element(by, value).clear()
        except Exception as handleRetry:
            WaitUtils.wait_for_element_present(self.driver, by, value)
            self.driver.find_element(by, value).clear()

    @general_log_decorator
    def get_element_text(self, by, value):
        try:
            return self.driver.find_element(by, value).text
        except Exception as handleRetry:
            WaitUtils.wait_for_element_visible(self.driver, by, value)
            return self.driver.find_element(by, value).text

    @general_log_decorator
    def get_elements_text(self, by, value):
        list_text = []
        elements = self.driver.find_elements(by, value)
        for i in elements:
            list_text.append(i.text)
        return list_text

    @general_log_decorator
    def find_element_location_in_view(self, by, value):
        try:
            self.driver.find_element(by, value).location_in_view
        except Exception as handleRetry:
            self._refresh()
            self.driver.find_element(by, value).location_in_view

    @general_log_decorator
    def android_scroll(self, up=0.5, down=None, scroll_time=1):
        screen = self.driver.get_window_size()
        start_x = screen['width']
        start_y = screen['height']

        for i in range(0, scroll_time):
            if down:
                up = down
            self.driver.swipe(start_x, start_y * up, start_x, start_y)

    @general_log_decorator
    def android_scroll_to_specific_text(self, text):
        self.driver._Driver__app_driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollTextIntoView("'
            + text + '")')

    @general_log_decorator
    def android_scroll_to_element(self, element_from, element_to):
        self.driver.scroll(element_from, element_to)

    @general_log_decorator
    def android_swipe_element_to_specific_location(self, element, rate=0.5):
        screen = self.driver.get_window_size()
        screen_height = screen['height']
        element_x = element.location['x']
        element_y = element.location['y']
        end_y = screen_height * rate
        self.driver.swipe(element_x, element_y, element_x, end_y)

    @general_log_decorator
    def element_show(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except Exception as e:
            return False

    @general_log_decorator
    def wait_element_text_visible(self, by, value, text):
        try:
            WaitUtils.wait_for_element_text_visible(self.driver, by, value, text)
            return True
        except Exception as e:
            return False

    @general_log_decorator
    def find_element_get_attribute(self, by, value, attr):
        try:
            return self.driver.find_element(by, value).get_attribute(attr)
        except Exception as handleRetry:
            return self.driver.find_element(by, value).get_attribute(attr)

    @general_log_decorator
    def scroll_by_direction(self, direction):
        self.driver.execute_script('mobile: scroll', {'direction': direction})

    # name is the accessibility id of the element
    @general_log_decorator
    def scroll_by_name(self, name):
        self.driver.execute_script('mobile: scroll', {'name': name})

    @general_log_decorator
    def swipe(self, direction):
        self.driver.execute_script('mobile: swipe', {'direction': direction})

    @general_log_decorator
    def android_scroll_by_direction(self, direction, percent=1.0):
        self.driver.execute_script('mobile: scrollGesture', {'direction': direction, 'percent': percent})

    @general_log_decorator
    def android_swipe_by_direction(self, direction, percent=1.0):
        self.driver.execute_script('mobile: swipeGesture', {'direction': direction,  'percent': percent})

    @general_log_decorator
    def find_elements_click(self, by, value, index):
        elements = self.driver.find_elements(by, value)
        elements[index].click()

    @general_log_decorator
    def find_elements_count(self, by, value):
        elements = self.driver.find_elements(by, value)
        return len(elements)

    @general_log_decorator
    def get_element_location(self, by, value):
        try:
            return self.driver.find_element(by, value).location
        except Exception as handleRetry:
            WaitUtils.wait_for_element_visible(self.driver, by, value)
            return self.driver.find_element(by, value).location

    @general_log_decorator
    def check_element_enabled(self, by, value):
        try:
            return self.driver.find_element(by, value).is_enabled()
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                return self.driver.find_element(by, value).is_enabled()
            except Exception as e:
                return False

    # TODO: We need to wrap more method here.
