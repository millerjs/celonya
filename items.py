
from kivy.uix.tabbedpanel import TabbedPanelItem


from constants import (
    FONT_SMALL, FONT_MEDIUM, FONT_LARGE, FONT_XLARGE, FONT_XXLARGE, BLACK,
    GREY, WHITE
)



class ItemTab(TabbedPanelItem):

    def __init__(self, *args, **kwargs):
        super(ItemTab, self).__init__(*args, **kwargs)
        self.text = 'Items'
