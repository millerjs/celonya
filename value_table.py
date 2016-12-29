from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from editors import IntegerEditorPopup
from models import session, Base

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)


class TableLabel(Label):
    font_size = FONT_LARGE


class TableButton(Button):
    font_size = FONT_XLARGE
    background_color = BLACK

    def __init__(self, target, attr, prefix='', suffix='', *args, **kwargs):
        super(TableButton, self).__init__(*args, **kwargs)

        self.prefix = prefix
        self.suffix = suffix
        self.target = target
        self.attr = attr
        self.value = getattr(self.target, self.attr)
        self.update_text()

    def set_value(self, value):
        setattr(self.target, self.attr, value)
        self.value = value

        if isinstance(self.target, Base):
            self.target = session.merge(self.target)
            session.commit()

        self.update_text()

    def update_text(self):
        # self.text = '%s:   %s%s%s' % (
        #     self.attr, self.prefix, self.value, self.suffix)
        self.text = '%s%s%s' % (self.prefix, self.value, self.suffix)

    def popup_editor(self):
        popup = IntegerEditorPopup(self.set_value, self.value)
        popup.open()


class ValueTable(BoxLayout):

    def __init__(self, target, attrs, prefix='', suffix='', *args, **kwargs):
        super(ValueTable, self).__init__(*args, **kwargs)
        content = BoxLayout(orientation='vertical', size_hint=(1, 1))
        columns = BoxLayout(orientation='horizontal')

        content.add_widget(columns)
        # content.add_widget(values)

        for attr in attrs:
            column = BoxLayout(orientation='vertical')
            column.add_widget(TableLabel(text=attr, size_hint=(1, .4)))
            value_button = TableButton(target, attr, prefix, suffix)
            value_button.on_press = value_button.popup_editor
            column.add_widget(value_button)
            columns.add_widget(column)

        self.add_widget(content)
