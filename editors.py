from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)

class TextPromptPopup(Popup):

    def __init__(self, prompt, callback, size_hint=(.5, .5), *args, **kwargs):
        self.callback = callback
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=str(prompt)))
        self.text_input = TextInput()
        content.add_widget(self.text_input)

        content.add_widget(Button(text='Continue', on_press=self.dismiss))
        super(TextPromptPopup, self).__init__(
            content=content, size_hint=size_hint, *args, **kwargs)

    def dismiss(self, instance):
        super(TextPromptPopup, self).dismiss()
        self.callback(self.text_input.text)



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


class ValueEditorPopup(Popup):
    def __init__(self, set_value, value, min_val=None, max_val=None,
                 size_hint=(.6, .5), *args, **kwargs):

        min_val = min_val if min_val is not None else value - 20
        max_val = max_val if max_val is not None else value + 20

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
        label_kwargs = dict(font_size=FONT_MEDIUM, size_hint=(.2, 1))

        # Boundary buttons
        min_btn = Button(text=str(min_val), **label_kwargs)
        max_btn = Button(text=str(max_val), **label_kwargs)

        def update_min():
            slider.min = (slider.min or -1) * 2
            min_btn.text = str(slider.min)

        def update_max():
            slider.max = (slider.max or -1) * 2
            max_btn.text = str(slider.max)

        min_btn.on_press = update_min
        max_btn.on_press = update_max

        # Add widgets
        slider_box.add_widget(min_btn)
        slider_box.add_widget(slider)
        slider_box.add_widget(max_btn)

        content.add_widget(slider_label)
        content.add_widget(Label(text='Absolute', size_hint=(1, .2)))
        content.add_widget(slider_box)
        content.add_widget(save_btn)

        super(ValueEditorPopup, self).__init__(
            title='Edit value', content=content, size_hint=size_hint,
            *args, **kwargs)