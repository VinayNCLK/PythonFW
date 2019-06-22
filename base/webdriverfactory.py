import os
from selenium import webdriver
from utilities import cutomlogger as cl
import logging


class WebDriverFactory:
    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,browser):
        self.browser = browser
        self.driver_chromeexe_location = "C:\\Users\\shekar\\PycharmProjects\\AutomationFW\\drivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = self.driver_chromeexe_location
        self.driver_ffexe_location = "C:\\Users\\shekar\\PycharmProjects\\AutomationFW\\drivers\\geckodriver.exe"
        os.environ["webdriver.gecko.driver"] = self.driver_ffexe_location
        self.driver_ieexe_location = "C:\\Users\\shekar\\PycharmProjects\\AutomationFW\\drivers\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = self.driver_ieexe_location

    def getDriverInstance(self):
        global driver
        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=self.driver_chromeexe_location)
            self.log.info("Test cases will execute in chrome browser")
        elif self.browser == "ff":
            driver = webdriver.Firefox(executable_path=self.driver_ffexe_location)
            self.log.info("Test cases will execute in ff browser")
        elif self.browser == "ie":
            driver = webdriver.Ie(executable_path=self.driver_ieexe_location)
            self.log.info("Test cases will execute in ie browser")
        else:
            self.log.error("Please provide the valid browser name eg: chrome, ff, ie")

        driver.get("http://localhost/login.do")
        driver.implicitly_wait(10)
        return driver
