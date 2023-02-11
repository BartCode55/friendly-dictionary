import kivy
import random
import copy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class DictionaryMethods():
    lines = []
    gameList = []
    correctList = []
    answerList = []
    number = 0
    def dictionaryPress(self):
        try:
            with open('slowa.txt', 'r', encoding='utf8') as file:
                self.lines = file.read().splitlines()
        except FileNotFoundError:
            print("Where friction Tuco")

        self.lines.sort(key=lambda v: v.upper())
        #for line in self.lines:
            #print(line)
    def randomWordsGame(self):
        self.gameList = random.sample(self.lines, k=5)
        #for line in self.gameList:
            #print(line)

        self.ids.AlphabetLabel.text = f'Oto lista słów:' \
                                      f'\n1.{self.gameList[0]}' \
                                      f'\n2.{self.gameList[1]}' \
                                      f'\n3.{self.gameList[2]}' \
                                      f'\n4.{self.gameList[3]}' \
                                      f'\n5.{self.gameList[4]}'
        self.correctList = self.gameList.copy()
        self.correctList.sort(key=lambda v: v.upper())
    def randomWordsAddition(self):#potem rozwiń to tak by np podawał dobrą tablice jak sie zle odpowie albo zrobic to popupem nie wiem
        answer = self.ids.AlphabetInput.text
        self.answerList.append(answer)
        self.number = self.number + 1
        self.ids.AlphabetInput.text = ""
        #for line in self.answerList:
            #print(line)

        if self.number == 5:
            if self.answerList == self.correctList:
                self.ids.AlphabetLabel.text = "Brawo jesteś mistrzem alfabetu!"
            else:
                self.ids.AlphabetLabel.text = "Zła odpowiedź! Następnym razem na pewno się uda!"
                #print("Oto poprawna lista!")
                #for line in self.correctList:
                    #print(line)

class MenuWindow(Screen, DictionaryMethods):
    pass

class DictionaryWindow(Screen):
    pass

class GamesWindow(Screen):
    pass

class AlphabetGame(Screen, DictionaryMethods):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("builder.kv")

class FriendlyDictionaryApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    FriendlyDictionaryApp().run()