from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window

Window.size = (360, 640)  # Set default window size for better visualization

# Chord transposition helper
CHORDS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def transpose_chord(chord, steps):
    if chord in CHORDS:
        return CHORDS[(CHORDS.index(chord) + steps) % len(CHORDS)]
    return chord

def transpose_line(chord_line, steps):
    return " ".join(
        [transpose_chord(chord, steps) if chord in CHORDS else chord for chord in chord_line.split()]
    )

SONGS = {
    "Hymns": {
        "All Hail the Power of Jesus' Name": {
            "lyrics": [
                "All hail the power of Jesus' name!",
                "Let angels prostrate fall;",
                "Bring forth the royal diadem,",
                "And crown Him Lord of all!",
            ],
            "chords": [
                "G D G",
                "C G D G",
                "G D G C",
                "G D G",
            ],
        },
        "Amazing Grace": {
            "lyrics": [
                "Amazing grace! How sweet the sound",
                "That saved a wretch like me.",
                "I once was lost, but now am found;",
                "Was blind, but now I see.",
            ],
            "chords": [
                "G C G D",
                "G C G",
                "G C G D",
                "G C G",
            ],
        },
    },
    "Choruses": {
        "Here I Am to Worship": {
            "lyrics": [
                "Light of the world,",
                "You stepped down into darkness,",
                "Opened my eyes, let me see",
                "Beauty that made this heart adore You",
            ],
            "chords": [
                "G D Em C",
                "G D Em C",
                "G D Em C",
                "D C G",
            ],
        },
    },
}

KV = """
ScreenManager:
    HomeScreen:
    MainScreen:
    SongScreen:

<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.1, 0.1, 1
        MDTopAppBar:
            title: "English Song Book"
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            padding: 20
            spacing: 40
            MDRaisedButton:
                text: "Hymns"
                on_release: app.show_category_songs("Hymns")
                size_hint: 0.9, None
                height: "64dp"
                pos_hint: {"center_x": 0.5}
            MDRaisedButton:
                text: "Choruses"
                on_release: app.show_category_songs("Choruses")
                size_hint: 0.9, None
                height: "64dp"
                pos_hint: {"center_x": 0.5}

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.1, 0.1, 1
        MDTopAppBar:
            title: "English Song Book"
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            left_action_items: [["arrow-left", lambda x: app.show_home_screen()]]
        MDTextField:
            id: search_bar
            hint_text: "Search Songs"
            mode: "rectangle"
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}
            on_text: app.filter_song_list(self.text)
        MDScrollView:
            MDList:
                id: song_list

<SongScreen>:
    name: "song"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.1, 0.1, 1
        MDTopAppBar:
            title: "Song Details"
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            left_action_items: [["arrow-left", lambda x: app.show_main_screen()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: 10
                spacing: 10
                size_hint_y: None
                height: self.minimum_height
                MDLabel:
                    id: song_title
                    text: ""
                    font_style: "H5"
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_color: 1, 0.75, 0, 1
                MDBoxLayout:
                    id: song_details
                    orientation: "vertical"
                    spacing: 5
                    size_hint_y: None
                    height: self.minimum_height
                MDBoxLayout:
                    size_hint_y: None
                    height: 50
                    padding: 10
                    spacing: 10
                    MDRaisedButton:
                        text: "Transpose -1"
                        on_release: app.transpose_chords(-1)
                    MDRaisedButton:
                        text: "Transpose +1"
                        on_release: app.transpose_chords(1)
"""

class HomeScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class SongScreen(Screen):
    pass

class SongbookApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.root = Builder.load_string(KV)
        return self.root

    def show_category_songs(self, category):
        song_list = self.root.get_screen("main").ids.song_list
        song_list.clear_widgets()
        for song_name in SONGS[category]:
            item = OneLineListItem(
                text=song_name,
                on_release=self.show_song_details,
                text_color=(1, 0.75, 0, 1),
            )
            song_list.add_widget(item)
        self.root.current = "main"

    def show_song_details(self, instance):
        for category in SONGS:
            if instance.text in SONGS[category]:
                self.current_song_name = instance.text
                song_data = SONGS[category][self.current_song_name]
                self.original_chords = song_data["chords"]
                self.transposed_chords = self.original_chords[:]
                self.update_song_details(song_data["lyrics"], self.original_chords, self.transposed_chords)
                self.root.current = "song"
                break

    def update_song_details(self, lyrics, original_chords, transposed_chords):
        song_screen = self.root.get_screen("song")
        song_screen.ids.song_title.text = self.current_song_name
        song_details = song_screen.ids.song_details
        song_details.clear_widgets()
        for o_chord, t_chord, lyric in zip(original_chords, transposed_chords, lyrics):
            line_layout = MDBoxLayout(orientation="vertical", size_hint_y=None, height=60, spacing=5)
            original_label = MDLabel(text=o_chord, halign="center", text_color=(0.6, 0.6, 0.6, 1))  # Gray text
            transposed_label = MDLabel(text=t_chord, halign="center", text_color=(1, 0.75, 0, 1))  # Amber text
            lyric_label = MDLabel(text=lyric, halign="center", text_color=(1, 1, 1, 1))
            line_layout.add_widget(original_label)
            line_layout.add_widget(transposed_label)
            line_layout.add_widget(lyric_label)
            song_details.add_widget(line_layout)

    def transpose_chords(self, steps):
        self.transposed_chords = [transpose_line(line, steps) for line in self.transposed_chords]
        song_data = SONGS[next(category for category in SONGS if self.current_song_name in SONGS[category])][self.current_song_name]
        self.update_song_details(song_data["lyrics"], self.original_chords, self.transposed_chords)

    def show_home_screen(self):
        self.root.current = "home"

    def show_main_screen(self):
        self.root.current = "main"

    def filter_song_list(self, search_text):
        search_text = search_text.lower()
        song_list = self.root.get_screen("main").ids.song_list
        song_list.clear_widgets()
        for category in SONGS:
            for song_name in SONGS[category]:
                if search_text in song_name.lower():
                    item = OneLineListItem(text=song_name, on_release=self.show_song_details, text_color=(1, 0.75, 0, 1))
                    song_list.add_widget(item)

if __name__ == "__main__":
    SongbookApp().run()
