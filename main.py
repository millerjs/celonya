from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel

from players_tab import CharcterTab
from models import Character, NPC


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        panel = TabbedPanel(do_default_tab=False, tab_width=400, tab_height=100)

        pc_tab = CharcterTab("PCs")
        pc_tab.load_characters(Character)

        npc_tab = CharcterTab("NPCs")
        npc_tab.load_characters(NPC)

        panel.add_widget(pc_tab)
        panel.add_widget(npc_tab)
        self.add_widget(panel)

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        return root


if __name__ == '__main__':
    MainApp().run()
