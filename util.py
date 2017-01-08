from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors.emacs import EmacsBehavior
from kivy.uix.rst import RstDocument
from constants import BLACK, WHITE


class ErrorPopup(Popup):
    def __init__(self, exception, size_hint=(.5, .5), *args, **kwargs):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=str(exception)))
        content.add_widget(Button(text='Continue', on_press=self.dismiss))
        super(ErrorPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)
        self.open()


class DetailPopup(Popup):
    def __init__(self, text, title='Details', size_hint=(.8, .8), *args, **kwargs):
        content = BoxLayout(orientation='vertical')
        content.add_widget(RstDocument(text=text))
        self.title = title
        content.add_widget(Button(
            text='Continue',
            on_press=self.dismiss,
            size_hint=(1, .2)))
        super(DetailPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)


class EmacsTextInput(TextInput, EmacsBehavior):
    background_color = BLACK
    foreground_color = WHITE


class DarkTextInput(EmacsTextInput):
    background_color = BLACK
    foreground_color = WHITE
