import kivy
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 1)
  
class mainfun(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
class Calculator(App):
   
    def build(self):
        return mainfun()
   
objectforRun = Calculator()
objectforRun.run()
  