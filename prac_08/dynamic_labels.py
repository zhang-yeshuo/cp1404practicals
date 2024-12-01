from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list = ['Brown', 'Bob', 'Cat', 'Cyan']

    def on_start(self):
        for name in self.list:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

DynamicLabelsApp().run()
