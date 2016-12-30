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
from models import Character, Race, session, Class, Encounter
from util import DarkTextInput

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

class EncountersTab(TabbedPanelItem):

    def __init__(self, font_size=FONT_MEDIUM, *args, **kwargs):
        super(EncountersTab, self).__init__(font_size=font_size, *args, **kwargs)

        self.text = 'Encounters'

        content = BoxLayout(orientation='vertical')

        self.encounter = session.query(Encounter).first()

        rendered = RstDocument(
            text=self.encounter.description,
            background_color=BLACK,
            colors=dict(
                paragraph='eeeeee',
                background='000000',
                title='eeeeee',
                link='666666'),
        )

        def edit_content(value):
            self.encounter.description = value
            self.encounter = session.merge(self.encounter)
            session.commit()
            rendered.text = value

        def open_editor(instance):
            editor = TextPromptPopup(
                'Edit encounter',
                callback=edit_content,
                text=rendered.text)
            editor.open()

        content.add_widget(rendered)

        content.add_widget(
            Button(text='Edit', size_hint=(1, .1), on_press=open_editor))

        self.add_widget(content)
