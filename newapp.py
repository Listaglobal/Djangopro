from mimetypes import init
import kivy
from kivy.app import App
from kivy.uix.gridlayout import Gridlayout
from kivy.uix.label import Label
from kivy.uix.textinput import Testinput
from kivy.uix.button import Button

class childApp(Gridlayout):
    def init(self,**kwargs):
        super(childApp, self). init()
    self.cols = 2
    self.add_widget(Label(test = 'Student Name'))
    self.s_name = Testinput()
    self.add_widget(Self.s_name)

    self.add_widget(Label(test = 'Student Marks'))
    self.s_marks = Testinput()
    self.add_widget(Self.s_marks)

    self.add_widget(Label(test = 'Student Gender'))
    self.s_gender = Testinput()
    self.add_widget(Self.s_gender)

class parentApp(App):
    def build(self):
        return childApp()
if name == "main":
    parentApp().run()



