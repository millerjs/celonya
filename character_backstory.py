from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.rst import RstDocument

from kivy.uix.tabbedpanel import TabbedPanelItem
from editors import TextPromptPopup
from models import session
from constants import BLACK


class BackstoryTab(TabbedPanelItem):

    def __init__(self, character, *args, **kwargs):
        super(BackstoryTab, self).__init__(*args, **kwargs)

        character.backstory = character.backstory or ''
        self.character = character
        self.text = 'Notes'

        content = BoxLayout(orientation='vertical')

        rendered = RstDocument(
            text=character.backstory,
            background_color=BLACK,
            colors=dict(
                paragraph='eeeeee',
                background='000000',
                title='eeeeee',
                link='666666'),
        )

        def edit_content(value):
            self.character.backstory = value
            self.character = session.merge(character)
            session.commit()
            rendered.text = value

        def open_editor(_):
            editor = TextPromptPopup(
                'Edit backstory',
                callback=edit_content,
                text=rendered.text)
            editor.open()

        content.add_widget(rendered)

        content.add_widget(
            Button(text='Edit', size_hint=(1, .1), on_press=open_editor))

        self.add_widget(content)
