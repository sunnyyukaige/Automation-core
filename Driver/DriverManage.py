import os

from Driver.Driver import Driver

__author__ = 'sunny.yu2'


class DriverManage(Driver):
    driver = None

    @staticmethod
    def set_driver(env="ios", desired_capability=None, app_path=''):
        if DriverManage.driver is None:
            if env == "Android":
                app = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
                # app = os.path.abspath(os.path.join(os.path.dirname(__file__),
                # '../../build/outputs/apk/app-dev-debug.apk'))
                desired_capabilities = {
                    'app': app,
                    'platformName': 'Android',
                    'platformVersion': '7.0',
                    'deviceName': 'test',
                    'browserName': 'Android',
                    'unicodeKeyboard': True,
                    'noReset': True
                }

            elif env == "ios":
                app = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Panda.app'))
                desired_capabilities = {
                    'app': app,
                    'platformName': 'iOS',
                    'platformVersion': '13.3',
                    'deviceName': 'iPhone 8',
                    'noReset': False
                    #  'autoWebview': True
                }
            if app_path != '':
                app = app
            elif desired_capability is not None:
                desired_capabilities = desired_capability
            DriverManage.driver = Driver("appium", command_executor='http://127.0.0.1:4723/wd/hub',
                                         desired_capabilities=desired_capabilities).get_driver()
        else:
            pass
        return DriverManage.driver

    @staticmethod
    def clear_browser():
        DriverManage.driver = None
