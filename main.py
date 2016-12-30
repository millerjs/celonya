from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from monsters_tab import MonsterTab
from players_tab import CharcterTab
from sounds_tab import SoundsTab
from encounters_tab import EncountersTab

from models import Character, NPC
from constants import FONT_MEDIUM
from kivy.uix.boxlayout import BoxLayout


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        panel = TabbedPanel(do_default_tab=False, tab_width=300, tab_height=100)

        pc_tab = CharcterTab("PCs")
        pc_tab.load_characters(Character)

        npc_tab = CharcterTab("NPCs")
        npc_tab.load_characters(NPC)

        # monster_tab = MonsterTab("Monsters")

        sounds_tab = SoundsTab("Sounds")
        encounters_tab = EncountersTab()

        panel.add_widget(pc_tab)
        panel.add_widget(npc_tab)
        panel.add_widget(sounds_tab)
        panel.add_widget(monster_tab)
        panel.add_widget(encounters_tab)

        self.add_widget(panel)

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        return root


if __name__ == '__main__':
    MainApp().run()
