# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://ehall.yzu.edu.cn/infoplus/form/XNYQSB/start")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("MZ120201331")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("2wa3es4rd")
        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/form[1]/div[5]/input").click()
        print('账号登入')
        driver.find_element_by_id("preview_start_button").click()
        print('开始办理')
        driver.find_element_by_id("V1_CTRL8").click()
        driver.find_element_by_id("V1_CTRL8").clear()
        driver.find_element_by_id("V1_CTRL8").send_keys(u"动研2020")
        print('输入班级完成')
        driver.find_element_by_id("fieldSFZX-0").click()  # 在校
        print('在校选项点击完成')
        '''
        dropdown1 = driver.find_element_by_id("V1_CTRL117_Container")
        dropdown1.click()
        time.sleep(2)
        driver.execute_script("document.querySelectorAll('select')[0].click()")
        print('shutdown unvisible 0')
        search1 = dropdown1.find_element_by_tag_name("input")
        search1.click()
        time.sleep(2)
        search1.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN,
                          Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN)
        time.sleep(2)
        search1.click()
        search1.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN,
                          Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)

        print('省份选择完成')

        dropdown2 = driver.find_element_by_id("V1_CTRL118_Container")
        dropdown2.click()
        time.sleep(2)
        driver.execute_script("document.querySelectorAll('select')[0].click()")
        print('shutdown unvisible 1')
        search2 = dropdown2.find_element_by_tag_name("input")
        search2.click()
        search2.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.DOWN,
                          Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        print('城市选择完成')

        dropdown3 = driver.find_element_by_id("V1_CTRL119_Container")
        dropdown3.click()
        time.sleep(2)
        driver.execute_script("document.querySelectorAll('select')[0].click()")
        print('shutdown unvisible 2')
        search3 = dropdown3.find_element_by_tag_name("input")
        search3.click()
        search3.send_keys(Keys.DOWN, Keys.ENTER)
        print('区选择完成')
        
        driver.find_element_by_id("V1_CTRL120").click()
        driver.find_element_by_id("V1_CTRL120").clear()
        driver.find_element_by_id("V1_CTRL120").send_keys(u"阿尔滕肯特小区")
        print('当前所在地点填写完毕')
        '''
        driver.find_element_by_id("V1_CTRL121").click()
        driver.find_element_by_id("V1_CTRL121").clear()
        driver.find_element_by_id("V1_CTRL121").send_keys(u"无")
        print('出行记录填写完毕')
        driver.find_element_by_xpath("//*[@id=\"V1_CTRL115\"]").click()
        print('特别提醒勾选')
        driver.find_element_by_xpath("//*[@id=\"V1_CTRL109\"]").click()
        print('上午体温')
        driver.find_element_by_xpath("//*[@id=\"V1_CTRL111\"]").click()
        print('下午体温')
        driver.find_element_by_xpath("//*[@id=\"V1_CTRL114\"]").click()
        print('无相关症状')
        driver.find_element_by_xpath("//*[@id=\"V1_CTRL82\"]").click()
        print('承诺可靠')
        driver.find_element_by_xpath("/html/body/div[4]/form/div/div[1]/div[2]/ul/li[1]/a").click()
        print('确认填报')
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/button[1]").click()
        print('确定弹框1完成')
        driver.find_element_by_id("#dialog_container_262761 > div.dialog_footer > button").click()
        print('确定弹框2完成')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
