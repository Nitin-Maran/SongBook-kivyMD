from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout()

        # Create an Image widget
        image = Image(source='piano.png')

        # Add the Image widget to the layout
        layout.add_widget(image)

        return layout

if __name__ == '__main__':
    MainApp().run()