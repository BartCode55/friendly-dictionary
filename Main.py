import kivy
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

class MenuWindow(Screen):
    pass

class DictionaryWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("builder.kv")

class FriendlyDictionaryApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    FriendlyDictionaryApp().run()