__author__ = 'sunny.yu'

from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver import ActionChains
from Element.Waitor import Waitor
from Element.Find import Find
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

    def find_element_click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_clickable(self.driver, by, value)
                self.driver.find_element(by, value).click()
            except WebDriverException as e:
                raise e
            except Exception:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def find_element_sendkeys(self, by, value, keys):
        try:
            self.driver.find_element(by, value).send_keys(keys)
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                self.driver.find_element(by, value).send_keys(keys)
            except WebDriverException as e:
                raise e
            except Exception:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def find_element_set_value(self, by, value, keys):
        try:
            self.driver.find_element(by, value).set_value(keys)
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                self.driver.find_element(by, value).set_value(keys)
            except WebDriverException as e:
                raise e
            except Exception:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def drag_and_drop(self, origin_el, destination_el):
        pass

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

    def check_element_visible(self, by, value):
        try:
            return self.driver._appium_context().find_element(by, value).is_displayed()
        except Exception as handleRetry:
            try:
                self._refresh()
                return self.driver._appium_context().find_element(by, value).is_displayed()
            except Exception as e:
                return False

    def clear_element_value(self, by, value):
        try:
            self.driver.find_element(by, value).clear()
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_present(self.driver, by, value)
                self.driver.find_element(by, value).clear()
            except WebDriverException as e:
                raise e
            except Exception as e:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def scroll_element_ios(self, scroller_locator, target_element_locator, forward):
        scroller = self.driver.find_element(scroller_locator[0], scroller_locator[1])
        target_element = self.driver.find_element(target_element_locator[0], target_element_locator[1])
        scroller_location_x = scroller.rect.get('x')
        scroller_location_y = scroller.rect.get('y')
        scroller_width = scroller.rect.get('width')
        scroller_height = scroller.rect.get('height')
        scroller_center_x = (scroller_location_x + scroller_width) * 1 / 2
        scroller_center_y = (scroller_location_y + scroller_height) * 1 / 2
        scroller_list = self.driver.find_elements(scroller_locator[0], scroller_locator[1] + '/XCUIElementTypeAny')
        swipe_duration = 2000

        if forward == 'right':
            start_x = scroller_location_x + scroller_width * 1 / 5
            start_y = scroller_center_y
            end_x = scroller_location_x + scroller_width * 4 / 5
            end_y = scroller_center_y
        elif forward == 'left':
            start_x = scroller_location_x + scroller_width * 4 / 5
            start_y = scroller_center_y
            end_x = scroller_location_x + scroller_width * 1 / 5
            end_y = scroller_center_y
        elif forward == 'down':
            start_x = scroller_center_x
            start_y = scroller_location_y + scroller_height * 1 / 5
            end_x = scroller_center_x
            end_y = scroller_center_x, scroller_location_y + scroller_height * 4 / 5
        elif forward == 'up':
            start_x = scroller_center_x
            start_y = scroller_location_y + scroller_height * 4 / 5
            end_x = scroller_center_x
            end_y = scroller_location_y + scroller_height * 1 / 5

        while not target_element.is_displayed() and not scroller_list[len(scroller_list) - 1].is_displayed():
            self.__app_driver.swipe(start_x, start_y, end_x, end_y, swipe_duration)

    '''
    This function is used for Android app login page at present.
    If ther pages fields cannot user send_keys or set_value, may try this method.
    '''

    def find_element_set_special_value(self, by, value, keys):
        try:
            self.driver.find_element(by, value).click()
            action = ActionChains(self.driver._Driver__app_driver)
            action.send_keys(keys)
            action.perform()

        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                self.driver.find_element(by, value).click()
                action = ActionChains(self.driver._Driver__app_driver)
                action.send_keys(keys)
                action.perform()
            except WebDriverException as e:
                raise e
            except Exception as e:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def get_element_text(self, by, value):
        try:
            return self.driver.find_element(by, value).text
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                return self.driver.find_element(by, value).text
            except WebDriverException as e:
                raise e
            except Exception as e:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def get_elements_text(self, by, value):
        list_text = []
        try:
            elements = self.driver.find_elements(by, value)
            for i in elements:
                list_text.append(i.text)
            return list_text
        except WebDriverException as e:
            raise e
        except Exception as e:
            raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def find_element_location_in_view(self, by, value):
        try:
            self.driver.find_element(by, value).location_in_view
        except Exception as handleRetry:
            try:
                self._refresh()
                self.driver.find_element(by, value).location_in_view
            except WebDriverException as e:
                raise e
            except Exception as e:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def android_scroll(self, direction, swipe_time):
        screen = self.driver._Driver__app_driver.get_window_size()
        screen_width = screen['width']
        screen_height = screen['height']

        if direction == "up":
            start_x = screen_width * 0.5
            start_y = screen_height * 0.75
            end_x = screen_width * 0.5
            end_y = screen_height * 0.5
        elif direction == "down":
            start_x = screen_width * 0.5
            start_y = screen_height * 0.25
            end_x = screen_width * 0.5
            end_y = screen_height * 0.5
        elif direction == "left":
            start_x = screen_width * 0.75
            start_y = screen_height * 0.5
            end_x = screen_width * 0.25
            end_y = screen_height * 0.5
        elif direction == "right":
            start_x = screen_width * 0.25
            start_y = screen_height * 0.5
            end_x = screen_width * 0.75
            end_y = screen_height * 0.5

        for i in range(0, int(swipe_time)):
            self.driver._Driver__app_driver.swipe(start_x, start_y, end_x, end_y)

    def android_scroll_to_specific_text(self, text):
        self.driver._Driver__app_driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("'
            + text + '").instance(0));')

    def android_scroll_to_element(self, by1, value1, by2, value2):
        element1 = self.driver.find_element(by1, value1)
        element2 = self.driver.find_element(by2, value2)
        self.driver.execute_script('mobile:scrollBackTo', {element1, element2})

    def android_scroll_element_to_specific_height(self, by, value, height):
        screen = self.driver._Driver__app_driver.get_window_size()
        screen_height = screen['height']
        element = self.driver.find_element(by, value)
        element_x = element.location['x']
        element_y = element.location['y']
        end_y = screen_height * height
        self.driver._Driver__app_driver.swipe(element_x, element_y, element_x, end_y)

    def element_show(self, by, value):
        try:
            self.driver._appium_context().find_element(by, value)
        except Exception as e:
            return False
        else:
            return True

    def wait_element_text_visible(self, by, value, text):
        try:
            WaitUtils.wait_for_element_text_visible(self.driver, by, value, text)
            return True
        except Exception as e:
            return False

    def find_element_get_attribute(self, by, value, attr):
        try:
            return self.driver.find_element(by, value).get_attribute(attr)
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                return self.driver.find_element(by, value).get_attribute(attr)
            except WebDriverException as e:
                raise e
            except Exception as e:
                raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def scroll_by_direction(self, direction):
        self.driver.execute_script('mobile: scroll', {'direction': direction})

    # name is the accessibility id of the element
    def scroll_by_name(self, name):
        self.driver.execute_script('mobile: scroll', {'name': name})

    def swipe(self, direction):
        self.driver.execute_script('mobile: swipe', {'direction': direction})

    def find_elements_click(self, by, value, index):
        try:
            elements = self.driver.find_elements(by, value)
            elements[index].click()
        except WebDriverException as e:
            raise e
        except Exception as e:
            raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

    def find_elements_count(self, by, value):
        try:
            elements = self.driver.find_elements(by, value)
            return len(elements)
        except WebDriverException as e:
            raise e

    def get_element_location(self, by, value):
        try:
            return self.driver.find_element(by, value).location
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                return self.driver.find_element(by, value).location
            except Exception as e:
                raise e

    def check_element_enabled(self, by, value):
        try:
            return self.driver.find_element(by, value).is_enabled()
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                return self.driver.find_element(by, value).is_enabled()
            except Exception as e:
                raise e

    # TODO: We need to wrap more method here.
