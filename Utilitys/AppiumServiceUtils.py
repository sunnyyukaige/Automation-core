from appium.webdriver.appium_service import AppiumService


class AppiumServiceUtils(object):

    appium_server = AppiumService()

    @staticmethod
    def start_appium():

        # appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
        errmsg = ""
        try:
            AppiumServiceUtils.appium_server.start()

        except Exception as msg:
            errmsg = str(msg)
            print(errmsg)
        return errmsg

    @staticmethod
    def stop_appium():
        errmsg = ""
        try:
            AppiumServiceUtils.appium_server.stop()
        except Exception as msg:
            errmsg = str(msg)
        return errmsg
