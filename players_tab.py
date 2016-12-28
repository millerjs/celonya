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

from editors import ValueEditorPopup, TextPromptPopup
from value_table import ValueTable
from models import Character, session
from util import DarkTextInput

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)


class CharacterSheet(TabbedPanelItem):

    def __init__(self, character, font_size=FONT_MEDIUM, *args, **kwargs):
        super(CharacterSheet, self).__init__(
            font_size=font_size, *args, **kwargs)

        self.character = character
        self.text = character.name

        details = TabbedPanel(
            do_default_tab=False,
            tab_width=350,
            tab_height=80)

        details.add_widget(StatTab(character))
        details.add_widget(WeaponsTab())
        details.add_widget(SpellTab())
        details.add_widget(ItemTab())
        details.add_widget(BackstoryTab())

        self.add_widget(details)


class StatTab(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(StatTab, self).__init__(*args, **kwargs)
        self.text = 'Stats'
        self.character = character

        self.content = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.content.spacing = 10

        # Modifiers
        modifiers = ValueTable(
            character, character.modifiers, prefix='+', size_hint=(1, .3))
        self.content.add_widget(modifiers)

        # Auxiliary values
        aux_values = ValueTable(
            character, character.aux_values, size_hint=(1, .3))
        self.content.add_widget(aux_values)


class SpellTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(SpellTab, self).__init__(*args, **kwargs)
        self.text = 'Spells'


class WeaponsTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(WeaponsTab, self).__init__(*args, **kwargs)
        self.text = 'Weapons'


class ItemTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(ItemTab, self).__init__(*args, **kwargs)
        self.text = 'Items'


class BackstoryTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(BackstoryTab, self).__init__(*args, **kwargs)
        self.text = 'Backstory'


class CharacterActionsTab(TabbedPanelItem):

    def __init__(self, parent, *args, **kwargs):
        super(CharacterActionsTab, self).__init__(*args, **kwargs)
        self.text = '*'

        self.content = BoxLayout(orientation='vertical')

        new_character = BoxLayout(orientation='vertical')
        character_prompt = BoxLayout(orientation='horizontal')
        character_prompt.add_widget(Label(text='Character Name', size_hint=(.2, 1)))
        character_name = DarkTextInput(font_size=FONT_XLARGE)
        character_prompt.add_widget(character_name)
        new_character.add_widget(character_prompt)
        create_character = Button(
            text='Add Character',
            on_press=lambda *args: parent.new_character(
                character_name.text.strip()))
        new_character.add_widget(create_character)

        self.content.add_widget(new_character)


class CharcterTab(TabbedPanelItem):

    def __init__(self, text, font_size=FONT_MEDIUM, *args, **kwargs):
        super(CharcterTab, self).__init__(font_size=font_size, *args, **kwargs)

        self.text = text

        # Non player characters
        content = BoxLayout(orientation='vertical')
        self.add_widget(content)

        # Character sheets
        self.character_sheets = TabbedPanel(
            do_default_tab=False,
            tab_width=200,
            tab_height=100)

        content.add_widget(self.character_sheets)
        self.character_sheets.add_widget(CharacterActionsTab(self))

    def load_characters(self):
        for character in session.query(Character).all():
            self.add_character(character)

    def add_character(self, character):
        character = session.merge(character)
        session.commit()
        self.character_sheets.add_widget(CharacterSheet(character))

    def new_character(self, name):
        self.add_character(Character(name=name))
