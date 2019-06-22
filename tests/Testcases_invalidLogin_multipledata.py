import pytest
from pages.LoginPO import LoginPO
from pages.HomePO import HomePO
import unittest
import time
from ddt import ddt,data,unpack
from utilities.readdata import getcsvdata


@pytest.mark.usefixtures("setup","ontimesetup")
@ddt
class TestDemo1(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classLevelsetup(self):
        print("Class level setup")
        self.lp = LoginPO(self.driver)
        self.hp = HomePO(self.driver)

    @data(*getcsvdata("C:\\Users\\shekar\\PycharmProjects\\AutomationFW\\testdata.csv"))
    @unpack
    def testmethodA(self,UserName,Password):
        print("Testing method A")
        self.lp.sendUserName(UserName)
        self.lp.sendPwd(Password)
        self.lp.keepmeloggedinChkbx()
        self.lp.clicklgnbtn()
        time.sleep(5)
        assert self.lp.errormsg() == "Username or Password is invalid. Please try again."



