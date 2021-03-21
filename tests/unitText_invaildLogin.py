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
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        #assert "Logged in"
        try:
            # attempt to find the sentence 'Your username and password didn't match. Please try again'
            # if found, means log in failed.
            # test successful
           elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/p[1]")
           assert True

        except:
            self.fail("wrong log info not successful")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
