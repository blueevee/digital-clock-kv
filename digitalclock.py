from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from time import strftime, sleep, time
import sched

class CronoWidget(BoxLayout):
    cronoValueText = StringProperty()
 
    def update(self, *args):
        self.cronoValueText= strftime("%H:%M:%S")

class DigitalClock(MDApp):

    def build (self):
        cronos = CronoWidget()
        Clock.schedule_interval(cronos.update,1)
        return cronos      


DigitalClock().run()