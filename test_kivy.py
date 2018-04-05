from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder


runTouchApp(Builder.load_string('''

BoxLayout:
    Button:
        text: 'Test'
        
    

'''))
