from base.seleniumdriver import SeleniumDriver
from utilities import cutomlogger as cl
import logging


class LoginPO(SeleniumDriver):
    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _usernametxtbx = "//input[@id='username']"
    _pwdtxtbx = "//input[@placeholder='Password']"
    _keepme_loggedin_chkbx = "//div[@id='keepLoggedInCheckBoxContainer']"
    _loginbtn = "//a[@id='loginButton']"
    _error_msg = "//span[contains(text(),'Username or Password is invalid. Please try again.')]"

    def sendUserName(self,username):
        self.sendData(username,self._usernametxtbx,locatortype="xpath")

    def sendPwd(self,pwd):
        self.sendData(pwd,self._pwdtxtbx,locatortype="xpath")

    def keepmeloggedinChkbx(self):
        self.clickElement(self._keepme_loggedin_chkbx,locatortype="xpath")

    def clicklgnbtn(self):
        self.clickElement(self._loginbtn,locatortype="xpath")
        #self.waitForElementClickable(self._loginbtn,locatortype="xpath")

    def errormsg(self):
        return self.getText(self._error_msg,locatortype="xpath")


