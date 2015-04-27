__author__ = 'Sasha'

from unittest import TestCase
from selenium import webdriver
from page import Page
import unittest


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.page = Page(self.driver)
        self.page.OpenUrl("http://www.yandex.ru")


    def test_title(self):
        self.page.EnterToFind('проверка')
        self.assertIn( 'проверка', self.page.GetTitle(), "Неверное значение")

    def test_Url(self):
        self.page.ClickToElem('b-weather__icon_link')
        self.assertEqual(self.page.GetUrl(),'https://pogoda.yandex.ru/novosibirsk/', "Неверное значение")


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
