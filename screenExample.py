from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        Label:
            text: 'Menu'

    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'
        padding: 0, 0, 10, 10

        Button:
            text: 'Next'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'
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

<SettingsScreen>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'

        Label:
            text: 'Settings'

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
                root.manager.current = 'menu'
            size: 100, 50
            size_hint: None, None
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
