from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from players_tab import CharcterTab
from models import Character, NPC
from constants import FONT_MEDIUM
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


import os
from os.path import isfile, join

SOUNDS_DIR = 'sounds'


class SoundCategoryTab(TabbedPanelItem):

    def __init__(self, directory, font_size=FONT_MEDIUM, *args, **kwargs):
        super(SoundCategoryTab, self).__init__(
            font_size=font_size, *args, **kwargs)

        self.directory = directory
        self.text = os.path.basename(directory)

        self.choices = GridLayout(cols=10, spacing=10, size_hint_y=None)
        self.choices.bind(minimum_height=self.choices.setter('height'))
        choices_root = ScrollView()
        choices_root.add_widget(self.choices)


        self.content = BoxLayout(orientation='vertical')
        self.content.add_widget(Button(
            text='RELOAD',
            on_press=lambda button: self.load_sounds(),
            size_hint=(1, .1),
        ))
        self.content.add_widget(choices_root)

        self.load_sounds()

    def load_sounds(self):
        self.choices.clear_widgets()

        sounds =  list(sorted([
            f for f in os.listdir(self.directory)
            if isfile(join(self.directory, f))
        ]))

        def play_sound(button):
            if not button.sound:
                print("Unable to play sound %s" % button.text)

            if button.sound_state == 'stopped':
                button.sound.play()
                button.text += ' * '

            elif button.sound_state == 'playing':
                button.sound_state = 'looping'
                button.sound.loop = True
                button.text = button.text[:-3]
                button.text += ' ! '

            elif button.sound_state == 'looping':
                button.sound.stop()

        for sound in sounds:
            btn = Button(
                text='.'.join(sound.split('.')[:-1]),
                size_hint_y=None,
                height=100,
                on_press=play_sound)

            btn.sound_state = 'stopped'

            def on_play(*args, button=btn):
                button.sound_state = 'playing'

            def on_stop(*args, button=btn):
                button.sound_state = 'stopped'
                button.text = button.text[:-3]

            btn.sound = SoundLoader.load(join(self.directory, sound))
            if btn.sound:
                btn.sound.on_play = on_play
                btn.sound.on_stop = on_stop

            self.choices.add_widget(btn)




class SoundsTab(TabbedPanelItem):

    def __init__(self, text, font_size=FONT_MEDIUM, *args, **kwargs):
        super(SoundsTab, self).__init__(font_size=font_size, *args, **kwargs)

        self.text = text

        # Non player characters
        content = BoxLayout(orientation='vertical')
        self.add_widget(content)

        category_tabs = TabbedPanel(do_default_tab=False, tab_width=200, tab_height=80)

        categories = {x[0] for x in os.walk(SOUNDS_DIR)} - {SOUNDS_DIR}
        print(categories)
        for category in categories:
            category_tabs.add_widget(SoundCategoryTab(category))

        content.add_widget(category_tabs)
