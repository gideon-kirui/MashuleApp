from kivymd.app import MDApp
#import sqlite3
from firebase import firebase
from kivy.lang.builder import Builder
from kivy_garden.mapview import MapView, MapMarkerPopup
from scrn_mng import screen_helper
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd_extensions.sweetalert import SweetAlert
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window

Window.size = (320, 680)


class SignupDC(BoxLayout):
    pass

class LoginDC(BoxLayout):
    pass

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class AdresourcesDC(BoxLayout):
    pass

class ReasiurceName(BoxLayout):
    pass

class RessPassDC(BoxLayout):
    pass

firebase = firebase.FirebaseApplication('https://mashule-47283-default-rtdb.firebaseio.com/, None')

class MashuleApp(MDApp):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)
    
    ########## Changing Category ###########
        menudata1 = ['National', 'Provincial', 'Extra-County', 'County', 'Distict']

        menu_items1 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        #"on_release": lambda x=f"{i}": self.menu_callback(x),
        } for i in menudata1
    
        ]
        self.menu = MDDropdownMenu(
        caller=self.screen.ids.drop_item,
        items=menu_items1,
        width_mult=2.5,
        max_height=200,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

    ########################### Edit School Menu #################
    ########## Changing Category ###########
        menudata2 = ['Edit', 'Delete', 'Rate', 'Report']

        menu_items2 = [
        {
        "text": f"{e}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{e}": self.menu_callback(x),
        } for e in menudata2
    
        ]
        self.menu2 = MDDropdownMenu(
        caller=self.screen.ids.drop_item2,
        items=menu_items2,
        width_mult=1.5,
        max_height=200,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

    def menu_callback(self, data):
        dia = data[3]
        if dia:
            self.show_exit_dialog()

    #################### Log In and SignUp ###############
    def add_user(self, regname, regpass):

        users = {'name': regname, 'password': regpass},

        regpsscmp = self.root.ids.regpass.text
        regpassconcmp = self.root.ids.regpasscon.text

        if regpsscmp == regpassconcmp:
            firebase.post('/Users', users)

            alert = SweetAlert(title="Registration Sucesfull",
                text="User Registered Successfully",
                type="simple",
                auto_dismiss=True)
            alert.open()

            self.Navigate_t0_homepage()

        else:
            alert = SweetAlert(title="Passwords Didn't match",
                text="Kindly Check the two passwords and Try again!",
                type="simple",
                auto_dismiss=True)
            alert.open()

    def user_login(self):

        username = self.root.ids.username.text
        userpasword = self.root.ids.userpass.text

        regusers = firebase.get('/Users', '')

        for i in regusers.keys():
            if i (str['name']) == username and i (str['password']) == userpasword:
                    toast(username + ', you have login succesfully')
                    self.Navigate_t0_homepage()

            else:
                alert = SweetAlert(title="Incorect Logins",
                    text="Kindly Check your credentials and Try again!",
                    type="alert",
                    auto_dismiss=True)
                alert.open()

    def add_school(self):

        schoolname = self.root.ids.schoolname
        schooladress = self.root.ids.schooladress
        schoolweb = self.root.ids.schoolweb
        schoolemail = self.root.ids.schoolemail
        schoolcontact = self.root.ids.schoolcontact
        schoolcat = self.root.ids.schoolcat
        schoolLevel = self.root.ids.schoolLevel

        shools = {
            'schnm': schoolname,
            'schadrs': schooladress,
            'schwb': schoolweb,
            'scheml': schoolemail,
            'schcnt': schoolcontact,
            'schcat': schoolcat,
            'schllvl': schoolLevel,
        }

        print(shools)

        firebase.post('/Schools', shools)
        toast(schoolname + ', added succesfuly')
        self.Navigate_t0_homepage()

    dialog = None
    #################### Logout Dialog ###############

    def show_exit_dialog(self):
        if not self.dialog:
            self.dialog1 = MDDialog(
            title="Log Out?",
            text="By clicking Yes, You will be loged out of this App and now you will be using it as a vistor. \n Do you wish to proceed?",
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="No",
                    theme_text_color="Hint", 
                    on_release = self.close_popup_dialogue1, 
                ),
                MDFlatButton(
                    text="Yes",
                    theme_text_color="Hint",
                ),
            ],
        )

        self.dialog1.open()


    def close_popup_dialogue1(self,obj):
        self.dialog1.dismiss()
           
    #################### ResetPassword Dialogs ###############

    def showResetPassword_dialog_pop(self):
        if not self.dialog:
            self.RespasD = MDDialog(
            title="Reset Password",
            #type = 'custom',
            content_cls=RessPassDC(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.closePassword_dialog_pop,  
                ), 
                MDFlatButton(
                    text="Reset",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.RespasD.open()

    def closePassword_dialog_pop(self,obj):
        self.RespasD.dismiss()

    #################### ADD ressources Dialog ###############

    def add_resource_dialog(self):
        if not self.dialog:
            self.adrd = MDDialog(
            title="Add Resources",
            type = 'custom',
            content_cls=AdresourcesDC(),
            #text="Creat Folder as per School name",
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="Create",
                    theme_text_color="Hint", 
                     
                ),
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Hint",
                    on_release = self.close_adrd_dialogue,
                ),
            ],
        )

        self.adrd.open()

    #################### ADD ressources Dialog ###############

    def resourcename_dialog_pop(self):
        if not self.dialog:
            self.ResNmD = MDDialog(
            title="",
            type = 'custom',
            content_cls=ReasiurceName(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.closeresourcename_dialog_pop,  
                ), 
                MDFlatButton(
                    text="Okay",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.Navigate_to_SignupPage,
                ),
            ],
        )
        self.ResNmD.open()

    def closeresourcename_dialog_pop(self,obj):
        self.ResNmD.dismiss()

    def close_adrd_dialogue(self,obj):
        self.adrd.dismiss()

    def Navigate_t0_homepage(self):
        self.root.current = 'home'

    def Navigate_to_resourcespage(self):
        self.root.current = 'resources'

    def Navigate_to_SignupPage(self):
        self.root.current = 'sgnlgn'

    def add_school_submit(self):
        self.root.current = 'home'
    
    def build(self):
        return self.screen

MashuleApp().run()