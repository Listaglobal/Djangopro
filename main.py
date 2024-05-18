from kivy.app import App
from kivy.uix.label import Label

class BasicApp(App):
    def Build(self):
        label = Label(text='Hello World')
        return label
    
    app = BasicApp()
    app.run()


    
