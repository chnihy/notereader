#! python3 

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner

from kivy.core.window import Window

import scales
from scales import allnotes_master

Window.maximize()

#### Modules
class Module(BoxLayout):
    pass

class Time(Module):
    pass

class ScaleSelect(Module):
    pass

class Rhythm(Module):
    pass

class Exercises(Module):
    pass

class Panel(BoxLayout):
    pass

#### Menus
class RootList(Spinner):
	keyslist = allnotes_master

class RhythmList(Spinner):
	rhythmlist = ["quarter","eighth","triplet","sixteenth","16th triplet","32nd"]

class ScaleList(Spinner):
	scalelist = list(scales.allscales.keys())



#### Main window
class MainLayout(BoxLayout):
    
    # Run button
    def run_program(self):
        pass
    
    pass

class MainApp(App):
    def build(self):
        self.title = "Note Reader App"

        return MainLayout()

if __name__ == "__main__":
    MainApp().run()