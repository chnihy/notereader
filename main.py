#! python3 

# TODO Order of Operations:
# 1. Wireframe
# 2. Functionality
    # TODO add 'max' for sample size selection
    # TODO add option to use one sample set for all exs or 
    # generate new sample for each exercise
    # TODO allow multiple measure long exs
    # TODO remove duplicate options: in measure, in ex    
    # TODO Customize appearance in XML, line breaks and 
    # exercise numbers etc...
# 3. Data validation
# 4. Design


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.properties import NumericProperty

from kivy.core.window import Window

import config
import scales
from scales import allnotes_master
import playback
import exercise_generator

Window.maximize()

#### Modules
class Module(BoxLayout):
    pass
class Panel(BoxLayout):
    pass

class Time(Module):
    def set_tempo(self, tempo):
        config.tempo = int(tempo)
    
    def set_beats(self, beats):
        if beats == "":
            config.beats = 4
        else:
            config.beats = int(beats)
    
    def set_beattype(self, beattype):
        config.beattype = beattype


class Rhythm(Module):
    def set_rhythm(self, rhythm):
        config.rhythm = rhythm


class ScaleSelect(Module):
    
    def set_clef(self, clef):
        config.clef = clef

    # Set key only pertains to what keysig is printed, not the scale
    def set_key_signature(self, key_signature):
        config.key_signature = key_signature

    def set_root(self, root):
        config.root = root

    def set_scaletype(self, scaletype):
        config.scaletype = scaletype

    def set_flats_or_sharps(self, selection):
        flats = ["C","F","Bb","Eb","Ab","Db","Gb"]
        if selection in flats:
            config.flats = True
        else:
            config.flats = False


class Exercises(Module):
    def set_sample_size(self, sample_size):
        if sample_size == "":
            config.sample_size = 1
        else:
            config.sample_size = int(sample_size)
    
    def set_num_of_exs(self, set_num_of_exs):
        if num_of_exs == "":
            config.num_of_exs = 1
        else:
            config.num_of_exs = int(num_of_exs)
    
    def set_title(self, title):
        config.title = title


# Menus
class RootList(Spinner):
	rootlist = allnotes_master

class RhythmList(Spinner):
	rhythmlist = ["quarter","eighth","triplet","sixteenth","16th triplet","thirty second"]

class ScaleList(Spinner):
	scalelist = list(scales.allscales.keys())

class KeySigList(Spinner):
    key_signatures = scales.key_signatures

# Main window
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

		# Enter key functionality binding
        Window.bind(on_key_down = self._on_keyboard_down)
    
    def run(self):
        # Assigning our scale in config
        config.scale = scales.allscales[config.scaletype][config.root]

        # Running the exercise generator program
        exercise_generator.run()

		# Calling SCAMP for transcription
        playback.play() # TODO Key signature

    # Enter key function
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.run()

# App
class MainApp(App):
    def build(self):
        self.title = "Note Reader App"

        return MainLayout()


if __name__ == "__main__":
    MainApp().run()