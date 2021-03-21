import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "Wrongunsername&pw"
        pwd = "Wrongpassword"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[1]/ul[2]/li/a").click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/p[2]/a").click()
        try:
           # attempt to find the lost password
           elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/form/input[2]")
           assert True

        except:
            self.fail("wrong log info not successful")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
