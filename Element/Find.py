from Utilitys.WaitUtils import WaitUtils
from functools import wraps

class Find:

    def __init__(self):
        pass

    def find_log_decorator(func):
        """
        输出Exception的装饰器
        :param func:
        :return:
        """

        @wraps(func)
        def wrapper(*args):
            try:
                result = func(*args)
            except Exception as e:
                logging.error(func.__name__ + ' run failed')
                raise Exception("Cannot find element by [%s]:under:\n %s \n" % (args[1], args[2]))
            return result

        return wrapper

    def get_driver(self):
        pass

    def _appium_context(self):
        pass

    def _refresh(self):
        pass

    @find_log_decorator
    def find_element(self, by, value):
            try:
                return self._appium_context().find_element(by, value)
            except Exception as handleRetry:
                self._refresh()
                WaitUtils.wait_for_element_present(self._appium_context(), by, value)
                return self._appium_context().find_element(by, value)

    def find_elements(self, by, value, number=1):
        try:
            if len(self.__find_elements(by, value)) >= number:
                return self.__find_elements(by, value)
            else:
                raise Exception
        except Exception as handleRetry:
            self._refresh()
            WaitUtils.wait_for_elements_number_right(self._appium_context(), by, value, number)
            return self.__find_elements(by, value)

    def __find_elements(self, by, value):
        try:
            try:
                return self._appium_context().find_elements(by, value)
            except Exception as handleRetry:
                self._refresh()
                WaitUtils.wait_for_element_present(self._appium_context(), by, value)
                return self._appium_context().find_elements(by, value)
        except Exception as e:
            raise Exception("Cannot find element by [%s] under: \n %s \n" % (value, self))
