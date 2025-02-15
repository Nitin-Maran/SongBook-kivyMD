from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
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
            "scale": "G Maj",
            "lyrics": [
                "All hail the power of Jesus' name!",
                "Let angels prostrate fall;",
                "Bring forth the royal diadem,",
                "And crown Him Lord of all!"
            ],
            "chords": [
                "G D G",
                "C G D G",
                "G D G C",
                "G D G"
            ],
            "chorus": [
                "And crown Him Lord of all,",
                "And crown Him Lord of all!",
                "Bring forth the royal diadem,",
                "And crown Him Lord of all!"
            ],
            "chorus_chords": [
                "G D G",
                "C G D G",
                "G D G C",
                "G D G"
            ]
        },
        "Amazing Grace": {
            "scale": "G Maj",
            "lyrics": [
                "Amazing grace! How sweet the sound",
                "That saved a wretch like me.",
                "I once was lost, but now am found;",
                "Was blind, but now I see."
            ],
            "chords": [
                "G C G D",
                "G C G",
                "G C G D",
                "G C G"
            ]
        },
        "Silent Night": {
            "scale": "G Maj",
            "lyrics": [
                "Silent night, holy night!",
                "All is calm, all is bright.",
                "Round yon Virgin, Mother and Child,",
                "Holy Infant so tender and mild."
            ],
            "chords": [
                "C G C",
                "F C G C",
                "C G C",
                "F C G C"
            ],
            "chorus": [
                "Sleep in heavenly peace,",
                "Sleep in heavenly peace."
            ],
            "chorus_chords": [
                "C G C",
                "F C G C"
            ]
        },
        "Hark! The Herald Angels Sing": {
            "scale": "D Maj",
            "lyrics": [
                "Hark! the herald angels sing,",
                "Glory to the newborn King;",
                "Peace on earth, and mercy mild,",
                "God and sinners reconciled."
            ],
            "chords": [
                "D G D",
                "A D G D",
                "G D G A",
                "D G D"
            ],
            "chorus": [
                "Hark! the herald angels sing,",
                "Glory to the newborn King!"
            ],
            "chorus_chords": [
                "D G D",
                "A D G D"
            ]
        },
        "All My Life Long I Had Panted": {
            "scale": "G Maj",
            "lyrics": [
                "All my life long I had panted",
                "For a drink from some cool spring,",
                "That I hoped would quench the burning",
                "Of the thirst I felt within."
            ],
            "chords": [
                "G C G",
                "D G C G",
                "G C D G",
                "G D G"
            ],
            "chorus": [
                "Hallelujah! I have found Him",
                "Whom my soul so long has craved!",
                "Jesus satisfies my longings,",
                "Through His blood I now am saved."
            ],
            "chorus_chords": [
                "G D G",
                "C G D G",
                "G D G C",
                "G D G"
            ]
        },
        "All Things Bright and Beautiful": {
            "scale": "G Maj",
            "lyrics": [
                "All things bright and beautiful,",
                "All creatures great and small,",
                "All things wise and wonderful,",
                "The Lord God made them all."
            ],
            "chords": [
                "G D G",
                "C G D G",
                "G D G C",
                "G D G"
            ],
            "chorus": [
                "Each little flower that opens,",
                "Each little bird that sings,",
                "He made their glowing colors,",
                "He made their tiny wings."
            ],
            "chorus_chords": [
                "G C G",
                "D G C G",
                "G C D G",
                "G D G"
            ]
        },
        "Amazing Grace How Sweet": {
            "scale": "G Maj",
            "lyrics": [
                "Amazing grace! How sweet the sound",
                "That saved a wretch like me.",
                "I once was lost, but now am found;",
                "Was blind, but now I see."
            ],
            "chords": [
                "G C G D",
                "G C G",
                "G C G D",
                "G C G"
            ]
        },
        "And Can It Be That I Should Gain": {
            "scale": "G Maj",
            "lyrics": [
                "And can it be that I should gain",
                "An interest in the Savior's blood?",
                "Died He for me, who caused His pain?",
                "For me, who Him to death pursued?"
            ],
            "chords": [
                "G C G D",
                "G C G",
                "G D G C",
                "G D G"
            ],
            "chorus": [
                "Amazing love! How can it be",
                "That Thou, my God, shouldst die for me?"
            ],
            "chorus_chords": [
                "G C G D",
                "G D G"
            ]
        },
        "As the Deer Pants for the Water": {
            "scale": "G Maj",
            "lyrics": [
                "As the deer pants for the water,",
                "So my soul longs after You.",
                "You alone are my heart's desire,",
                "And I long to worship You."
            ],
            "chords": [
                "G C G D",
                "G C G",
                "G C G D",
                "G C G"
            ],
            "chorus": [
                "You alone are my strength, my shield;",
                "To You alone may my spirit yield.",
                "You alone are my heart's desire,",
                "And I long to worship You."
            ],
            "chorus_chords": [
                "G C G D",
                "G D G C",
                "G C G D",
                "G C G"
            ]
        }
    },
    "Choruses": {
        "Here I Am to Worship": {
            "scale": "G Maj",
            "lyrics": [
                "Light of the world,",
                "You stepped down into darkness,",
                "Opened my eyes, let me see",
                "Beauty that made this heart adore You"
            ],
            "chords": [
                "G D Em C",
                "G D Em C",
                "G D Em C",
                "D C G"
            ],
            "chorus": [
                "Here I am to worship,",
                "Here I am to bow down,",
                "Here I am to say that You're my God."
            ],
            "chorus_chords": [
                "G D Em C",
                "G D Em C",
                "G D C G"
            ]
        },
        "Shout to the Lord": {
            "scale": "A Maj",
            "lyrics": [
                "My Jesus, my Savior,",
                "Lord, there is none like You;",
                "All of my days I want to praise",
                "The wonders of Your mighty love"
            ],
            "chords": [
                "A E F#m D",
                "A E F#m D",
                "A E F#m D",
                "E D A"
            ],
            "chorus": [
                "Shout to the Lord, all the earth, let us sing,",
                "Power and majesty, praise to the King."
            ],
            "chorus_chords": [
                "A E F#m D",
                "A D E A"
            ]
        },
        "How Great Is Our God": {
            "scale": "G Maj",
            "lyrics": [
                "The splendor of a King,",
                "Clothed in majesty,",
                "Let all the earth rejoice,",
                "All the earth rejoice"
            ],
            "chords": [
                "G C D",
                "Em C D",
                "G C D",
                "Em C D"
            ],
            "chorus": [
                "How great is our God! Sing with me,",
                "How great is our God! And all will see,",
                "How great, how great is our God!"
            ],
            "chorus_chords": [
                "G C D",
                "Em C D",
                "G C G"
            ]
        },
        "Oceans (Where Feet May Fail)": {
            "scale": "D Maj",
            "lyrics": [
                "You call me out upon the waters,",
                "The great unknown where feet may fail,",
                "And there I find You in the mystery,",
                "Listening and spending long nights with me"
            ],
            "chords": [
                "D A Bm G",
                "D A Bm G",
                "D A Bm G",
                "A G D"
            ],
            "chorus": [
                "Spirit lead me where my trust is without borders,",
                "Let me walk upon the waters, wherever You would call me."
            ],
            "chorus_chords": [
                "D A Bm G",
                "D A Bm G"

            ]
        }

    }
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
        canvas.before:
            Color:
                rgba: (0, 0, 0, 1)  # Top color - Black
            Rectangle:
                size: self.size
                pos: self.pos
            Color:
                rgba: (1, 0.8, 0, 1)  # Bottom color - Amber
            Rectangle:
                size: self.size
                pos: self.x, self.y + self.height / 2
        MDBoxLayout:
            orientation: "vertical"
            spacing: 20
            padding: [20, 40, 20, 20]
            size_hint: 1, 0.5
            pos_hint: {"center_x": 0.5, "top": 1}
            Image:
                source: "piano1.png"
                size_hint: 0.8, 0.8
                pos_hint: {"center_x": 0.5}
                allow_stretch: True
            MDLabel:
                text: "Christian Chord Book English"
                halign: "center"
                font_style: "H4"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # White text color
                bold: True
            MDLabel:
                text: "Nitin Maran M"
                halign: "center"
                font_style: "Subtitle1"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0.8  # Slightly transparent white text
                italic: True
        MDBoxLayout:
            orientation: "vertical"
            spacing: 20
            padding: [40, 50, 40, 20]  # Added padding to bring buttons down
            MDRaisedButton:
                text: "Hymns"
                on_release: app.show_category_songs("Hymns")
                size_hint: None, None
                size: 220, 60
                pos_hint: {"center_x": 0.5}
                md_bg_color: 0.9, 0.6, 0.2, 1
                elevation: 12
                text_color: 1, 1, 1, 1  # White text
            MDRaisedButton:
                text: "Choruses"
                on_release: app.show_category_songs("Choruses")
                size_hint: None, None
                size: 220, 60
                pos_hint: {"center_x": 0.5}
                md_bg_color: 0.4, 0.2, 0.6, 1
                elevation: 12
                text_color: 1, 1, 1, 1  # White text
            MDLabel:
                text: "Find Your Favorite Songs"
                halign: "center"
                font_style: "Caption"
                theme_text_color: "Hint"
                text_color: 1, 1, 1, 1  # White text

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.1, 0.1, 1 # Dark background
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
            background_color: 0.2, 0.2, 0.2, 1  # Dark background for text field
        MDScrollView:
            MDList:
                id: song_list

<SongScreen>:
    name: "song"
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.1, 0.1, 1 # Dark background
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
                    text_color: 1, 0.75, 0, 1 # Amber
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
                        size_hint: None, None
                        size: 160, 50
                        pos_hint: {"center_x": 0.5}
                        md_bg_color: 0.9, 0.6, 0.2, 1
                        elevation: 8
                    MDRaisedButton:
                        text: "Transpose +1"
                        on_release: app.transpose_chords(1)
                        size_hint: None, None
                        size: 160, 50
                        pos_hint: {"center_x": 0.5}
                        md_bg_color: 0.4, 0.2, 0.6, 1
                        elevation: 8
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
        """Show songs for the selected category."""
        song_list = self.root.get_screen("main").ids.song_list
        song_list.clear_widgets()
        for song_name, song_data in SONGS[category].items():
            item = TwoLineListItem(
                text=song_name,
                secondary_text=f"Scale: {song_data['scale']}",
                on_release=self.show_song_details,
                text_color=(1, 0.75, 0, 1),  # Amber text
            )
            song_list.add_widget(item)
        self.root.current = "main"

    def populate_song_list(self):
        """Populate the song list with all songs."""
        song_list = self.root.get_screen("main").ids.song_list
        song_list.clear_widgets()
        for song_name in SONGS:
            item = TwoLineListItem(
                text=song_name,
                on_release=self.show_song_details,
                text_color=(1, 0.75, 0, 1),  # Amber text
            )
            song_list.add_widget(item)

    def filter_song_list(self, search_text):
        """Filter songs in the list based on the search text."""
        search_text = search_text.lower()
        song_list = self.root.get_screen("main").ids.song_list
        song_list.clear_widgets()
        for category in SONGS:
            for song_name, song_data in SONGS[category].items():
                if search_text in song_name.lower():
                    item = TwoLineListItem(
                        text=song_name,
                        secondary_text=f"Scale: {song_data['scale']}",
                        on_release=self.show_song_details,
                        text_color=(1, 0.75, 0, 1),  # Amber text
                    )
                    song_list.add_widget(item)

    def show_song_details(self, instance):
        """Display the selected song's details."""
        for category in SONGS:
            if instance.text in SONGS[category]:
                self.current_song_name = instance.text
                song_data = SONGS[category][self.current_song_name]
                song_screen = self.root.get_screen("song")
                song_screen.ids.song_title.text = self.current_song_name

                # Populate lyrics with chords above each word
                self.current_chords = song_data["chords"]
                self.display_song_details(song_data["lyrics"], self.current_chords)
                self.root.current = "song"
                break

    def display_song_details(self, lyrics, chords):
        """Display the song lyrics with chords."""
        song_details = self.root.get_screen("song").ids.song_details
        song_details.clear_widgets()
        for chord_line, lyric_line in zip(chords, lyrics):
            line_layout = MDBoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=60,
                spacing=5,
            )
            chord_label = MDLabel(
                text=chord_line,
                font_style="Body2",
                halign="center",
                text_color=(1, 0.75, 0, 1),  # Amber text
            )
            lyric_label = MDLabel(
                text=lyric_line,
                font_style="Body1",
                halign="center",
                text_color=(1, 0.75, 0, 1),  # Amber text
            )
            line_layout.add_widget(chord_label)
            line_layout.add_widget(lyric_label)
            song_details.add_widget(line_layout)

    def transpose_chords(self, steps):
        """Transpose the chords by a given number of semitones."""
        for category in SONGS:
            if self.current_song_name in SONGS[category]:
                song_data = SONGS[category][self.current_song_name]
                self.current_chords = [
                    transpose_line(line, steps) for line in self.current_chords
                ]
                self.display_song_details(song_data["lyrics"], self.current_chords)
                break

    def show_main_screen(self):
        """Return to the main screen."""
        self.root.current = "main"

    def show_home_screen(self):
        """Return to the home screen."""
        self.root.current = "home"


if __name__ == "__main__":
    SongbookApp().run()
