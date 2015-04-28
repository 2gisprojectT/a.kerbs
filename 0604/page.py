__author__ = 'Sasha'
from yandextest import YandexText
class Page():
    def __init__(self, driver):
        self.driver = driver

    def OpenUrl(self, url):
        self.driver.get(url)
        return self

    def GetUrl(self):
        return self.driver.current_url

    def GetTitle(self):
        return self.driver.title

    def EnterToFind(self,text):
        self.YandexText = YandexText(self.driver)
        self.YandexText.entering(text)

    def ClickToElem(self,textName):
        self.YandexText = YandexText(self.driver)
        self.YandexText.clickElem(textName)
