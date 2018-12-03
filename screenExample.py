from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.progressbar import ProgressBar

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<StartScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        Label:
            text: 'Start'

    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        padding: 0, 0, 10, 10

        Button:
            text: 'Next'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'progress'
            size: 100, 50
            size_hint: None, None

    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        padding: 10, 0, 0, 10

        Button:
            text: 'Back'
            size: 100, 50
            size_hint: None, None

<ProgressScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        padding: 50, 0, 50, 0

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            spacing: 20

            Label:
                text: 'Updating...'

            ProgressBar:
                value: 50

    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        padding: 0, 0, 10, 10

        Button:
            text: 'Next'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'done'
            size: 100, 50
            size_hint: None, None

    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        padding: 10, 0, 0, 10

        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'start'
            size: 100, 50
            size_hint: None, None

<DoneScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        Label:
            text: 'Done'

    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        padding: 0, 0, 10, 10

        Button:
            text: 'Next'
            size: 100, 50
            size_hint: None, None

    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'bottom'
        padding: 10, 0, 0, 10

        Button:
            text: 'Back'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'progress'
            size: 100, 50
            size_hint: None, None
""")

# Declare both screens
class StartScreen(Screen):
    pass

class ProgressScreen(Screen):
    pass

class DoneScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(ProgressScreen(name='progress'))
sm.add_widget(DoneScreen(name='done'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
