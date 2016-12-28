from collections import OrderedDict
from random import randint

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

class Character(object):

    def __init__(self, name):
        self.name = name
        self.modifiers = OrderedDict((
            ('str', randint(0, 3)),
            ('con', randint(0, 3)),
            ('int', randint(0, 3)),
            ('wis', randint(0, 3)),
            ('cha', randint(0, 3)),
            ('dex', randint(0, 3)),
        ))

        self.aux_values = OrderedDict((
            ('level', 1),
            ('AC', randint(10, 14)),
            ('proficiency', 2),
            ('HP', randint(8, 11)),
            ('MHP', randint(8, 11)),
        ))


class Button1(Button):
    size = (150, 80)
    size_hint = (None, None)
    pos_hint = {'center_x': 0.5, 'center_y': 0.5}


class TableLabel(Label):
    font_size = 30


class ValueEditorSlider(Slider):

    def __init__(self, on_update, step=1, *args, **kwargs):
        self.on_update = on_update
        super(ValueEditorSlider, self).__init__(step=step, *args, **kwargs)

    def on_touch_move(self, touch):
        super(ValueEditorSlider, self).on_touch_move(touch)
        self.on_update(self.value)

    def on_touch_down(self, touch):
        super(ValueEditorSlider, self).on_touch_down(touch)
        self.on_update(self.value)


class TableButton(Button):
    font_size = 30

    def __init__(self, value, prefix='', suffix='', min_val=-20,
                 max_val=20, *args, **kwargs):
        super(TableButton, self).__init__(*args, **kwargs)

        self.prefix = prefix
        self.suffix = suffix
        self.min_val = min_val
        self.max_val = max_val
        self.value = value
        self.update_text()

    def set_value(self, value):
        self.value = value
        self.update_text()

    def update_text(self):
        self.text = self.prefix + str(self.value) + self.suffix

    def popup_editor(self):
        content = BoxLayout(orientation='vertical')
        popup = Popup(title='Edit value', content=content, size_hint=(.5, .5))

        slider_label = Label(text='%d' % self.value, font_size=40)

        def update_label(value):
            slider_label.text = '%d' % value

        slider = ValueEditorSlider(
            on_update=update_label,
            min=self.min_val,
            max=self.max_val,
            value=int(self.value))

        def save(_):
            self.set_value(slider.value)
            popup.dismiss()

        save_btn = Button(text='save', font_size=20, on_press=save)

        content.add_widget(slider_label)
        content.add_widget(slider)
        content.add_widget(save_btn)

        popup.open()


class ValueTable(BoxLayout):

    def __init__(self, key_values, prefix='', suffix='', *args, **kwargs):
        super(ValueTable, self).__init__(*args, **kwargs)
        content = BoxLayout(orientation='vertical', size_hint=(1, 1))
        labels = BoxLayout(orientation='horizontal', size_hint=(1, .3))
        values = BoxLayout(orientation='horizontal', size_hint=(1, .7))

        content.add_widget(labels)
        content.add_widget(values)

        for key, value in key_values.items():
            labels.add_widget(TableLabel(text=key))
            value_button = TableButton(value, prefix, suffix)
            value_button.on_press = value_button.popup_editor
            values.add_widget(value_button)

        values.spacing = 20
        values.padding = 10

        self.add_widget(content)


class CharacterSheet(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(CharacterSheet, self).__init__(*args, **kwargs)
        self.character = character
        self.text = character.name

        details = TabbedPanel(
            do_default_tab=False,
            rows=2,
            tab_width=300,
            tab_height=80)

        details.add_widget(StatTab(character))
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

        # Auxiliary values
        aux_values = ValueTable(self.character.modifiers, prefix='+', size_hint=(1, .3))
        self.content.add_widget(aux_values)

        # Modifiers
        modifiers = ValueTable(self.character.aux_values, size_hint=(1, .3))
        self.content.add_widget(modifiers)


class SpellTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(SpellTab, self).__init__(*args, **kwargs)
        self.text = 'Spells'


class ItemTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(ItemTab, self).__init__(*args, **kwargs)
        self.text = 'Items'


class BackstoryTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(BackstoryTab, self).__init__(*args, **kwargs)
        self.text = 'Backstory'


class CharcterTab(TabbedPanelItem):

    def __init__(self, text, *args, **kwargs):
        super(CharcterTab, self).__init__(*args, **kwargs)

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

    def add_character(self, char_sheet):
        self.character_sheets.add_widget(char_sheet)


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        panel = TabbedPanel(
            do_default_tab=False,
            rows=2,
            tab_width=300,
            tab_height=100)

        pc_tab = CharcterTab("PCs")

        pc_tab.add_character(CharacterSheet(Character('Trym Tosscobble')))
        pc_tab.add_character(CharacterSheet(Character('Aden Iolas')))
        pc_tab.add_character(CharacterSheet(Character('Mara Salchil')))
        pc_tab.add_character(CharacterSheet(Character('Shandarah Smith')))
        pc_tab.add_character(CharacterSheet(Character('Mud')))
        pc_tab.add_character(CharacterSheet(Character('Peaches')))

        npc_tab = CharcterTab("NPCs")

        panel.add_widget(pc_tab)
        panel.add_widget(npc_tab)
        self.add_widget(panel)


class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        return root


if __name__ == '__main__':
    MainApp().run()