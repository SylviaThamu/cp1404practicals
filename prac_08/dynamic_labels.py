"""CP1404/CP5632 Practical - Dynamic Labels"""

import os
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple app that creates a Label for each name."""
    def __init__(self, **kwargs):
        """Set up data (the model)."""
        super().__init__(**kwargs)
        # Model: list of names (strings)
        self.names = ["Peter Thamu", "Rachel Thamu", "Christine Thamu", "Sylvia Thamu"]

    def build(self):
        """Build the Kivy GUI and create the labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        # Create one Label per name and add it to the BoxLayout with id 'main'
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root


DynamicLabelsApp().run()
