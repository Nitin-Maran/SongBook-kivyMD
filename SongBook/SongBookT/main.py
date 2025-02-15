from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class SongBookApp(MDApp):
    def build(self):
        screen = MDScreen()
        scroll_view = MDScrollView()
        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=20)

        # Silent Night Song (G Major)
        silent_night_title = MDLabel(
            text="Silent Night",
            font_style="H4",
            halign="center"
        )
        silent_night_scale = MDLabel(
            text="Scale: G Major",
            halign="center"
        )
        silent_night_lyrics = MDLabel(
            text="""
Chords: G, Em, Bm, D, C

Verse 1:
G                Em
Silent night, holy night
Bm             D
All is calm, all is bright
Em             G
Round yon Virgin mother and Child
C           Cmaj7    G
Holy infant so tender and mild
C       Em       G        D
Sleep in heavenly peace
G       D7      Em7     G
Sleep in heavenly peace

Verse 2:
G               Em
Silent night, holy night
Bm             D
Son of God, love's pure light
Em             G2
Radiant beams from Thy holy face
C           Cmaj7    G
With the dawn of redeeming grace
C       Em       G        D
Jesus, Lord at Thy birth
G       D7      Em7     G
Jesus, Lord at Thy birth
""",
            halign="center"
        )

        # Hark the Herald Song (A Major)
        hark_herald_title = MDLabel(
            text="Hark! The Herald Angels Sing",
            font_style="H4",
            halign="center"
        )
        hark_herald_scale = MDLabel(
            text="Scale: A Major",
            halign="center"
        )
        hark_herald_lyrics = MDLabel(
            text="""
Chords: A, D, E, F#m

Verse 1:
A               D
Hark! The herald angels sing
E               A
Glory to the newborn King
F#m             D
Peace on earth and mercy mild
A               E
God and sinners reconciled
D               E
Joyful, all ye nations rise
A               D
Join the triumph of the skies
E               A
With angelic host proclaim
D               E        A
Christ is born in Bethlehem
""",
            halign="center"
        )

        # Add widgets to layout
        layout.add_widget(silent_night_title)
        layout.add_widget(silent_night_scale)
        layout.add_widget(silent_night_lyrics)
        layout.add_widget(hark_herald_title)
        layout.add_widget(hark_herald_scale)
        layout.add_widget(hark_herald_lyrics)

        scroll_view.add_widget(layout)
        screen.add_widget(scroll_view)
        return screen

SongBookApp().run()
