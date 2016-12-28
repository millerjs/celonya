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


FONT_SMALL = 10
FONT_MEDIUM = 20
FONT_LARGE = 30
FONT_XLARGE = 40
FONT_XXLARGE = 60

BLACK = (0, 0, 0, 1)
GREY = (0.175, 0.175, 0.175, 1)
WHITE = (1, 1, 1, 1)


class Character(object):

    modifiers = ['str', 'con', 'int', 'wis', 'cha', 'dex']
    aux_values = ['level', 'AC', 'proiciency', 'HP', 'MHP']

    def __init__(self, name, **kwargs):
        self.name = name
        for key in self.modifiers + self.aux_values:
            setattr(self, key, kwargs.get(key, 0))

class Button1(Button):
    size = (150, 80)
    size_hint = (None, None)
    pos_hint = {'center_x': 0.5, 'center_y': 0.5}


class TableLabel(Label):
    font_size = FONT_LARGE


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


class ValueEditorText(TextInput):
    def __init__(self, font_size=FONT_XXLARGE, multiline=False,
                 background_color=GREY, foreground_color=WHITE,
                 *args, **kwargs):

        super(ValueEditorText, self).__init__(
            font_size=font_size,
            multiline=multiline,
            background_color=background_color,
            foreground_color=foreground_color,
            *args, **kwargs)

    def insert_text(self, substring, from_undo=False):
        try:
            text = str(int(substring))
        except ValueError:
            text = ''

        return super(ValueEditorText, self).insert_text(
            text, from_undo=from_undo)


class ErrorPopup(Popup):
    def __init__(self, exception, size_hint=(.5, .5), *args, **kwargs):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=str(exception)))
        content.add_widget(Button(text='Continue', on_press=self.dismiss))
        super(ErrorPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)
        self.open()


class ValueEditorPopup(Popup):
    def __init__(self, set_value, value, min_val=None, max_val=None,
                 size_hint=(.6, .5), *args, **kwargs):

        min_val = min_val if min_val is not None else val - 20
        max_val = max_val if max_val is not None else val + 20

        content = BoxLayout(orientation='vertical')
        slider_label = ValueEditorText(
            text='%d' % value,
            size_hint=(.2, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})


        def update_label(value):
            slider_label.text = '%d' % value

        slider = ValueEditorSlider(
            on_update=update_label, min=min_val, max=max_val, value=int(value))

        def save(_):
            try:
                set_value(int(slider_label.text))
                self.dismiss()
            except Exception as exception:
                ErrorPopup(exception)

        slider_label.bind(on_text_validation=save)
        save_btn = Button(text='save', font_size=20, on_press=save)

        slider_box = BoxLayout()
        label_kwargs = dict(font_size=FONT_MEDIUM, size_hint=(.05, 1))
        slider_box.add_widget(Label(text=str(min_val), **label_kwargs))
        slider_box.add_widget(slider)
        slider_box.add_widget(Label(text=str(max_val), **label_kwargs))

        content.add_widget(slider_label)
        content.add_widget(slider_box)
        content.add_widget(save_btn)

        super(ValueEditorPopup, self).__init__(
            title='Edit value', content=content, size_hint=size_hint,
            *args, **kwargs)


class TableButton(Button):
    font_size = FONT_LARGE

    def __init__(self, value, prefix='', suffix='', min_val=-5,
                 max_val=30, *args, **kwargs):
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
        popup = ValueEditorPopup(
            self.set_value, self.value, self.min_val, self.max_val)
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
        aux_dict = {key: getattr(character, key) for key in character.aux_values}
        aux_values = ValueTable(aux_dict, prefix='+', size_hint=(1, .3))
        self.content.add_widget(aux_values)

        # Modifiers
        mod_dict = {key: getattr(character, key) for key in character.modifiers}
        modifiers = ValueTable(mod_dict, size_hint=(1, .3))
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
