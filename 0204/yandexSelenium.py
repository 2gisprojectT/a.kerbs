__author__ = 'Sasha'

# coding: utf-8
from selenium import webdriver
from unittest import TestCase
import unittest


class Test_Ya(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.yandex.ru")

    def test_title1(self):
        element = self.driver.find_element_by_name('text')
        element.send_keys('проверка')
        element.click()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_xpath("//button[@type='submit']")
        element.click()

        title_value = self.driver.title
        self.assertIn('проверка', title_value, "Неверное значение")

    def test_Url(self):
        dd=self.driver.find_element_by_class_name('b-weather__icon_link')
        dd.click()
        self.assertEqual(self.driver.current_url, 'https://pogoda.yandex.ru/novosibirsk/', "Неправильный переход")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
