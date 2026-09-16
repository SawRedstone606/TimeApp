from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime

# กำหนดสีพื้นหลัง (โทนเข้ม)
Window.clearcolor = (0.05, 0.05, 0.08, 1)

class TimeApp(App):
    def build(self):
        # จัดวางแบบแนวตั้ง (แสดงเวลา + วันที่)
        layout = BoxLayout(orientation='vertical', padding=20)
        
        # แสดงเวลา
        self.time_label = Label(
            text="", 
            font_size='50sp', 
            bold=True,
            color=(0.2, 0.9, 0.6, 1)
        )
        
        # แสดงวันที่
        self.date_label = Label(
            text="", 
            font_size='20sp',
            color=(0.7, 0.7, 0.7, 1)
        )
        
        layout.add_widget(self.time_label)
        layout.add_widget(self.date_label)
        
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)
        return layout

    def update_time(self, dt):
        now = datetime.now()
        self.time_label.text = now.strftime("%H:%M:%S")
        self.date_label.text = now.strftime("%A, %d %B %Y")

if __name__ == '__main__':
    TimeApp().run()
