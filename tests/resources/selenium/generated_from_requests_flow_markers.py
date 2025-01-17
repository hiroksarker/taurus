# coding=utf-8

import logging
import random
import string
import sys
import unittest
from time import time, sleep

import apiritif

import os
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bzt.resources.selenium_extras import FrameManager, WindowManager

def setup():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service_log_path='<somewhere>webdriver.log', chrome_options=options)
    driver.implicitly_wait(3.5)
    wnd_mng = WindowManager(driver)
    frm_mng = FrameManager(driver)
    vars = {

    }
    apiritif.put_into_thread_store(vars, driver, wnd_mng, frm_mng)


def teardown():
    (_, driver, _, _) = apiritif.get_from_thread_store()
    driver.quit()


class TestLocSc(unittest.TestCase):

    def setUp(self):
        (self.vars, self.driver, self.wnd_mng, self.frm_mng) = apiritif.get_from_thread_store()

    def test_1_(self):
        try:
            self.driver.execute_script('/* FLOW_MARKER test-case-start */', {
                'testCaseName': '/',
                'testSuiteName': 'loc_sc',
            })
            with apiritif.transaction_logged('/'):
                self.driver.get('http://blazedemo.com/')
                WebDriverWait(self.driver, 3.5).until(econd.presence_of_element_located((By.XPATH, "//input[@type='submit']")), 'Element "//input[@type=\'submit\']" failed to appear within 3.5s')
                self.assertEqual(self.driver.title, 'BlazeDemo')
                body = self.driver.page_source
                re_pattern = re.compile('contained_text')
                self.assertEqual(0, len(re.findall(re_pattern, body)), "Assertion: 'contained_text' found in BODY")
        except AssertionError as exc:
            self.driver.execute_script('/* FLOW_MARKER test-case-stop */', {
                'status': 'failed',
                'message': str(exc),
            })
            raise
        except BaseException as exc:
            self.driver.execute_script('/* FLOW_MARKER test-case-stop */', {
                'status': 'broken',
                'message': str(exc),
            })
            raise
        else:
            self.driver.execute_script('/* FLOW_MARKER test-case-stop */', {
                'status': 'success',
                'message': '',
            })

    def test_2_empty(self):
        try:
            self.driver.execute_script('/* FLOW_MARKER test-case-start */', {
                'testCaseName': 'empty',
                'testSuiteName': 'loc_sc',
            })
            with apiritif.transaction_logged('empty'):
                pass
        except AssertionError as exc:
            self.driver.execute_script('/* FLOW_MARKER test-case-stop */', {
                'status': 'failed',
                'message': str(exc),
            })
            raise
        except BaseException as exc:
            self.driver.execute_script('/* FLOW_MARKER test-case-stop */', {
                'status': 'broken',
                'message': str(exc),
            })
            raise
        else:
            self.driver.execute_script('/* FLOW_MARKER test-case-stop */', {
                'status': 'success',
                'message': '',
            })
