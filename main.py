from kivymd.app import MDApp
import mysql.connector
from kivy.lang.builder import Builder
from kivy_garden.mapview import MapView, MapMarkerPopup
from scrn_mng import screen_helper
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.image import Image
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd_extensions.sweetalert import SweetAlert
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window

Window.size = (320, 680)


mashuledb = mysql.connector.connect(
    host="localhost", #"11.106.0.13",
    user="gideon", #'marshaa1_mshule',
    passwd="gen@mic1", #'mashule@cpanel',
    database="Mashule",#'marshaa1_MashuleApp',
    auth_plugin='mysql_native_password'
)

mashulecursor = mashuledb.cursor()

class SignupDC(MDBoxLayout):
    pass

class LoginDC(MDBoxLayout):
    pass

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class AdresourcesDC(MDBoxLayout):
    pass

class ReasiurceName(MDBoxLayout):
    pass

class AddactivityInt(MDBoxLayout):
    pass

class RessPassDC(MDBoxLayout):
    pass


class MashuleApp(MDApp):

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)

        self.data = []

    ########## Changing Category ###########
        menudata1 = ['National', 'Provincial', 'Extra-County', 'County', 'Distict']

        menu_items1 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback(x),
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

    ########################### Fillter Schools #################

    #def menu_callback(self, x):
        #if x == 'County' :
            #mashulecursor.execute("SELECT name, category FROM Schools WHERE category='County'")
            #dataf = mashulecursor.fetchall()
            #self.create_cards(data=dataf)
            #print(data)
            #toast(f"you have selected {x}")

   
    ################ Displaying schools on homepage ##############
    
    def on_start(self):

        data = self.fetch_data_from_database()

        self.create_cards(data)

    def fetch_data_from_database(self):

        mashulecursor.execute('SELECT name, category FROM Schools')
        data = mashulecursor.fetchall()
        return data

    def create_cards(self, data):

        for school in data:
            card = MDCard(md_bg_color= (.9, .9, .9, .7), 
            size_hint=(.4, .6),
            size_hint_y=None,
            height= 250,
            padding=5,
            pos_hint={'center_x': .5, 'center_y': .5},
            orientation="vertical",)

            gridlay =(MDGridLayout(cols=1))
            schlnmBl=(MDBoxLayout(adaptive_height= True))
            mdlschnm = (MDLabel(text=f"{school[0][0:7]} ...",
                font_style="Body1",
                size_hint_y= None,
                height= 10,
                color='black',
                pos_hint= {"center_y": .5}
            ))
            icnbt = (MDIconButton(
                md_bg_color=(1, 1, 1, 1),
                icon= "dots-vertical",
                size_hint_y= None,
                icon_size= "14sp",
                size_hint_x= None,
                pos_hint= {"center_y": .5},
               # on_release= self.menu2.open()
            ))
            schlnmBl.add_widget(mdlschnm)
            schlnmBl.add_widget(icnbt)

            schcatBl =(MDLabel(text=f"{school[1]} school" ,
                size_hint_y= None,
                height=20,
                font_style= "Caption",
                color= 'brown',
            ))
            
            
            gridlay.add_widget(schlnmBl)
            gridlay.add_widget(schcatBl)

            card.add_widget(gridlay)
            imgbxlt = (MDBoxLayout(
                size_hint_y= None,
                spacing=5,
                height= 60,
            ))
            img = Image(source='./images/school2.png', size_hint_y= None)
            imgbxlt.add_widget(img)
            card.add_widget(imgbxlt)
            rigstrl =(MDGridLayout(
                cols= 1
            ))
            rsbtn = (MDRaisedButton(
                text= "see details",
                md_bg_color= "blue",
                pos_hint= {"center_x": .5, "center_y": .03},
                on_release= self.see_school_data()
            ))
            bxstrl = (MDBoxLayout(
                size_hint_y= None,
                height=40,
            ))
            strts = (MDIcon(
                icon= "hexagram",
                color= 'green'
            ))
            strts1 = (MDIcon(
                icon= "hexagram",
                color= 'green'
            ))
            strts2 = (MDIcon(
                icon= "hexagram",
                color= 'green'
            ))
            strts3 = (MDIcon(
                icon= "hexagram",
                color= 'green'
            ))
            strts4 = (MDIcon(
                icon= "hexagram",
                color= 'green'
            ))
            rigstrl.add_widget(rsbtn)
            rigstrl.add_widget(bxstrl)
            bxstrl.add_widget(strts)
            bxstrl.add_widget(strts1)
            bxstrl.add_widget(strts2)
            bxstrl.add_widget(strts3)
            bxstrl.add_widget(strts4)
            card.add_widget(rigstrl)
            self.root.ids.schoolitemdis.add_widget(card)
    
    #################### Log In and SignUp ###############
    def add_user(self, regname, regpass):

        regpsscmp = self.root.ids.regpass.text
        regpassconcmp = self.root.ids.regpasscon.text

        if regpsscmp == regpassconcmp:
            mashulecursor.execute('INSERT INTO Users (name, password) VALUES (%s,%s)',(regname, regpass))
            mashuledb.commit()
            alert = SweetAlert(title="Registration Sucesfull",
                text=f"{regname} Registered Successfully",
                type="simple",
                auto_dismiss=True)
            alert.open()
            self.set_regform_empty()
        
        else:
            alert = SweetAlert(title="Passwords Didn't match",
                text="Kindly Check the two passwords and Try again!",
                type="simple",
                auto_dismiss=True)
            alert.open()

    def user_login(self, username, userpass):

        mashulecursor.execute('SELECT * FROM Users where name=%s AND password=%s', (username, userpass))
        user = mashulecursor.fetchone()

        if user:
            alert = SweetAlert(title="Log In Succesfull",
                text=f"Hi {username} Welcome To Mashule App. Let's Get Educated.",
                type="simple",
                auto_dismiss=True)
            alert.open()
            self.Navigate_t0_homepage()
            self.set_login_form_empty()

        else:
            toast('Wrong Credentials, Try again')
            self.set_login_form_empty()
         
        

    def add_school(self, schoolname, schooladress, schoolweb, schoolemail, schoolcontact, schoolcat, schoolLevel):

        mashulecursor.execute('INSERT INTO Schools (name, address, website, email, contact, category, level) VALUES (%s,%s,%s,%s,%s,%s,%s)',(schoolname, schooladress, schoolweb, schoolemail, schoolcontact, schoolcat, schoolLevel))
        mashuledb.commit()
        toast(schoolname + ', added succesfuly')
        self.set_addschoolform_empty()
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
################################### Add Activity Dialogue #############
    def AddActivity_dialog_pop(self):
        if not self.dialog:
            self.AddActivity = MDDialog(
            title="",
            type = 'custom',
            content_cls=AddactivityInt(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.closeAddActivity_dialog_pop,  
                ), 
                MDFlatButton(
                    text="Okay",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.Navigate_t0_homepage,
                ),
            ],
        )
        self.AddActivity.open()

    def set_regform_empty(self):
        self.root.ids.regname.text = ""
        self.root.ids.regpass.text = ""
        self.root.ids.regpasscon.text = ""

    def set_login_form_empty(self):
        self.root.ids.username.text = ""
        self.root.ids.userpass.text = ""
        

    def set_addschoolform_empty(self):
        self.root.ids.schoolname.text = ""
        self.root.ids.schooladress.text = ""
        self.root.ids.schoolweb.text = "" 
        self.root.ids.schoolemail.text = "" 
        self.root.ids.schoolcontact.text = "" 
        self.root.ids.schoolcat.text = ""
        self.root.ids.schoolLevel.text = ""
    
    def see_school_data(self):

        self.root.current ='school'

        mashulecursor.execute('SELECT * FROM Schools (name, contact, email, website, address')
        name = mashulecursor.fetchall()

        for i in name:
            self.root.ids.schabname.text = f"More About {i[0]}"

        mashulecursor.execute('SELECT contact FROM Schools')
        cont = mashulecursor.fetchall()

        for c in cont:
            self.root.ids.schconta.text = f"{c[0]}"
            
        mashulecursor.execute('SELECT email FROM Schools')
        ema = mashulecursor.fetchall()

        for e in ema:
            self.root.ids.schemai.text = f"{e[0]}"

        mashulecursor.execute('SELECT website FROM Schools')
        web = mashulecursor.fetchall()

        for w in web:
            self.root.ids.schwebs.text = f"{w[0]}"

        mashulecursor.execute('SELECT address FROM Schools')
        add = mashulecursor.fetchall()

        for a in add:
            self.root.ids.schaddr.text = f"{a[0]}"

    def closeAddActivity_dialog_pop(self,obj):
        self.AddActivity.dismiss()

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