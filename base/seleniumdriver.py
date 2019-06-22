from utilities import cutomlogger as cl
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumDriver():
    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getbytype(self,locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "linktext":
            return By.LINK_TEXT
        elif locatortype == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Provided locator type is wrong -"
                           " Please provide valid locator type - "
                           "Name, ID, Xpath, Css selector")
            print_stack()
        return False

    def getWebElement(self, locator, locatortype="id"):
        element = None
        try:
            bytetype = self.getbytype(locatortype)
            element = self.driver.find_element(bytetype, locator)
            self.log.info("Identified the web element with locator " +
                          locator + " locator type " + locatortype)
        except:
            self.log.error("Unable to identify the element with locator "
                           ""+locator+" locator type "+locatortype)
            print_stack()
        return element

    def elementisdisplayed(self, locator, locatortype="id"):
        try:
            element = self.getWebElement(locator,locatortype)
            if element is not None:
                self.log.info("Element is displayed in the webpage "
                              "with locator "+locator)
                return True
            else:
                self.log.error("Element is not displayed on the webpage "
                               "with locator " + locator)
                return False
        except:
            self.log("Element is not displayed with locator "+locator)
            print_stack()
            return False

    def sendData(self, data, locator, locatortype="id"):
        try:
            element = self.getWebElement(locator,locatortype)
            element.send_keys(data)
            self.log.info("Sent some data to element - "+locator+" date "+data)
        except:
            self.log.error("Unable to Send data to element - "
                           + locator + " date " + data)
            print_stack()

    def clickElement(self, locator, locatortype="id"):
        try:
            element = self.getWebElement(locator, locatortype)
            element.click()
            self.log.info("Clicked on element - " + locator)
        except:
            self.log.error("Unable to click on element - " + locator)
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getText(self,locator, locatortype="id"):
        gettext=None
        try:
            element = self.getWebElement(locator, locatortype)
            gettext = element.text
        except:
             print_stack()
        return gettext

    def getrefreshpage(self):
        self.driver.refresh()

    def clickOnBackBtn(self):
        self.driver.back()

    def clickOnFrwdBtn(self):
        self.driver.forward()

    def getURL(self):
        return self.driver.current_url

    def select_drpdw(self, visibletext, locator, locatortype="id"):
        try:
            element = self.getWebElement(locator, locatortype)
            s1 = Select(element)
            s1.select_by_visible_text(visibletext)
            self.log.info("Selected option "
                          ""+visibletext+" on element - " + locator)
        except:
            self.log.error("Unable to Select option element - " + locator)
            print_stack()

    def switch_to_frame(self,locator, locatortype="id"):
        try:
            element = self.getWebElement(locator, locatortype)
            self.driver.switch_to.frame(element)
            self.log.info("Switched to the frame with webelement "+locator)
        except:
            self.log.error("Unable to swith to "
                           "frame with element - " + locator)
            print_stack()

    def get_Parentwindow_id(self):
        parentwindowid = self.driver.current_window_handle
        return parentwindowid

    def get_AllWindow_id(self):
        allwindowids = self.driver.window_handles
        return allwindowids

    def switch_to_window(self,windowid):
        try:
            self.driver.switch_to.window(windowid)
            self.log.info("Switched to window with window id "+windowid)
        except:
            self.log.error("Unable to switch to window "
                           "with window id - " + windowid)
            print_stack()

    def onmouse_over(self,locator, locatortype="id"):
        try:
            act = ActionChains(self.driver)
            element = self.getWebElement(locator, locatortype)
            act.move_to_element(element).perform()
            self.log.info("Mouse over on element "+locator)
        except:
            self.log.error("Unable to on mouse over on element - " + locator)
            print_stack()

    def acceptAlert(self):
        self.driver.switch_to.alert.accept()

    def cancelAlert(self):
        self.driver.switch_to.alert.dismiss()

    def waitForElementClickable(self, locator, timeout=10, poll_fer=2,
                                locatortype="id"):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_fer,
                             ignored_exceptions=None)
            bytype = self.getbytype(locatortype)
            element = wait.until(EC.element_to_be_clickable
                          ((bytype, locator)))
            element.click()
            self.log.info("Clicked in element with locator - "+locator)
        except:
            self.log.info("Unable to Click on element with locator - " +
                          locator + " after waiting " + timeout)
            print_stack()
