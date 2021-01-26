from appium_flutter_finder.flutter_finder import *
from Utilitys.WaitUtils import WaitUtils


class FlutterFind:
    def __init__(self):
        self.finder = FlutterFinder()

    def get_driver(self):
        pass

    def _appium_context(self):
        pass

    def find_flutter_element(self, value):
        try:
            WaitUtils.flutter_wait_for_element(self._appium_context(), value)
            return FlutterElement(self._appium_context(), value)
        except Exception as handleRetry:
            try:
                WaitUtils.flutter_wait_for_element(self._appium_context(), value)
                return FlutterElement(self._appium_context(), value)
            except Exception as e:
                raise e
