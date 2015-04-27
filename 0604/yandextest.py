__author__ = 'Sasha'

from base_component import BaseComponent

class YandexText(BaseComponent):
    data ={
        'textEnter': 'text',
        'buttonEnter':"//button[@type='submit']",
    }

    def entering(self,text):
        self.driver.find_element_by_id(self.data['textEnter']).send_keys(text)
        self.driver.find_element_by_xpath(self.data['buttonEnter']).click()

    def clickElem(self,text):
        self.element = self.driver.find_element_by_class_name(text).click()
