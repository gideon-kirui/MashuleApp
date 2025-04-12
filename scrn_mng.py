screen_helper = '''
ScreenManager:
    MDScreen:
        id: 'home'
        name: 'home'
        md_bg_color: .9, .9, .9, .7
        MDBoxLayout:
            orientation: "vertical"
            MDGridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    padding:dp(10)
                    spacing:dp(10)
                    MDIconButton:
                        icon: "menu"
                        color: "blue"
                        on_press: nav_hdrawer.set_state("open")
                        text_color: (1, 1, 0, 1)

                    MDBoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_y':0.5}
                        spacing:dp(10)
                        MDLabel:
                            text: "Ma-shule"
                            font_style: "H4"
                            color: "black"
                            halign: "left"
                            text_size: (150, None)
                            size_hint_x: .4

                        MDIcon:
                            icon: "images/logo.png"
                            
                            

                    MDIconButton:
                        icon: "dots-vertical"
                        color: "blue"
                        on_press: nav_hadrawer.set_state("open")

                MDBoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    padding:dp(10)
                    spacing:dp(10)
                    MDTextField:
                        hint_text: "Search  School"
                        icon_right: 'magnify'
                        mode: "round"
                        hint_text_color_normal: 0, 0, 0, .3
                        hint_text_color_focus: 0, 0, 0, 1
                        line_color_focus: 0, 0, 0, 1
                        icon_right_color_normal: 0, 0, 0, 1
                        text_color_focus: 0, 0, 0,
                        
                       
                        
                    MDRaisedButton:
                        id: drop_item
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        text: 'Category'
                        font_size: '16sp'
                        on_release: app.menu.open()

            MDCard:
                id: schholswidget
                md_bg_color: 1, 1, 1, .6
                radius: [50, 50, 0, 0]
                padding: dp(10)
                MDBoxLayout:
                    id: home_view
                    orientation: 'vertical'
                    ScrollView:
                        MDGridLayout:
                            id: schoolitemdis
                            padding: '10dp'
                            spacing: '10dp'
                            cols: 2
                            size_hint: 1, None
                            height: self.minimum_size[1]
                            
                            
                                

                    MDBoxLayout:
                        id: addschwdgt
                        size_hint_y: None
                        size_hint_x: None
                        height: self.minimum_size[1]
                        

            MDLabel:
                text: 'mashuleApp Copyright 2023'
                pos_hint: {"center_x": .5, "center_y": .5}
                font_style: 'Caption'
                hint_size: None, None
                adaptive_size: True

        MDNavigationDrawer:
            id: nav_hdrawer
            top_right_radius: 20
            size_hint: (0.65, 0.2)
            pos_hint: {'center_y':0.88}
            BoxLayout:
                orientation: 'vertical'
                spacing: '5dp'
                ScrollView:
                    MDList:
                        id:left_drawer
                        #OneLineIconListItem:
                            #text: 'Log in'
                            #on_press: root.current='sgnlgn'
                            #IconLeftWidget:
                                #icon: 'account-check'

                        OneLineIconListItem:
                            text: 'Resources'
                            on_press: root.current = 'resources'
                            IconLeftWidget:
                                icon: 'pencil'
            
        MDNavigationDrawer:
            id: nav_hadrawer
            anchor: 'right'
            top_right_radius: 20
            size_hint: (0.8, 0.5)
            pos_hint: {'center_y':0.73}
            BoxLayout:
                orientation: 'vertical'
                spacing: '5dp'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'About Us'
                            #on_press: app.show_exit_dialog()
                            IconLeftWidget:
                                icon: 'information-outline'

                        OneLineIconListItem:
                            text: 'Help'
                            #on_press: app.showLogin_dialog_pop()
                            IconLeftWidget:
                                icon: 'help'

                        OneLineIconListItem:
                            text: 'Contact Us'
                            #on_press: app.showLogin_dialog_pop()
                            IconLeftWidget:
                                icon: 'phone'

                        OneLineIconListItem:
                            text: 'Share'
                            #on_press: app.showSignup_dialog_pop()
                            IconLeftWidget:
                                icon: 'share-variant'

                        OneLineIconListItem:
                            text: 'FeedBack'
                            #on_press: app.show_exit_dialog()
                            IconLeftWidget:
                                icon: 'comment-outline'

                        OneLineIconListItem:
                            text: 'Terms And Conditions'
                            #on_press: app.show_exit_dialog()
                            IconLeftWidget:
                                icon: 'handshake-outline'    

    MDScreen:
        id: 'sgnlgn'
        name: 'sgnlgn'
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1
            MDIconButton:
                icon: "arrow-left"
                color: "blue"
                on_press: root.current = 'home'
                pos_hint: {"center_x": .08, "center_y": .97}
            Image:
                source: "images//logo.png"
                size_hint: .6, .4
                pos_hint: {"center_x": .5, "center_y": .8}
                
            MDLabel:
                text: "Log In"
                pos_hint: {"center_x": .5, "center_y": .6}
                halign: "center"
                underline: True
                font_size: "40sp"
                theme_text_color: "Custom"
                color: 60/255, 43/255, 117/255, 1
                

            MDTextField:
                id: username
                hint_text: "name"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .45}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDGridLayout:
                cols:2
                size_hint_y: None
                height: self.minimum_size[1]
                pos_hint: {"center_x": .5, "center_y": .37}
                padding:dp(10)
                MDTextField:
                    id: userpass
                    hint_text:  'password'
                    password: True
                    icon_left: "key-variant"
                    mode: 'round'
                    line_anim: 'True'
                    

                MDIconButton:
                    icon: "eye-off"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    pos: regpass.width - self.width + dp(8), 0
                    theme_text_color: "Hint"
                    on_release:
                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                        userpass.password = False if userpass.password is True else True
            
            MDTextButton:
                text: "Forget your password?"
                theme_text_color: "Custom"
                text_color: 246/255, 135/255, 177/255, 1
                pos_hint: {"center_x": .5, "center_y": .27}
                #on_press: app.showResetPassword_dialog_pop()

            MDLabel:
                size_hint_x: .9
                text: "You dont have an Acount? click Requset Reg bellow"
                theme_text_color: "Custom"
                font_style: 'Caption'
                text_color: 0, 0, 0, 1
                pos_hint: {"center_x": .5, "center_y": .23}
                

            MDFloatLayout:
                size_hint: 1, .2
                pos_hint: {"center_y": .5}
                MDGridLayout:
                    cols:2
                    padding:dp(10)
                    spacing:dp(5)
                    MDChip:
                        text: "Requset Reg"
                        on_release: app.request_Registration_dialog()
                        icon_left: "mail"
                        md_bg_color: .2, .2, .2, .6
                        text_color: 1, 1, 1, 1
                        icon_left_color: 5, 5, 5, .4
                    
                    MDChip:
                        text: "Know More"
                        on_release: app.See_explation_dialog()
                        icon_left: "information"
                        text_color: 0, 0, 1, 1
                        icon_left_color: .2, .2, .2, 1

            Button:
                text: "Log In"
                font_size: "20sp"
                size_hint: .4, .06
                pos_hint: {"center_x": .5, "center_y": .08}
                background_color: 0, 0, 0, 0
                on_release: app.user_login(username.text, userpass.text)
                canvas.before:
                    Color: 
                        rgb: 246/255, 135/255, 177/255, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [23]

    MDScreen:
        id: 'signupU'
        name: 'signupU'
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1
            MDIconButton:
                icon: "arrow-left"
                color: "blue"
                on_press: root.current = 'home'
                pos_hint: {"center_x": .08, "center_y": .97}

            Image:
                source: "images//logo1.jpg"
                size_hint: .6, .4
                pos_hint: {"center_x": .5, "center_y": .8}
                
            MDLabel:
                text: "REGISTER NEW USER"
                pos_hint: {"center_x": .5, "center_y": .55}
                halign: "center"
                underline: True
                font_style:"H5"
                theme_text_color: "Custom"
                color: 60/255, 43/255, 117/255, 1
                

            MDTextField:
                id: regname
                hint_text: "name"
                size_hint: .9, None
                pos_hint: {"center_x": .5, "center_y": .43}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDGridLayout:
                cols:2
                size_hint_y: None
                height: self.minimum_size[1]
                pos_hint: {"center_x": .5, "center_y": .33}
                padding:dp(10)
                MDTextField:
                    id: regpass
                    hint_text:  'password'
                    password: True
                    icon_left: "key-variant"
                    mode: 'round'
                    line_anim: 'True'
                    

                MDIconButton:
                    icon: "eye-off"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    pos: regpass.width - self.width + dp(8), 0
                    theme_text_color: "Hint"
                    on_release:
                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                        regpass.password = False if regpass.password is True else True

            MDGridLayout:
                cols:2
                size_hint_y: None
                height: self.minimum_size[1]
                pos_hint: {"center_x": .5, "center_y": .23}
                padding:dp(10)
                MDTextField:
                    id: regpasscon
                    hint_text: 'confirm password'
                    password: True
                    icon_left: "key-variant"
                    mode: 'round'
                    line_anim: 'True'
                    

                MDIconButton:
                    icon: "eye-off"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    pos: regpasscon.width - self.width + dp(8), 0
                    theme_text_color: "Hint"
                    on_release:
                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                        regpasscon.password = False if regpasscon.password is True else True

            Button:
                text: "Add User"
                font_size: "20sp"
                size_hint: .4, .06
                pos_hint: {"center_x": .5, "center_y": .1}
                background_color: 0, 0, 0, 0
                on_release: app.add_user(regname.text, regpass.text)
                canvas.before:
                    Color: 
                        rgb: 246/255, 135/255, 177/255, 1
                    RoundedRectangle:
                        size: self.size
                        pos: self.pos
                        radius: [23]


    MDScreen:
        id: 'resources'
        name: 'resources'
        md_bg_color: 1, 1, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: .9, .9, .9, .7
            MDGridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    padding:dp(10)
                    spacing:dp(10)
                    MDIconButton:
                        icon: "arrow-left"
                        color: "blue"
                        on_press: root.current = 'home'

                    MDBoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_y':0.5}
                        spacing:dp(10)
                        MDLabel:
                            text: "Resources"
                            font_style: "H6"
                            color: "black"
                            halign: "left"
                            text_size: (200, None)
                            size_hint_x: .4

            MDCard:
                md_bg_color: 1, 1, 1, 1
                radius: [50, 50, 0, 0]
                padding: dp(10)
                MDGridLayout:
                    padding: '10dp'
                    spacing: '10dp'
                    cols: 1
                    MDLabel:
                        size_hint: 1, None
                        text: 'Download revision materials bellow'
                        halign: 'center'
                        font_style: 'H5'
                        color: .5, .3, .7, .6

                    MDBoxLayout:
                        ScrollView:
                            MDGridLayout:
                                id: addreslist
                                padding: '10dp'
                                spacing: '10dp'
                                cols: 1
                                size_hint: 1, None
                                height: self.minimum_size[1]


                    MDFloatLayout:
                        id:addrsbtn
                         
    MDScreen:
        id: 'manusers'
        name: 'manusers'
        md_bg_color: 1, 1, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: .9, .9, .9, .7
            MDGridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    padding:dp(10)
                    spacing:dp(10)
                    MDIconButton:
                        icon: "arrow-left"
                        color: "blue"
                        on_press: root.current = 'home'

                    MDBoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_y':0.5}
                        spacing:dp(10)
                        MDLabel:
                            text: "Manage Mashule Users"
                            font_style: "H6"
                            color: "black"
                            halign: "left"
                            text_size: (200, None)
                            size_hint_x: .4

            MDCard:
                md_bg_color: 1, 1, 1, 1
                radius: [50, 50, 0, 0]
                padding: dp(10)
                MDGridLayout:
                    padding: '10dp'
                    spacing: '10dp'
                    cols: 1
                    MDLabel:
                        size_hint: 1, None
                        text: 'Admin page For managing Users'
                        halign: 'center'
                        font_style: 'H5'
                        color: .5, .3, .7, .6

                    MDBoxLayout:
                        ScrollView:
                            MDGridLayout:
                                id: addreslist
                                padding: '10dp'
                                spacing: '10dp'
                                cols: 1
                                size_hint: 1, None
                                height: self.minimum_size[1]

    MDScreen:
        id: 'manschools'
        name: 'manschools'
        md_bg_color: 1, 1, 1, 1
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: .9, .9, .9, .7
            MDGridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    size_hint_y: None
                    height: self.minimum_height
                    padding:dp(10)
                    spacing:dp(10)
                    MDIconButton:
                        icon: "arrow-left"
                        color: "blue"
                        on_press: root.current = 'home'

                    MDBoxLayout:
                        size_hint_y: None
                        height: self.minimum_height
                        pos_hint: {'center_y':0.5}
                        spacing:dp(10)
                        MDLabel:
                            text: "Manage Mashule Schools"
                            font_style: "H6"
                            color: "black"
                            halign: "left"
                            text_size: (200, None)
                            size_hint_x: .4

            MDCard:
                md_bg_color: 1, 1, 1, 1
                radius: [50, 50, 0, 0]
                padding: dp(10)
                MDGridLayout:
                    padding: '10dp'
                    spacing: '10dp'
                    cols: 1
                    MDLabel:
                        size_hint: 1, None
                        text: 'Schools Management Panel'
                        halign: 'center'
                        font_style: 'H5'
                        color: .5, .3, .7, .6

                    MDBoxLayout:
                        ScrollView:
                            MDGridLayout:
                                id: addreslist
                                padding: '10dp'
                                spacing: '10dp'
                                cols: 1
                                size_hint: 1, None
                                height: self.minimum_size[1]

    MDScreen:
        id: 'addschool'
        name: 'addschool'
        MDFloatLayout:
            md_bg_color: 1, 1, 1, 1
            MDIconButton:
                icon: "arrow-left"
                color: "blue"
                on_press: root.current = 'home'
                pos_hint: {"center_x": .08, "center_y": .97}

            MDLabel:
                text: "Add School"
                pos_hint: {"center_x": .5, "center_y": .9}
                halign: "center"
                underline: True
                font_size: "40sp"
                theme_text_color: "Custom"
                color: 60/255, 43/255, 117/255, 1

            #Image:
            #    source: "images//logo.png"
            #    size_hint: .6, .4
            #    pos_hint: {"center_x": .5, "center_y": .8}
                
            MDTextField:
                id: schoolname
                hint_text: "School Name"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .7}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDTextField:
                id: schooladress
                hint_text: "Adress"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .6}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDTextField:
                id: schoolweb
                hint_text: "Website link"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .5}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDTextField:
                id: schoolemail
                hint_text: "Email"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .4}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDTextField:
                id: schoolcontact
                hint_text: "Contact"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .3}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDTextField:
                id: schoolcat
                hint_text: "Category"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .2}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'     

            MDTextField:
                id: schoolLevel
                hint_text: "School Level"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y": .1}
                icon_left: "account"
                mode: 'round'
                line_anim: 'True'

            MDRaisedButton:
                text: "Submit"
                md_bg_color: "red"
                pos_hint: {"center_x": .5, "center_y": .03}
                on_release: app.add_school(schoolname.text, schooladress.text, schoolweb.text, schoolemail.text, schoolcontact.text, schoolcat.text, schoolLevel.text)

    MDScreen:
        name: 'school'
        MDBottomNavigation:
            id: btmnav
            panel_color: .9, .9, .9, .7
            text_color_active: 8/255, 3/255, 147/255, 1
            text_color_normal: 0, 0, 0, 1
            MDBottomNavigationItem:
                name: 'abuot'
                text: 'About'
                icon: 'information-outline'
                MDBoxLayout:
                    md_bg_color: 1, 1, 1, 1
                    orientation: "vertical"
                    MDGridLayout:
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height
                        MDBoxLayout:
                            size_hint_y: None
                            height: self.minimum_height
                            padding:dp(10)
                            spacing:dp(10)
                            MDIconButton:
                                icon: "arrow-left"
                                color: "blue"
                                on_press: root.current = 'home'

                            MDBoxLayout:
                                size_hint_y: None
                                height: self.minimum_height
                                pos_hint: {'center_y':0.5}
                                spacing:dp(10)
                                MDLabel:
                                    id:schabname
                                    #text: "About Kanyawanga"[0:18]
                                    font_style: "H6"
                                    color: "black"
                                    halign: "left"
                                    text_size: (200, None)
                                    size_hint_x: .4

                            MDIconButton:
                                icon: "pencil"
                                color: "blue"
                                on_press: root.current = 'addschool'


                    MDCard:
                        md_bg_color: 1, 1, 1, 1
                        elevation: 2
                        size_hint: .85, .6
                        pos_hint: {"center_x": .5, "center_y": .5}
                        radius: [10]
                        MDGridLayout:
                            padding: '5dp'
                            spacing: '10dp'
                            cols: 1
                            size_hint: 1, .6
                            height: self.minimum_size[1]
                            pos_hint: {"center_x": .5, "center_y": .5}
                            MDCard:
                                md_bg_color: .9, .9, .9, .7
                                elevation: 5
                                size_hint: 1, .2
                                padding: '10dp'
                                spacing: '10dp'
                                radius: [10]
                                MDLabel:
                                    text: 'Call:'
                                    pos_hint: {"center_x": .1, "center_y": .5}
                                    valign: 'center'
                                    adaptive_size: True
                                    text_color: 'white'
                                    font_style: 'Body1' 

                                MDLabel:
                                    id:schconta
                                    pos_hint: {"center_x": .95, "center_y": .5}
                                    adaptive_size: True
                                    text_color: 'white'
                                    font_style: 'Body1'

                            MDCard:
                                md_bg_color: .9, .9, .9, .7
                                elevation: 5
                                size_hint: 1, .2
                                radius: [10]
                                padding: '5dp'
                                spacing: '10dp'
                                MDLabel:
                                    text: 'Email:'
                                    pos_hint: {"center_x": .1, "center_y": .5}
                                    adaptive_size: True

                                MDLabel:
                                    id:schemai
                                    text: 'schoolmail@gmail.com'
                                    pos_hint: {"center_x": .95, "center_y": .5}
                                    hint_size: None, None
                                    adaptive_size: True

                            MDCard:
                                md_bg_color: .9, .9, .9, .7
                                elevation: 5
                                size_hint: 1, .2
                                radius: [10]
                                padding: '5dp'
                                spacing: '10dp'
                                MDLabel:
                                    text: 'website:'
                                    pos_hint: {"center_x": .1, "center_y": .5}
                                    adaptive_size: True

                                MDLabel:
                                    id:schwebs
                                    pos_hint: {"center_x": .95, "center_y": .5}
                                    hint_size: None, None
                                    adaptive_size: True

                            MDCard:
                                md_bg_color: .9, .9, .9, .7
                                elevation: 5
                                size_hint: 1, .2
                                radius: [10]
                                padding: '5dp'
                                spacing: '10dp'
                                MDLabel:
                                    text: 'Address:'
                                    pos_hint: {"center_x": .1, "center_y": .5}
                                    adaptive_size: True

                                MDLabel:
                                    id:schaddr
                                    pos_hint: {"center_x": .95, "center_y": .5}
                                    hint_size: None, None
                                    adaptive_size: True


            MDBottomNavigationItem:
                name: 'events'
                text: 'Events'
                icon: 'rotate-orbit'
                MDBoxLayout:
                    orientation: "vertical"
                    panel_color: .9, .9, .9, 1
                    MDGridLayout:
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height
                        MDBoxLayout:
                            size_hint_y: None
                            height: self.minimum_height
                            padding:dp(10)
                            spacing:dp(10)
                            MDIconButton:
                                icon: "arrow-left"
                                color: "blue"
                                on_press: root.current = 'home'

                            MDBoxLayout:
                                size_hint_y: None
                                height: self.minimum_height
                                pos_hint: {'center_y':0.5}
                                spacing:dp(10)
                                MDLabel:
                                    text: "Activities"
                                    font_style: "H6"
                                    color: "black"
                                    halign: "left"
                                    text_size: (200, None)
                                    size_hint_x: .4

                    MDCard:
                        md_bg_color: 1, 1, 1, 1
                        radius: [50, 50, 0, 0]
                        padding: dp(10)
                        MDBoxLayout:
                            ScrollView:
                                MDGridLayout:
                                    padding: '10dp'
                                    spacing: '10dp'
                                    cols: 1
                                    size_hint: 1, None
                                    height: self.minimum_size[1]
                                    MDSmartTile:
                                        radius: 24
                                        lines: 2
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 1, 1, 1, .2
                                        source: "images/school2.png"
                                        size_hint: None, None
                                        size: "280dp", "200dp"
                                        box_color: 0, 0, 1, 1
                                        overlap: True

                                        MDIconButton:
                                            icon: "heart-outline"
                                            theme_icon_color: "Custom"
                                            icon_color: 1, 0, 0, 1
                                            pos_hint: {"center_y": .5}
                                            on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                        TwoLineListItem:
                                            text: "Tree Planting day"
                                            secondary_text: "23/01/2023"
                                            bold: True
                                            color: 1, 0, 0, 1


                                    MDSmartTile:
                                        radius: 24
                                        lines: 2
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 1, 1, 1, .2
                                        source: "images/school2.png"
                                        size_hint: None, None
                                        size: "280dp", "200dp"
                                        box_color: 0, 0, 1, 1
                                        overlap: True

                                        MDIconButton:
                                            icon: "heart-outline"
                                            theme_icon_color: "Custom"
                                            icon_color: 1, 0, 0, 1
                                            pos_hint: {"center_y": .5}
                                            on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                        TwoLineListItem:
                                            text: "Tree Planting day"
                                            secondary_text: "23/01/2023"
                                            bold: True
                                            color: 1, 0, 0, 1

                                    MDSmartTile:
                                        radius: 24
                                        lines: 2
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 1, 1, 1, .2
                                        source: "images/school2.png"
                                        size_hint: None, None
                                        size: "280dp", "200dp"
                                        box_color: 0, 0, 1, 1
                                        overlap: True

                                        MDIconButton:
                                            icon: "heart-outline"
                                            theme_icon_color: "Custom"
                                            icon_color: 1, 0, 0, 1
                                            pos_hint: {"center_y": .5}
                                            on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                        TwoLineListItem:
                                            text: "Tree Planting day"
                                            secondary_text: "23/01/2023"
                                            bold: True
                                            color: 1, 0, 0, 1

                                    MDSmartTile:
                                        radius: 24
                                        lines: 2
                                        box_radius: [0, 0, 24, 24]
                                        box_color: 1, 1, 1, .2
                                        source: "images/school2.png"
                                        size_hint: None, None
                                        size: "280dp", "200dp"
                                        box_color: 0, 0, 1, 1
                                        overlap: True

                                        MDIconButton:
                                            icon: "heart-outline"
                                            theme_icon_color: "Custom"
                                            icon_color: 1, 0, 0, 1
                                            pos_hint: {"center_y": .5}
                                            on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

                                        TwoLineListItem:
                                            text: "Tree Planting day"
                                            secondary_text: "23/01/2023"
                                            bold: True
                                            color: 1, 0, 0, 1  

                #MDFloatLayout:
                MDFloatingActionButton:
                    id: button
                    icon: "plus"
                    md_bg_color: 0, 0, 0, 1
                    size_hint: None, None
                    icon_color: 'white'
                    pos_hint: {'center_x':0.9, 'center_y':0.05}
                    on_release: app.AddActivity_dialog_pop(),        
                

            MDBottomNavigationItem:
                name: 'adress'
                text: 'Adress'
                icon: 'map-marker-radius-outline'
                MDBoxLayout:
                    orientation: "vertical"
                    panel_color: .9, .9, .9, .1
                    MDGridLayout:
                        cols: 1
                        size_hint_y: None
                        height: self.minimum_height
                        MDBoxLayout:
                            size_hint_y: None
                            height: self.minimum_height
                            padding:dp(10)
                            spacing:dp(10)
                            MDIconButton:
                                icon: "arrow-left"
                                color: "blue"
                                on_press: root.current = 'home'

                            MDBoxLayout:
                                size_hint_y: None
                                height: self.minimum_height
                                pos_hint: {'center_y':0.5}
                                spacing:dp(10)
                                MDLabel:
                                    text: "Location"
                                    font_style: "H6"
                                    color: "black"
                                    halign: "left"
                                    text_size: (200, None)
                                    size_hint_x: .4

                    MDCard:
                        radius: [50, 50, 0, 0]
                        padding: dp(10)
                        
                        MDBoxLayout:
                            size_hint_y: .9
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            #height: "400dp"
                            orientation: 'vertical'
                            spacing: '10dp'
                            valign: 'top'
                            # MapView:
                            #     lat:11
                            #     lon:11
                            #     double_tap_zoom:True
                            #     zoom:5
                            #     MapMarkerPopup:
                            #         lat:11
                            #         lon:11
                                        
                            

<SignupDC>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "300dp"
    MDTextField:
        hint_text: "Name"

    MDTextField:
        hint_text: "Email Adress"
        

    MDTextField:
        hint_text: "Enter Password"

    MDTextField:
        hint_text: "Re_Enter PassWord"

<LoginDC>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "120dp"
    MDTextField:
        id: email
        hint_text: "Email"
        

    MDTextField:
        id: password
        hint_text: "Enter Password"

<RessPassDC>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "200dp"
    MDTextField:
        hint_text: "Enter Old Password"

    MDTextField:
        hint_text: "Enter New Password"
        

    MDTextField:
        hint_text: "Confirm Password"

<AdresourcesDC>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "80dp"
    GridLayout:
        cols:2
        size_hint_y: None
        height: self.minimum_height
        MDIconButton:
            icon: "plus-circle"
            on_release: app.resourcename_dialog_pop()
            #pos_hint: {'center_x':0.9, 'center_y':0.2}
            
        MDLabel:
            text: "Creat Folder"

        MDIconButton:
            icon: "plus-circle"
            on_release: app.myresourcename_dialog_pop()
            #pos_hint: {'center_x':0.9, 'center_y':0.2}
            
        MDLabel:
            text: "Upload File"


<ReasiurceName>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "30dp"
    MDTextField:
        id:rsstxt
        hint_text: "Folder Name"
        mode: "round"

<ReasiurceobjName>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "60dp"
    MDTextField:
        id:fldntxt
        hint_text: "File Name"
        mode: "round"
    
    MDRaisedButton:
        text: "Upload File"
        md_bg_color: "blue"
        pos_hint: {"center_x": .5, "center_y": .03}
        on_release: app.open_file_manager()

<AddactivityInt>
    orientation: "vertical"
    spacing: "10dp"
    size_hint_y: None 
    height: "50dp"
    MDTextField:
        hint_text: "Activity Tittle"
        mode: "round"

    MDTextField:
        hint_text: "date of activity"
        mode: "round"




'''