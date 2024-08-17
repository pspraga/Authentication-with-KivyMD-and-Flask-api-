
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
#import sqlite3
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import platform
from kivymd.toast import toast
import requests
import base64


sm=ScreenManager()
class loginPage(Screen):
    def login(self):
        n=self.ids.uname.text
        p=self.ids.passwd.text
        pas=p.encode("ascii")
        base64_bytes = base64.b64encode(pas)
        con_pas = base64_bytes.decode("ascii")
        if(n=="" and p==""):
            toast("Please Enter username and password")
        else:
            try:

                #self.con=pyodbc.connect(driver="ODBC Driver 11 for SQL Server",host="192.168.1.20",user="sa",password="abc@123",database="reg")
                response = requests.post('http://192.168.1.43:5000/login', json={'username': n, 'password': con_pas})
                if response.status_code == 200:
                    sm.current = 'dash'
                
                else:
                    toast("InValid Login")
            except:
                toast("Connection Issue")
                
            
                
    pass
  
    




"""class signupPage(Screen):
    def Submit(self):
        if (self.ids.uname.text=="" and self.ids.email.text=="" and self.ids.passwd.text==""):
            toast("Please Enter All The Field")
        else:
            try:
                name=self.ids.uname.text
                mail=self.ids.email.text
                pas=self.ids.passwd.text
           
                
                
                print("value added")
                sm.current="login"
            except:
                toast("connection issue....")
            
    pass
 """

class dashPage(Screen):
    pass







#sm.current="login"
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="DeepOrange"
        Builder.load_file("ScreenUI.kv")
        #sm=ScreenManager()
#screens=[loginPage(name="login"),signupPage(name="signup")]
        sm.add_widget(loginPage(name="login"))
        #sm.add_widget(signupPage(name="signup"))
        sm.add_widget(dashPage(name="dash"))
        
        
        return sm
if __name__=='__main__':
    
    if(platform == 'android'):
        Window.maximize()
    else:
        Window.size = (420, 720)
    #Window.size=(360,640)
    
    
    MyApp().run()
