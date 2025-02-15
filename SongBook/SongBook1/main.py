from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helpers import songname_helper
from helpers import songnum_helper
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineIconListItem, ThreeLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget


class SongBook(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            image= ImageLeftWidget(source="piano.png")
            items = ThreeLineAvatarIconListItem(text='Item ' + str(i), secondary_text='G maj Scale')
            items.add_widget(image)
            list_view.add_widget(items)

        self.songname = Builder.load_string(songname_helper)
        self.songnum = Builder.load_string(songnum_helper)
        btn_flat = MDRectangleFlatButton(text='Songs Here', pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                         on_release=self.show_data)
        icon_btn = MDIconButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        icon_btn1 = MDFloatingActionButton(icon='language-python', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        screen.add_widget(scroll)
        screen.add_widget(self.songname)  # Added back the songname widget
        screen.add_widget(self.songnum)
        screen.add_widget(icon_btn)
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn1)
        return screen

    def show_data(self, obj):
        if self.songname.text is not "":
            check_string = self.songname.text + ' does not exist'
        else:
            check_string = "Please enter a valid Song"

        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Song Name Check', text=check_string, size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


SongBook().run()
