
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By

class Class1:
    def __init__(self):
        self.driver_chromeexe_location = "C:\\Users\\shekar\\PycharmProjects\\" \
                              "SeleniumPractice\\drivers\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = self.driver_chromeexe_location
        self.driver_ffexe_location = "C:\\Users\\shekar\\PycharmProjects" \
                              "\\SeleniumPractice\\drivers\\geckodriver.exe"
        os.environ["webdriver.gecko.driver"] = self.driver_ffexe_location
        self.driver_ieexe_location = "C:\\Users\\shekar\\PycharmProjects" \
                          "\\SeleniumPractice\\drivers\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = self.driver_ieexe_location
        self.driver = webdriver.Chrome(executable_path=self.driver_chromeexe_location)
        #self.driver = webdriver.Firefox(executable_path=self.driver_ffexe_location)
        # self.driver = webdriver.Ie(executable_path=self.driver_ieexe_location)

    def method1(self):
        self.driver.get("http://localhost/login.do")
        self.driver.find_element(By.XPATH,"//input[@id='username']").\
            send_keys("admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")\
            .send_keys("manager")
        self.driver.find_element(By.XPATH,
                                 "//div[@id='keepLoggedInCheckBoxContainer']")\
            .click()
        self.driver.find_element(By.XPATH,"//a[@id='loginButton']").click()
        time.sleep(5)
        #self.driver.find_element(By.XPATH,"//a[@id='logoutLink']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Logout']").click()
        time.sleep(10)
        self.driver.close()



def main():
    obj1 = Class1()
    obj1.method1()

if __name__ == '__main__':
    main()
