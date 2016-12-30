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

from editors import IntegerEditorPopup, TextPromptPopup
from value_table import ValueTable
from models import MonsterInstance, Monster, Race, session, Class
from util import DarkTextInput

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)
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


class MonsterDetails(BoxLayout):
    orientation = 'horizontal'
    size_hint = (1, .1)


class MonsterType(BoxLayout):
    orientation = 'horizontal'

    def __init__(self, monster, *args, **kwargs):
        self.monster = monster
        super(MonsterType, self).__init__(*args, **kwargs)

        spinner = Spinner(
            font_size=FONT_XLARGE,
            text=self.monster.monster_type or '',
            values=[monster_type.name for monster_type in session.query(Monster)])

        def view_details(_):
            details = Popup(size_hint=(.8, .8), title=self.monster.monster_type)
            monster_type = (session.query(Monster)
                    .filter(Monster.name == self.monster.monster_type)
                    .scalar())
            if monster_type:
                text = monster_type.details
            else:
                text = "Monster_Type '%s' not found" % self.monster.monster_type

            details.add_widget(RstDocument(text=text))
            details.open()

        spinner.bind(text=self.update)
        self.add_widget(spinner)
        self.add_widget(Button(
            text="Monster_Type details",
            font_size=FONT_XLARGE,
            on_press=view_details))

    def update(self, spinner, monster_type):
        self.monster.monster_type = monster_type
        self.monster = session.merge(self.monster)
        session.commit()


class StatTab(TabbedPanelItem):

    def __init__(self, monster, *args, **kwargs):
        super(StatTab, self).__init__(*args, **kwargs)
        self.text = 'Stats'
        self.monster = monster

        self.content = BoxLayout(orientation='vertical', size_hint=(1, 1))
        self.content.spacing = 10

        # General
        details = MonsterDetails()
        self.content.add_widget(details)
        details.add_widget(MonsterMonster_Type(self.monster))
        details.add_widget(MonsterClass(self.monster))

        # Modifiers
        modifiers = ValueTable(
            monster, monster.modifiers, prefix='+', size_hint=(1, .3))
        self.content.add_widget(modifiers)

        # Auxiliary values
        aux_values = ValueTable(
            monster, monster.aux_values, size_hint=(1, .3))
        self.content.add_widget(aux_values)


class MonsterSheet(TabbedPanelItem):

    def __init__(self, monster, font_size=FONT_MEDIUM, *args, **kwargs):
        super(MonsterSheet, self).__init__(
            font_size=font_size, *args, **kwargs)

        self.monster = monster
        self.text = monster.name

        details = TabbedPanel(
            do_default_tab=False,
            tab_width=350,
            tab_height=80)

        details.add_widget(StatTab(monster))
        details.add_widget(SpellTab())
        details.add_widget(MonsterItemsTab(monster))
        details.add_widget(BackstoryTab(monster))

        self.add_widget(details)


class SpellTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(SpellTab, self).__init__(*args, **kwargs)
        self.text = 'Spells'


class MonsterActionsTab(TabbedPanelItem):

    def __init__(self, parent, *args, **kwargs):
        super(MonsterActionsTab, self).__init__(*args, **kwargs)
        self.text = '*'

        self.content = BoxLayout(orientation='vertical')

        new_monster = BoxLayout(orientation='vertical')
        monster_prompt = BoxLayout(orientation='horizontal')
        monster_prompt.add_widget(Label(text='Monster Name', size_hint=(.2, 1)))
        monster_name = DarkTextInput(font_size=FONT_XLARGE)
        monster_prompt.add_widget(monster_name)
        new_monster.add_widget(monster_prompt)
        create_monster = Button(
            text='Add Monster',
            on_press=lambda *args: parent.new_monster(
                monster_name.text.strip()))
        new_monster.add_widget(create_monster)

        self.content.add_widget(new_monster)


class MonsterTab(TabbedPanelItem):

    def __init__(self, text, font_size=FONT_MEDIUM, *args, **kwargs):
        super(MonsterTab, self).__init__(font_size=font_size, *args, **kwargs)

        self.text = text

        # Non player monsters
        content = BoxLayout(orientation='vertical')
        self.add_widget(content)

        # Monster sheets
        self.monster_sheets = TabbedPanel(
            do_default_tab=False,
            tab_width=200,
            tab_height=100)

        content.add_widget(self.monster_sheets)
        self.load_monsters()

    def load_monsters(self):
        for monster in session.query(MonsterInstance).all():
            self.add_monster(monster)

    def add_monster(self, monster):
        monster = session.merge(monster)
        session.commit()
        self.monster_sheets.add_widget(MonsterSheet(monster))

    def new_monster(self, name):
        self.add_monster(Monster(name=name))
