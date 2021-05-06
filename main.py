from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    EmoScreen:
<MenuScreen>:
    name: 'menu'
    MDTextField:
        hint_text: "ENTER USERNAME"
        helper_text: "OR CHECK SAVED LOGINS"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint_x:None
        width:200
    MDRectangleFlatButton:
        text: 'SUBMIT'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.check_string()
    

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'SELECT LANGUAGE'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'TELUGU'
        pos_hint: {'center_x':0.7,'center_y':0.4}
        on_press: root.telugu()
    MDRectangleFlatButton:
        text: 'HINDI'
        pos_hint: {'center_x':0.3,'center_y':0.4}
        on_press: root.manager.current = 'EMO'
    MDRectangleFlatButton:
        text: 'TAMIL'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        on_press: root.manager.current = 'EMO'
    MDRectangleFlatButton:
        text: 'ENGLISH'
        pos_hint: {'center_x':0.3,'center_y':0.3}
        on_press: root.manager.current = 'EMO'
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: 'Demo'
                icon: 'language-python'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: root.navigation_draw()
<EMOScreen>:
    name: 'EMO'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'CAMERA'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        on_press: root.sayhello2()
    MDRectangleFlatButton:
        text: 'RANDOM'
        pos_hint: {'center_x':0.5,'center_y':0.45}
        on_press: root.sayhello()
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: 'Demo'
                icon: 'language-python'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: root.navigation_draw()
"""


class MenuScreen(Screen):
    def check_string(self):
        self.manager.current = "profile"

    def closedialog(self, obj):
        self.dialog.dismiss()


class ProfileScreen(Screen):
    def telugu(self):
        self.manager.current = "EMO"
    def navigation_draw(self):
        self.manager.current = "menu"
class EmoScreen(Screen):
    def sayhello(self):
        print("HI")

    def sayhello2(self):
        print("HI")
    def navigation_draw(self):
        self.manager.current = "menu"


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ProfileScreen(name='EMO'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()
