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
        print("Testing method A")
        self.lp.sendUserName("admin")
        self.lp.sendPwd("manager")
        self.lp.keepmeloggedinChkbx()
        self.lp.clicklgnbtn()
        print(self.hp.getCurentTitle())
        time.sleep(15)
        assert self.hp.getCurentTitle() == "actiTIME - Enter Time-Track"
        time.sleep(15)
        self.hp.clickLogoutBtn()


