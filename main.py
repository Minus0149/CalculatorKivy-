from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Config.set('input', 'mouse', 'mouse,disable_multitouch')

Window.clearcolor = (0.5, 0.5, 0.5, 1)
Window.size = (400, 600)


class WidgetExample(BoxLayout):
    def clear(self):
        self.ids.Calculator_display.text = '0'

    def button_press(self, button):
        prior = self.ids.Calculator_display.text
        if prior == "Error":
            prior = ''

        if prior == '0':
            self.ids.Calculator_display.text = ''
            self.ids.Calculator_display.text = f'{button}'
        else:
            self.ids.Calculator_display.text = f'{prior}{button}'

    def math_sign(self, sign):
        prior = self.ids.Calculator_display.text
        ln = len(prior)
        checking = prior[ln-1]
        checked = prior[0:ln-1]
        if "-" in checking:
            self.ids.Calculator_display.text = f'{checked}{checking.replace("-" , sign)}'
        elif "+" in checking:
            self.ids.Calculator_display.text = f'{checked}{checking.replace("+" , sign)}'
        elif "/" in checking:
            self.ids.Calculator_display.text = f'{checked}{checking.replace("/" , sign)}'
        elif "*" in checking:
            self.ids.Calculator_display.text = f'{checked}{checking.replace("*" , sign)}'
        else:
            self.ids.Calculator_display.text = f'{checked}{checking}{sign}'

    def bs(self):
        prior = self.ids.Calculator_display.text
        prior = prior[:-1]
        self.ids.Calculator_display.text = prior

    def ans(self):
        prior = self.ids.Calculator_display.text
        try:
            answer = eval(prior)
            self.ids.Calculator_display.text = str(answer)
        except:
            self.ids.Calculator_display.text = "Error"

    def dot(self):
        prior = self.ids.Calculator_display.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            if prior == "":
                prior = f'{prior}0.'
                self.ids.Calculator_display.text = prior
            else:
                prior = f'{prior}.'
                self.ids.Calculator_display.text = prior
        elif "." in prior:
            pass
        else:
            if prior == "":
                prior = f'{prior}0.'
                self.ids.Calculator_display.text = prior
            else:
                prior = f'{prior}.'
                self.ids.Calculator_display.text = prior

    def percent(self, sing):
        prior = self.ids.Calculator_display.text
        precentage = float(prior)/100
        self.ids.Calculator_display.text = f'{precentage}{sing}'

    def pn(self):
        prior = self.ids.Calculator_display.text
        checking = prior[0:1]
        not_checking = prior[1:]
        if "-" in checking:
            self.ids.Calculator_display.text = f'{checking.replace("-", "", 1)}{not_checking}'
        else:
            self.ids.Calculator_display.text = f'-{checking}{not_checking}'


class Calculator(App):
    pass


Calculator().run()
