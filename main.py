from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.listview import ListView
from kivy.uix.label import Label
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder

Builder.load_string("""

<Button1>:
    size: (150, 80)
    size_hint: (None, None)
    pos_hint: {'center_x':0.5, 'center_y':0.5}

<StatButton>:
    font_size: 30

<StatLabel>:
    font_size: 30

""")


class Character(object):

    def __init__(self, name, con, str_, wis, int_, cha):
        self.name = name
        self.con = con
        self.str_ = str_
        self.wis = wis
        self.int_ = int_
        self.cha = cha


class Button1(Button):  pass
class StatButton(Button):  pass
class StatLabel(Label):  pass


class CharacterSheet(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(CharacterSheet, self).__init__(*args, **kwargs)

        self.character = character
        self.text = character.name
        self.content = BoxLayout(orientation='vertical', size_hint=(1, .2))

        # Modifier labels
        modifier_labels = BoxLayout(orientation='horizontal', size_hint=(1, .3))
        modifier_labels.add_widget(StatLabel(text='con'))
        modifier_labels.add_widget(StatLabel(text='str'))
        modifier_labels.add_widget(StatLabel(text='wis'))
        modifier_labels.add_widget(StatLabel(text='int'))
        modifier_labels.add_widget(StatLabel(text='cha'))
        self.content.add_widget(modifier_labels)

        # Modifier values
        modifiers = BoxLayout(orientation='horizontal', size_hint=(1, .7))
        modifiers.add_widget(StatButton(text='+'+str(character.con)))
        modifiers.add_widget(StatButton(text='+'+str(character.str_)))
        modifiers.add_widget(StatButton(text='+'+str(character.wis)))
        modifiers.add_widget(StatButton(text='+'+str(character.int_)))
        modifiers.add_widget(StatButton(text='+'+str(character.cha)))
        self.content.add_widget(modifiers)

        self.modifiers = modifiers


def create_tab_npc():
    # Non player characters
    tab_npc = TabbedPanelItem(text='NPCs')
    tab_npc_content = BoxLayout(orientation='vertical')
    tab_npc.add_widget(tab_npc_content)

    # Character sheets
    character_sheets = TabbedPanel(
        do_default_tab=False,
        tab_width=200,
        tab_height=80)
    tab_npc_content.add_widget(character_sheets)

    character_sheets.add_widget(CharacterSheet(Character('Trym', 1, 2, 3, 4, 5)))

    return tab_npc


def create_tab_pc():
    # Non player characters
    tab_npc = TabbedPanelItem(text='PCs')
    tab_npc_content = BoxLayout(orientation='vertical')
    action_buttons = BoxLayout(orientation='horizontal', size_hint=(None, None))
    tab_npc.add_widget(tab_npc_content)
    tab_npc_content.add_widget(action_buttons)

    # Character sheets
    character_sheets = TabbedPanel(
        do_default_tab=False,
        tab_width=200,
        tab_height=80)
    tab_npc_content.add_widget(character_sheets)

    def add_character(instance):
        character_sheets.add_widget(TabbedPanelItem(text='PC'))

    action_buttons.add_widget(Button1(text='+ PC', on_press=add_character))

    return tab_npc


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        panel = TabbedPanel(
            do_default_tab=False,
            tab_width=200,
            tab_height=80)

        panel.add_widget(create_tab_npc())
        panel.add_widget(create_tab_pc())
        panel.add_widget(TabbedPanelItem(text='Spells'))
        self.add_widget(panel)


class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        return root


if __name__ == '__main__':
    MainApp().run()
