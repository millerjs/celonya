from collections import OrderedDict
from random import randint

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.rst import RstDocument

from editors import IntegerEditorPopup, TextPromptPopup
from value_table import ValueTable
from models import Character, Race, session, Class
from util import DarkTextInput

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

class CharacterDetails(BoxLayout):
    orientation = 'horizontal'
    size_hint = (1, .1)


class CharacterRace(BoxLayout):
    orientation = 'horizontal'

    def __init__(self, character, *args, **kwargs):
        self.character = character
        super(CharacterRace, self).__init__(*args, **kwargs)

        spinner = Spinner(
            font_size=FONT_XLARGE,
            text=self.character.race or '',
            values=[race.name for race in session.query(Race)])

        def view_details(_):
            details = Popup(size_hint=(.8, .8), title=self.character.race)
            race = (session.query(Race)
                    .filter(Race.name == self.character.race)
                    .scalar())
            if race:
                text = race.details
            else:
                text = "Race '%s' not found" % self.character.race

            details.add_widget(RstDocument(text=text))
            details.open()

        self.add_widget(Button(
            text="Race details",
            font_size=FONT_XLARGE,
            on_press=view_details))

        spinner.bind(text=self.update)
        self.add_widget(spinner)


    def update(self, spinner, race):
        self.character.race = race
        self.character = session.merge(self.character)
        session.commit()


class CharacterClass(BoxLayout):
    orientation = 'horizontal'

    def __init__(self, character, *args, **kwargs):
        self.character = character
        super(CharacterClass, self).__init__(*args, **kwargs)

        spinner = Spinner(
            font_size=FONT_XLARGE,
            text=self.character.class_ or '',
            values=[class_.name for class_ in session.query(Class)])

        spinner.bind(text=self.update)

        def view_details(_):
            details = Popup(size_hint=(.8, .8), title=self.character.class_)
            class_ = (session.query(Class)
                      .filter(Class.name == self.character.class_)
                      .scalar())
            if class_:
                text = class_.details
            else:
                text = "Class_ '%s' not found" % self.character.class_

            details.add_widget(RstDocument(text=text))
            details.open()

        self.add_widget(Button(
            text="Class details",
            font_size=FONT_XLARGE,
            on_press=view_details))

        self.add_widget(spinner)

    def update(self, spinner, class_):
        self.character.class_ = class_
        self.character = session.merge(self.character)
        session.commit()



class StatTab(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(StatTab, self).__init__(*args, **kwargs)
        self.text = 'Stats'
        self.character = character

        self.content = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.content.spacing = 10

        # General
        details = CharacterDetails()
        self.content.add_widget(details)
        details.add_widget(CharacterRace(self.character))
        details.add_widget(CharacterClass(self.character))

        # Modifiers
        modifiers = ValueTable(
            character, character.modifiers, prefix='+', size_hint=(1, .3))
        self.content.add_widget(modifiers)

        # Auxiliary values
        aux_values = ValueTable(
            character, character.aux_values, size_hint=(1, .3))
        self.content.add_widget(aux_values)
