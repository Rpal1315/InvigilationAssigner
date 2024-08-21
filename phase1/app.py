KV = """
ScreenManager:
    id: sm
    MDScreen:
        id: screen_home
        md_bg_color: self.theme_cls.secondaryContainerColor

        MDTopAppBar:
            type: "small"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .5}

            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "menu"
                    on_release: nav_drawer.set_state("toggle")

            MDTopAppBarTitle:
                id: title
                text: "Invigilation Assigner"
                pos_hint: {}

            MDTopAppBarTrailingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "account-circle-outline"

        MDNavigationDrawer:
            # Add Navigation Drawer Panel Content here.
            id: nav_drawer_home
            radius: 0, dp(16), dp(16), 0
            MDNavigationDrawerMenu:
                # Add Navigation Drawer Menu Items here.
                MDNavigationDrawerLabel:
                    text: "Menu"
                MDNavigationDrawerItem:
                    on_release: sm.current = "screen_2"
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "wrench"

                    MDNavigationDrawerItemText:
                        text: "Setup"
    MDScreen:
        id: screen_2
        md_bg_color: self.theme_cls.secondaryContainerColor

        MDTopAppBar:
            type: "small"
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .5}

            MDTopAppBarLeadingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "menu"
                    on_release: nav_drawer.set_state("toggle")

            MDTopAppBarTitle:
                id: title
                text: "Invigilation Assigner"
                pos_hint: {}

            MDTopAppBarTrailingButtonContainer:

                MDActionTopAppBarButton:
                    icon: "account-circle-outline"

        MDNavigationDrawer:
            # Add Navigation Drawer Panel Content here.
            id: nav_drawer2
            radius: 0, dp(16), dp(16), 0
            MDNavigationDrawerMenu:
                # Add Navigation Drawer Menu Items here.
                MDNavigationDrawerLabel:
                    text: "Menu"
                MDNavigationDrawerItem:
                    on_release: sm.current = "screen_2"
                    MDNavigationDrawerItemLeadingIcon:
                        icon: "wrench"

                    MDNavigationDrawerItemText:
                        text: "Setup"

"""
from kivymd.app import MDApp
from kivy.lang import Builder


class MainApp(MDApp):
    def build(self):
        global apps_build
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Beige"
        apps_build= Builder.load_string(KV)
        return apps_build

    def toggle_nav_drawer(self):
        print("v")

    def on_start(self):
        print(apps_build.ids)
        # apps_build.ids["sm"].current = 'screen_home'
        self.app = self


MainApp().run()
