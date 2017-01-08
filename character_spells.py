
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanelItem

from models import Spell
from models import session

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

from models import SpellbookEntry


from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from util import DetailPopup

class SpellTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(SpellTab, self).__init__(*args, **kwargs)
        self.text = 'Spells'


class SpellbookEntry(BoxLayout):
    orientation = 'horizontal'

    def __init__(self, spells_tab, inventory_entry, *args, **kwargs):
        super(SpellbookEntry, self).__init__(*args, **kwargs)

        self.inventory_entry = inventory_entry
        spell = (session.query(Spell)
                 .filter(Spell.name == inventory_entry.spell)
                 .scalar())

        attrs = ['name', 'casting_time', 'components', 'duration',
                 'level', 'range', 'school']

        for attr in attrs:
            self.add_widget(Label(text=getattr(spell, attr) or ''))

        def show_details(instance):
            text = '\n\n'.join([
                "%s\n~~~~\n%s" % (attr, getattr(spell, attr) or '')
                for attr in ['description'] + attrs
            ])
            DetailPopup(text=text).open()

        self.add_widget(Button(text='details', on_press=show_details))

        def remove_spell(btn):
            session.delete(session.merge(self.inventory_entry))
            spells_tab.set_spells()

        self.add_widget(Button(text='remove', on_press=remove_spell))


class SpellHeader(BoxLayout):
    orientation = 'horizontal'
    size_hint = (1, .1)

    def __init__(self, *args, **kwargs):
        super(SpellHeader, self).__init__(*args, **kwargs)

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



class AddSpellPopup(Popup):
    def __init__(self, spell_tab, size_hint=(.8, .8), *args, **kwargs):
        content = BoxLayout(orientation='vertical')
        character = spell_tab.character
        self.title = 'Add spell for %s' % character.name
        spells = list(sorted(spell.name for spell in session.query(Spell).all()))

        choices = GridLayout(cols=5, spacing=10, size_hint_y=None)
        choices.bind(minimum_height=choices.setter('height'))

        def add_spell(btn):
            session.merge(SpellbookEntry(character=character.name, spell=btn.text))
            session.commit()
            self.dismiss()
            spell_tab.set_spells()

        for spell in spells:
            btn = Button(text=spell, size_hint_y=None, height=40, on_press=add_spell)
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

        super(AddSpellPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)


class CharacterSpellsTab(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(CharacterSpellsTab, self).__init__(*args, **kwargs)
        self.character = character
        self.text = 'Spells'
        self.content = BoxLayout(orientation='vertical')
        self.spacing = 10
        self.spells = ScrollView(size=(Window.width, Window.height))

        self.layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.spells.add_widget(self.layout)

        def add_spell(button):
            popup = AddSpellPopup(self)
            popup.open()

        buttons = BoxLayout(orientation='horizontal', size_hint=(1, .1))
        buttons.add_widget(Button(text='Add spell', on_press=add_spell))
        self.content.add_widget(buttons)
        self.content.add_widget(SpellHeader())
        self.content.add_widget(self.spells)

        self.set_spells()

    def set_spells(self):
        self.layout.clear_widgets()

        spells = (session.query(SpellbookEntry)
                 .filter(SpellBookEntry.character == self.character.name)
                 .all())

        for spell in spells:
            self.layout.add_widget(
                SpellbookEntry(self, spell, height=60, size_hint_y=None))
        self.layout.bind(minimum_height=self.layout.setter('height'))
