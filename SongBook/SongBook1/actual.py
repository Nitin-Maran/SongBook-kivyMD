from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import helpers

list_helper = """


"""
class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        return screen



DemoApp().run()
