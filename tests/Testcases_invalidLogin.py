import pytest
from pages.LoginPO import LoginPO
from pages.HomePO import HomePO
import unittest
import time


@pytest.mark.usefixtures("setup","ontimesetup")
class TestDemo1(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classLevelsetup(self):
        print("Class level setup")
        self.lp = LoginPO(self.driver)
        self.hp = HomePO(self.driver)

    def testmethodA(self):
        try:
            print("Testing method A")
            self.lp.sendUserName("admin1")
            self.lp.sendPwd("manager1")
            self.lp.keepmeloggedinChkbx()
            self.lp.clicklgnbtn()
            time.sleep(5)
            assert self.lp.errormsg() == "sername or Password is invalid. Please try again."
        except:
            self.driver.get_screenshot_as_file("C:\\Users\\shekar\\PycharmProjects\\AutomationFW\\screenshots\\TestDemo1.png")


