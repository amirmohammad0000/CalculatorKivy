##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Import
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.fullscreen = False
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Import


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Import File Style
Builder.load_file("style.kv")
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Import File Style


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Screens
screenManager = ScreenManager()


class Page_Home(Screen):
    pass


class Page_About(Screen):
    pass


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Screens

##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Class Main App
class MainApp(MDApp):
    # Start Function Main App
    def build(self):
        screenManager.add_widget(Page_Home(name="page_home"))
        screenManager.add_widget(Page_About(name="page_about"))
        return screenManager
        # End Function Main App

    # Start Functions For Buttons
    def button_1(self):
        res = self.root.get_screen("page_home").ids.result
        res.text = ""

    def button_2(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text != "":
            res.text += "%"

    def button_3(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text == "":
            res.text += "-"

    def button_4(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text != "":
            res.text += "/"

    def button_5(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "7"

    def button_6(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "8"

    def button_7(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "9"

    def button_8(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text != "":
            res.text += "*"

    def button_9(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "4"

    def button_10(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "5"

    def button_11(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "6"

    def button_12(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text != "":
            res.text += "-"

    def button_13(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "1"

    def button_14(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "2"

    def button_15(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "3"

    def button_16(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text != "":
            res.text += "+"

    def button_17(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "3.1415926536"
        if "3.14159265363.1415926536" in res.text:
            res.text = res.text.replace("3.14159265363.1415926536", "3.1415926536")

    def button_18(self):
        res = self.root.get_screen("page_home").ids.result
        res.text += "0"

    def button_19(self):
        res = self.root.get_screen("page_home").ids.result
        if res.text != "":
            res.text += "."

    def button_20(self):
        res = self.root.get_screen("page_home").ids.result
        if "+=" not in res.text or "-=" not in res.text or "/=" not in res.text or "*=" not in res.text or "%=" not in res.text or ".=" not in res.text:
            try:
                if res.text != "":
                    results = eval(res.text)
                    res.text = str(results)
            except:
                res.text = ""

    # End Functions For Buttons

    # Start Functions For Law Game
    def Law(self):
        res = self.root.get_screen("page_home").ids.result
        # Start If For %
        if "%%" in res.text:
            result = res.text.replace("%%", "%")
            res.text = result

        if "%+" in res.text:
            result = res.text.replace("%+", "+")
            res.text = result

        if "%-" in res.text:
            result = res.text.replace("%-", "-")
            res.text = result

        if "%/" in res.text:
            result = res.text.replace("%/", "/")
            res.text = result

        if "%*" in res.text:
            result = res.text.replace("%*", "*")
            res.text = result

        if "%." in res.text:
            result = res.text.replace("%.", ".")
            res.text = result
        # End If For %

        # Start If For /
        if "//" in res.text:
            result = res.text.replace("//", "/")
            res.text = result

        if "/+" in res.text:
            result = res.text.replace("/+", "+")
            res.text = result

        if "/-" in res.text:
            result = res.text.replace("/-", "-")
            res.text = result

        if "/%" in res.text:
            result = res.text.replace("/%", "%")
            res.text = result

        if "/*" in res.text:
            result = res.text.replace("/*", "*")
            res.text = result

        if "/." in res.text:
            result = res.text.replace("/.", ".")
            res.text = result
        # End If For /

        # Start If For *
        if "**" in res.text:
            result = res.text.replace("**", "*")
            res.text = result

        if "*+" in res.text:
            result = res.text.replace("*+", "+")
            res.text = result

        if "*-" in res.text:
            result = res.text.replace("*-", "-")
            res.text = result

        if "*%" in res.text:
            result = res.text.replace("*%", "%")
            res.text = result

        if "*/" in res.text:
            result = res.text.replace("*/", "/")
            res.text = result

        if "*." in res.text:
            result = res.text.replace("*.", ".")
            res.text = result
        # End If For *

        # Start If For -
        if "--" in res.text:
            result = res.text.replace("--", "-")
            res.text = result

        if "-+" in res.text:
            result = res.text.replace("-+", "+")
            res.text = result

        if "-/" in res.text:
            result = res.text.replace("-/", "/")
            res.text = result

        if "-*" in res.text:
            result = res.text.replace("-*", "*")
            res.text = result

        if "-%" in res.text:
            result = res.text.replace("-%", "%")
            res.text = result

        if "-." in res.text:
            result = res.text.replace("-.", ".")
            res.text = result
        # End If For -

        # Start If For +
        if "++" in res.text:
            result = res.text.replace("++", "+")
            res.text = result

        if "+-" in res.text:
            result = res.text.replace("+-", "-")
            res.text = result

        if "+/" in res.text:
            result = res.text.replace("+/", "/")
            res.text = result

        if "+*" in res.text:
            result = res.text.replace("+*", "*")
            res.text = result

        if "+%" in res.text:
            result = res.text.replace("+%", "%")
            res.text = result

        if "+." in res.text:
            result = res.text.replace("+.", ".")
            res.text = result
        # End If For +

        # Start If For .
        if ".." in res.text:
            result = res.text.replace("..", ".")
            res.text = result

        if ".+" in res.text:
            result = res.text.replace(".+", "+")
            res.text = result

        if ".-" in res.text:
            result = res.text.replace(".-", "-")
            res.text = result

        if "./" in res.text:
            result = res.text.replace("./", "/")
            res.text = result

        if ".*" in res.text:
            result = res.text.replace(".*", "*")
            res.text = result

        if ".%" in res.text:
            result = res.text.replace(".%", "%")
            res.text = result
        # End If For .
    # End Functions For Law Game


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Class Main App


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Run Game
if __name__ == "__main__":
    MainApp().run()
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Run Game
