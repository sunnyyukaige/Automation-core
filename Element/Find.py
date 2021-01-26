from Utilitys.WaitUtils import WaitUtils


class Find:

    def __init__(self):
        pass

    def get_driver(self):
        pass

    def _appium_context(self):
        pass

    def _refresh(self):
        pass

    def find_element(self, by, value):
        try:
            try:
                return self._appium_context().find_element(by, value)
            except Exception as handleRetry:
                self._refresh()
                WaitUtils.wait_for_element_present(self._appium_context(), by, value)
                return self._appium_context().find_element(by, value)
        except Exception as e:
            raise Exception("Cannot find element by [%s]:[%s] under:\n %s \n" % (by, value, self))

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
