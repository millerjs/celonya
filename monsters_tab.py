
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView

from value_table import ValueTable
from models import Monster
from models import MonsterInstance
from models import session

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.rst import RstDocument

from value_table import ValueTable
from models import session
import add_monster

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
            monster_type = self.monster.monster_type or ''
            details = Popup(size_hint=(.8, .8), title=monster_type)
            monster_type = (session.query(Monster)
                            .filter(Monster.name == monster_type)
                            .scalar())
            if monster_type:
                text = monster_type.get_details()
            else:
                text = "Monster_Type '%s' not found" % monster_type

            details.add_widget(RstDocument(text=text))
            details.open()

        spinner.bind(text=self.update)
        self.add_widget(spinner)
        self.add_widget(Button(
            text="Details",
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
        details.add_widget(MonsterType(self.monster))

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

        self.add_widget(details)


class SpellTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(SpellTab, self).__init__(*args, **kwargs)
        self.text = 'Spells'



class AddMonsterPopup(Popup):
    def __init__(self, parent, size_hint=(.8, .8), *args, **kwargs):
        content = BoxLayout(orientation='vertical')
        self.title = 'Add monster'

        name_input = TextInput(text='', size_hint=(1, .1), font_size=FONT_MEDIUM)
        type_input = TextInput(text='', size_hint=(1, .1), font_size=FONT_MEDIUM)

        items = list(sorted(item.name for item in session.query(Monster).all()))

        choices = GridLayout(cols=5, spacing=10, size_hint_y=None)
        choices.bind(minimum_height=choices.setter('height'))

        def save(monster_type):
            add_monster.add(name_input.text, monster_type)
            parent.load_monsters()

            self.dismiss()

        def add_item(btn):
            save(btn.text)

        def add_manually(_):
            save(type_input.text)

        for item in items:
            btn = Button(text=item, size_hint_y=None, height=40, on_press=add_item)
            choices.add_widget(btn)

        content.add_widget(name_input)
        content.add_widget(type_input)

        choices_root = ScrollView()
        choices_root.add_widget(choices)
        content.add_widget(choices_root)

        buttons = BoxLayout(orientation='horizontal', size_hint=(1, .2))
        content.add_widget(buttons)
        buttons.add_widget(Button(
            text='Cancel',
            on_press=self.dismiss,
        ))
        buttons.add_widget(Button(
            text='Add',
            on_press=add_manually,
        ))

        super(AddMonsterPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)


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
            tab_width=150,
            tab_height=100)

        def add_monster(button):
            popup = AddMonsterPopup(self)
            popup.open()

        buttons = BoxLayout(orientation='horizontal', size_hint=(1, .1))

        new_monster = Button(text='+', on_press=add_monster)
        refresh = Button(text='refresh', on_press=lambda x: self.load_monsters())
        buttons.add_widget(new_monster)
        buttons.add_widget(refresh)

        content.add_widget(buttons)
        content.add_widget(self.monster_sheets)
        self.load_monsters()

    def load_monsters(self):
        # existing = {panel.text for panel in self.monster_sheets.}
        monsters = sorted(session.query(MonsterInstance).all(),
                          key=lambda monster: monster.name)
        for monster in monsters:
            self.add_monster(monster)

    def add_monster(self, monster):
        monster = session.merge(monster)
        session.commit()
        self.monster_sheets.add_widget(MonsterSheet(monster))

    def new_monster(self, name):
        self.add_monster(Monster(name=name))
