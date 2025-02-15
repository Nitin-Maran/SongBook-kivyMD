from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton

class SilentNightApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"

        screen = MDScreen()
        main_layout = MDBoxLayout(orientation='vertical', padding=10, spacing=5)

        # Song Title
        title_label = MDLabel(
            text="SILENT NIGHT",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(title_label)

        # Transpose Input Layout
        transpose_layout = MDBoxLayout(
            orientation='horizontal',
            spacing=5,
            padding=(20, 0),
            size_hint_y=None,
            height=60
        )

        self.transpose_input = MDTextField(
            hint_text="Transpose",
            input_type='number',
            helper_text="(-12 to +12)",
            helper_text_mode="on_error",
            size_hint_x=0.4,
            max_text_length=3
        )

        transpose_button = MDIconButton(
            icon="piano",
            on_release=self.transpose_song
        )

        transpose_layout.add_widget(self.transpose_input)
        transpose_layout.add_widget(transpose_button)
        main_layout.add_widget(transpose_layout)

        # Scroll View for Lyrics
        scroll_view = MDScrollView(size_hint_y=0.7)  # Reduced scrolling limit

        self.song_label = MDLabel(
            text=self.get_original_song_content(),
            theme_text_color="Custom",
            text_color=self.theme_cls.primary_color,
            font_style="Body1",
            size_hint_y=None,
            height=600,  # Reduced height
            padding=(20, 20)
        )

        scroll_view.add_widget(self.song_label)
        main_layout.add_widget(scroll_view)

        screen.add_widget(main_layout)
        return screen

    def get_original_song_content(self):
        return """**Original Scale**: G Major

**Original Chords**:
G                 D7             G
Silent night, holy night
C                 G               C
All is calm, all is bright
G                 C               G
'Round yon Virgin Mother and Child
C                 G               D7           G Em
Holy infant so tender and mild
G                 D7              G
Sleep in heavenly peace
G                 D7              G
Sleep in heavenly peace"""

    def transpose_song(self, instance):
        try:
            semitones = int(self.transpose_input.text)
            if -12 <= semitones <= 12:
                transposed_song = self.transpose_chords(self.get_original_song_content(), semitones)
                self.song_label.text = transposed_song
            else:
                print("Transpose between -12 and +12")
        except ValueError:
            print("Invalid transpose value")

    def transpose_chords(self, song_text, semitones):
        chord_map = {
            'C': ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C'],
            'G': ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']
        }

        # Placeholder transposition logic
        return song_text.replace('G', chord_map['G'][(chord_map['G'].index('G') + semitones) % 12])

SilentNightApp().run()

