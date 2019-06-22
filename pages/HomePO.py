from base.seleniumdriver import SeleniumDriver
from utilities import cutomlogger as cl
import logging


class HomePO(SeleniumDriver):
    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _logoutbtn = "//a[text()='Logout']"

    def clickLogoutBtn(self):
        self.clickElement(self._logoutbtn,locatortype="xpath")

    def getCurentTitle(self):
        return self.getTitle()
