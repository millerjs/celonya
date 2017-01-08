
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.rst import RstDocument

from editors import TextPromptPopup
from models import Encounter
from models import session

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

class EncountersTab(TabbedPanelItem):

    def __init__(self, font_size=FONT_MEDIUM, *args, **kwargs):
        super(EncountersTab, self).__init__(font_size=font_size, *args, **kwargs)

        self.text = 'Encounters'

        content = BoxLayout(orientation='vertical')

        self.encounter = session.query(Encounter).first()

        rendered = RstDocument(
            text=self.encounter.description,
            background_color=BLACK,
            colors=dict(
                paragraph='eeeeee',
                background='000000',
                title='eeeeee',
                link='666666'),
        )

        def edit_content(value):
            self.encounter.description = value
            self.encounter = session.merge(self.encounter)
            session.commit()
            rendered.text = value

        def open_editor(instance):
            editor = TextPromptPopup(
                'Edit encounter',
                callback=edit_content,
                text=rendered.text)
            editor.open()

        content.add_widget(rendered)

        content.add_widget(
            Button(text='Edit', size_hint=(1, .1), on_press=open_editor))

        self.add_widget(content)
