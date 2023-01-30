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
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd_extensions.sweetalert import SweetAlert
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window

Window.size = (320, 680)


mashuledb = mysql.connector.connect(
    host= "localhost",
    user= 'gideon',
    passwd= 'gen@mic1',
    database='Mashule',
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

class ReasiurceobjName(MDBoxLayout):
    pass

class AddactivityInt(MDBoxLayout):
    pass

class RessPassDC(MDBoxLayout):
    pass


class MashuleApp(MDApp):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)
        self.file_manager = MDFileManager(
            select_path = self.select_path,
            exit_manager= self.exit_manager,
            preview = True
        )

        self.data = []

        self.loginwdgt = OneLineIconListItem(
        text= 'Log in', on_press= self.Navigate_to_SignupPage
        )
        accticnwdgt = IconLeftWidget(
            icon= 'account-check'
        )

        self.loginwdgt.add_widget(accticnwdgt)
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

    def menu_callback(self, x):
        if x :
            #mashulecursor.execute("SELECT name, category FROM Schools WHERE category='County'")
            #dataf = mashulecursor.fetchall()
        
            toast('This functionality will be enabled soon')

   
    ################ Displaying schools on homepage ##############
    
    def on_start(self):

        data = self.fetch_data_from_database()

        self.create_cards(data)

        self.root.ids.left_drawer.add_widget(self.loginwdgt)

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

            schcatBl =(MDLabel(
                text=f"{school[1]} school" ,
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
                on_release= self.see_school_data
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
            if username == 'Mash@Admin' and userpass == 'gen@mic1':
                alert = SweetAlert(title="Admin login Succesfull",
                    text=f"Hi {username} You can now add manage users",
                    type="simple",
                    auto_dismiss=True)
                alert.open()
                self.Navigate_t0_homepage()
                self.set_login_form_empty()
                self.add_addim_previlages()
            else:
                alert = SweetAlert(title="Log In Succesfull",
                    text=f"Hi {username} Welcome To Mashule App. Let's Get Educated.",
                    type="simple",
                    auto_dismiss=True)
                alert.open()
                self.Navigate_t0_homepage()
                self.set_login_form_empty()
                self.add_loginuser_previlages()
        elif self.root.ids.username.text == "" and self.root.ids.userpass.text == "":
            toast('fill in Your login credentials')
        else:
            toast('Wrong Credentials, Try again')
            self.set_login_form_empty()
         
        

    def add_school(self, schoolname, schooladress, schoolweb, schoolemail, schoolcontact, schoolcat, schoolLevel):       

        mashulecursor.execute('INSERT INTO Schools (name, address, website, email, contact, category, level) VALUES (%s,%s,%s,%s,%s,%s,%s)',(schoolname, schooladress, schoolweb, schoolemail, schoolcontact, schoolcat, schoolLevel))
        mashuledb.commit()
        
        alert = SweetAlert(title="added succesfuly",
            text=f"You Can restart the app to See the school updated",
            type="simple",
            auto_dismiss=True)
        alert.open()
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
           
    #################### Registration Dialogs ###############

    def request_Registration_dialog(self, *args):
        if not self.dialog:
            self.request_Reg = MDDialog(
            title="Registration Request",
            text="PAY Ksh.3000 TO:\n 1111111111111 \n \n SEND YOU DETAILS TO: \nmashule@gmail.com\npayment reference number inclusive",
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="Cancel",
                    theme_text_color="Hint", 
                    on_release = self.close_request_Registration, 
                ),
                MDFlatButton(
                    text="Okay",
                    theme_text_color="Hint",
                    on_release = self.regpop, 
                ),
            ],
        )

        self.request_Reg.open()

    def close_request_Registration(self,obj):
        self.request_Reg.dismiss()

    def regpop(self, *args):
        alert = SweetAlert(title="Please Wait as we verify details",
            text="Hi, If you've contacted mashule@gmail.com, then we will send you an email with you first time login credentials(you can consider cahing them after login) through the email you used to contact us. \n \nThank you",
            type="simple",
            auto_dismiss=True)
        alert.open()
        self.request_Reg.dismiss()
    ######################### More about reg #########################

    def See_explation_dialog(self):
        if not self.dialog:
            self.See_exp = MDDialog(
            title="How to go about Registration",
            text="To Join Mashule, You will be required to: \n1.Pay Ksh.3000 to this acount mashuleacountNo. \n2.Send Your Your details(payment refference number inclusive) \n3.Wait for a while for verification \n4.Your login credentials will be sent through the emailprovided after verification \n5.You are encouraged to change the credentials to prefered ones",
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="Request Reg",
                    theme_text_color="Hint", 
                    on_release = self.request_Registration_dialog, 
                ),
                MDFlatButton(
                    text="Okay",
                    theme_text_color="Hint",
                    on_release = self.close_See_explation_dialog
                ),
            ],
        )

        self.See_exp.open()

    def close_See_explation_dialog(self,obj):
        self.See_exp.dismiss()

    ####################### restset password dialog ###########
    def showResetPassword_dialog_pop(self, *args):
        if not self.dialog:
            self.RespasD = MDDialog(
            title="Reset Password",
            type = 'custom',
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

    def add_resource_dialog(self, obj):
        if not self.dialog:
            self.adrd = MDDialog(
            title="Add Resources",
            type = 'custom',
            content_cls=AdresourcesDC(),
            #text="Creat Folder as per School name",
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="Cancel",
                    theme_text_color="Hint",
                    on_release = self.close_adrd_dialogue,
                ),
                MDFlatButton(
                    text="Okay",
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
                    on_release = self.req_lgin_rss,
                ),
            ],
        )
        self.ResNmD.open()
        

    def myresourcename_dialog_pop(self):
        if not self.dialog:
            self.MyResNmD = MDDialog(
            title="",
            type = 'custom',
            content_cls=ReasiurceobjName(),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="Cancel",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.closemyresourcename_dialog_pop,  
                ), 
                MDFlatButton(
                    text="Okay",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release = self.req_lgin_myrss,
                ),
            ],
        )
        self.MyResNmD.open()
        
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
    
    def see_school_data(self, args):

        self.root.current ='school'

    def add_addim_previlages(self):
        listofap = OneLineIconListItem(text= 'Add User', on_press= self.signupscreen)
        iconlt = IconLeftWidget(
            icon= 'account-plus',
        )
        listofap.add_widget(iconlt)
        self.root.ids.left_drawer.add_widget(listofap)

        listofuss = OneLineIconListItem(text= 'Manage Users', on_press= self.signupscreen)
        iconltuss = IconLeftWidget(
            icon= 'account-multiple',
        )
        listofuss.add_widget(iconltuss)
        self.root.ids.left_drawer.add_widget(listofuss)

        listofap1 = OneLineIconListItem(text= 'Logout', on_press= self.log_out_manager)
        iconlt1 = IconLeftWidget(
            icon= 'logout',
        )
        listofap1.add_widget(iconlt1)
        self.root.ids.left_drawer.add_widget(listofap1)

        self.root.ids.left_drawer.remove_widget(self.loginwdgt)

        addschwdgtactbtnad = MDFloatingActionButton(
            icon= "plus",
            md_bg_color= (.9, .9, .9, .7),
            size_hint= (None, None),
            icon_color= 'black',
            pos_hint= {'center_x': 1, 'center_y':0.4},
            on_release= self.nav_to_add_school
        )
        self.root.ids.addschwdgt.add_widget(addschwdgtactbtnad)

        addrswdgtbtn = MDFloatingActionButton(
            icon= "plus",
            md_bg_color= (.9, .9, .9, .7),
            size_hint= (None, None),
            icon_color= 'black',
            pos_hint= {'center_x': .9, 'center_y':0.2},
            on_release= self.add_resource_dialog
        )
        self.root.ids.addrsbtn.add_widget(addrswdgtbtn)
        

    def add_loginuser_previlages(self):
        listofsp = OneLineIconListItem(text= 'Logout', on_press= self.log_out_manager)
        iconltsp = IconLeftWidget(
            icon= 'logout',
        )
        listofsp.add_widget(iconltsp)
        self.root.ids.left_drawer.add_widget(listofsp)

        listofrpsp = OneLineIconListItem(text= 'Reset Pasword', on_press=self.showResetPassword_dialog_pop)
        iconltrpsp = IconLeftWidget(
            icon= 'key-chain',
        )
        listofrpsp.add_widget(iconltrpsp)
        self.root.ids.left_drawer.add_widget(listofrpsp)

        self.root.ids.left_drawer.remove_widget(self.loginwdgt)

        addschwdgtactbtn = MDFloatingActionButton(
            icon= "plus",
            md_bg_color= (.9, .9, .9, .7),
            size_hint= (None, None),
            icon_color= 'black',
            pos_hint= {'center_x': 1, 'center_y':0.4},
            on_release= self.nav_to_add_school
        )
        self.root.ids.addschwdgt.add_widget(addschwdgtactbtn)

        addrswdgtbtn = MDFloatingActionButton(
            icon= "plus",
            md_bg_color= (.9, .9, .9, .7),
            size_hint= (None, None),
            icon_color= 'black',
            pos_hint= {'center_x': .9, 'center_y':0.2},
            on_release= self.add_resource_dialog
        )
        self.root.ids.addrsbtn.add_widget(addrswdgtbtn)

    def log_out_manager(self, obj):
        toast('Under developement')
        
    def closeAddActivity_dialog_pop(self,obj):
        self.AddActivity.dismiss()

    def closeresourcename_dialog_pop(self,obj):
        self.ResNmD.dismiss()

    def closemyresourcename_dialog_pop(self, obj):
        self.MyResNmD.dismiss()

    def close_adrd_dialogue(self,obj):
        self.adrd.dismiss()

    def req_lgin_rss(self, *args):
        rssfdwt = OneLineIconListItem(
        text= ""
        )
        resfldwdgt = IconLeftWidget(
            icon= 'folder',
            #on_release= self.open_file_manager()
        )
        
        rssfdwt.add_widget(resfldwdgt)
        #rssfdwt.add_widget(resflrdwdgt)

        self.root.ids.addreslist.add_widget(rssfdwt)

        self.ResNmD.dismiss()
        self.adrd.dismiss()
        self.root.current = 'resources'

    def req_lgin_myrss(self, *args):
        myrssfdwt = OneLineIconListItem(
        text= ""
        )
        myresfldwdgt = IconLeftWidget(
            icon= 'file',
            #on_release= self.open_file_manager()
        )
        
        myrssfdwt.add_widget(myresfldwdgt)
        #rssfdwt.add_widget(resflrdwdgt)

        self.root.ids.addreslist.add_widget(myrssfdwt)

        self.MyResNmD.dismiss()
        self.adrd.dismiss()
        self.root.current = 'resources'
    
    def open_file_manager(self):
        self.file_manager.show('/')
    
    def select_path(self, path):
        toast(f'you have selected {path}')

    def exit_manager(self, obj):
        self.file_manager.close()

    def Navigate_t0_homepage(self):
        self.root.current = 'home'

    def Navigate_to_resourcespage(self):
        self.root.current = 'resources'

    def Navigate_to_SignupPage(self, *args):
        self.root.current = 'sgnlgn'

    def signupscreen(self, *args):
        self.root.current = 'signupU'

    def nav_to_add_school(self, arg):
        self.root.current = 'addschool'

    def add_school_submit(self):
        self.root.current = 'home'
    
    def build(self):
        return self.screen

MashuleApp().run()