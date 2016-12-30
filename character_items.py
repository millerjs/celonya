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
from models import Character, Race, session, Class, Item
from util import DarkTextInput

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

from models import InventoryItem
from kivy.uix.listview import ListView, ListItemButton, CompositeListItem, ListItemLabel
from kivy.adapters.dictadapter import DictAdapter


from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

from util import DetailPopup


class ItemEntry(BoxLayout):
    orientation = 'horizontal'

    def __init__(self, items_tab, inventory_entry, *args, **kwargs):
        super(ItemEntry, self).__init__(*args, **kwargs)

        self.inventory_entry = inventory_entry
        item = (session.query(Item)
                .filter(Item.name == inventory_entry.item)
                .scalar())

        attrs = ['name', 'category', 'damage', 'ac', 'weight',
                 'cost', 'strength', 'stealth']

        for attr in attrs:
            self.add_widget(Label(text=getattr(item, attr) or ''))

        def show_details(instance):
            text = '\n\n'.join([
                "%s\n~~~~\n%s" % (attr, getattr(item, attr) or '')
                for attr in ['properties', 'description'] + attrs
            ])
            DetailPopup(text=text).open()

        self.add_widget(Button(text='details', on_press=show_details))

        def remove_item(btn):
            session.delete(session.merge(self.inventory_entry))
            items_tab.set_items()

        self.add_widget(Button(text='remove', on_press=remove_item))


class ItemHeader(BoxLayout):
    orientation = 'horizontal'
    size_hint = (1, .1)

    def __init__(self, *args, **kwargs):
        super(ItemHeader, self).__init__(*args, **kwargs)

        self.add_widget(Label(text='name', font_size=FONT_LARGE))
        self.add_widget(Label(text='category', font_size=FONT_LARGE))
        self.add_widget(Label(text='damage', font_size=FONT_LARGE))
        self.add_widget(Label(text='ac', font_size=FONT_LARGE))
        self.add_widget(Label(text='weight', font_size=FONT_LARGE))
        self.add_widget(Label(text='cost', font_size=FONT_LARGE))
        self.add_widget(Label(text='strength', font_size=FONT_LARGE))
        self.add_widget(Label(text='stealth', font_size=FONT_LARGE))

        self.add_widget(Label(text='')) # description
        self.add_widget(Label(text='')) # remove



class AddItemPopup(Popup):
    def __init__(self, item_tab, size_hint=(.8, .8), *args, **kwargs):
        content = BoxLayout(orientation='vertical')
        character = item_tab.character
        self.title = 'Add item for %s' % character.name
        items = list(sorted(item.name for item in session.query(Item).all()))

        choices = GridLayout(cols=5, spacing=10, size_hint_y=None)
        choices.bind(minimum_height=choices.setter('height'))

        def add_item(btn):
            session.merge(InventoryItem(character=character.name, item=btn.text))
            session.commit()
            self.dismiss()
            item_tab.set_items()

        for item in items:
            btn = Button(text=item, size_hint_y=None, height=40, on_press=add_item)
            choices.add_widget(btn)

        choices_root = ScrollView()
        choices_root.add_widget(choices)
        content.add_widget(choices_root)

        buttons = BoxLayout(orientation='horizontal', size_hint=(1, .2))
        content.add_widget(buttons)
        buttons.add_widget(Button(
            text='Cancel',
            on_press=self.dismiss,
        ))

        super(AddItemPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)


class CharacterItemsTab(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(CharacterItemsTab, self).__init__(*args, **kwargs)
        self.character = character
        self.text = 'Items'
        self.content = BoxLayout(orientation='vertical')
        self.spacing = 10
        self.items = ScrollView(size=(Window.width, Window.height))

        self.layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.items.add_widget(self.layout)

        def add_item(button):
            popup = AddItemPopup(self)
            popup.open()

        buttons = BoxLayout(orientation='horizontal', size_hint=(1, .1))
        buttons.add_widget(Button(text='Add item', on_press=add_item))
        self.content.add_widget(buttons)
        self.content.add_widget(ItemHeader())
        self.content.add_widget(self.items)

        self.set_items()

    def set_items(self):
        self.layout.clear_widgets()

        items = (session.query(InventoryItem)
                 .filter(InventoryItem.character == self.character.name)
                 .all())

        for item in items:
            self.layout.add_widget(ItemEntry(self, item, height=60, size_hint_y=None))
        self.layout.bind(minimum_height=self.layout.setter('height'))
