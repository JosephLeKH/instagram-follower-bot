from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time as t
import os


class InstaFollower:

    def __init__(self):
        #Target following account
        self.TARGET = "kingjames"

        #Initialize Selenium driver
        chrome_driver = os.environ["DRIVER_PATH"]
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        ser = Service(executable_path=chrome_driver, log_path="NUL")
        self.driver = webdriver.Chrome(service=ser, options=options)

        self.EMAIL = os.environ["EMAIL"]
        self.PW = os.environ["INSTA_PASSWORD"]
        self.follows = ""

    def login(self):
        self.driver.get("https://www.instagram.com/")
        t.sleep(3)
        email = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.click()
        email.send_keys(self.EMAIL)
        pw = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw.click()
        pw.send_keys(self.PW)
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]').click()
        t.sleep(3)

    def follow(self):
        t.sleep(1)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/'
                                                    'div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]/div/div/span/span').click()
        t.sleep(0.5)
        search = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/'
                                                             'div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search.click()
        search.send_keys(self.TARGET)
        t.sleep(2)
        search.send_keys(Keys.DOWN)
        search.send_keys(Keys.DOWN)
        search.send_keys(Keys.ENTER)
        t.sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]'
                                                    '/div[2]/section/main/div/header/section/ul/li[3]/a').click()
        t.sleep(1)


        #Scroll down to the bottom of the following pop-up
        pop_up_window = WebDriverWait(
            self.driver, 2).until(ec.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')))

        self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)

        #Follow every account from the end of the list while scrolling up
        self.follows = self.driver.find_elements(by=By.CSS_SELECTOR, value='.x9f619 ._acan')
        self.follows.reverse()
        for x in self.follows:
            actions = ActionChains(self.driver)
            actions.move_to_element(x).perform()

            x.click()
            self.driver.find_element(by=By.XPATH,
                                         value='/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/'
                                               'div/div/div/div/button[2]').click()
            t.sleep(0.5)

        self.driver.quit()



