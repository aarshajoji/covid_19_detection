import mys
import kivy
import sqlite3 as lite
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from os.path import sep, expanduser, isdir, dirname
from kivy.properties import BooleanProperty, ListProperty, StringProperty,ObjectProperty
from kivy.core.text import Label as CoreLabel
from kivy.logger import Logger
from deploy import Myclass
file=""
pred=""
def invalidLogin():
    pop = Popup(title='Invalid Login',
    content=Label(text='Invalid username or password.'),
    size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
    content=Label(text='Please fill in all inputs with valid information.'),
    size_hint=(None, None), size=(400, 400))
    pop.open()

class CreateAccountWindow(Screen):
    docid = ObjectProperty(None)
    namee = ObjectProperty(None)
    password = ObjectProperty(None)
    def submit(self):
        if self.docid.text != "" and self.namee.text != "" :
            if self.password.text != "":
                mys.insert(self.docid.text,self.namee.text,self.password.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.docid.text = ""
        self.password.text = ""
        self.namee.text = ""
class Admin(Screen):
    password = ObjectProperty(None)
    def AdminLogin(self):
        if self.password.text == "" :
            self.reset()
            sm.current = "addisp"
        else:
            invalidLogin()

    def login(self):
        self.reset()
        sm.current = "addisp"

    def home(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.password.text = ""

class AdminDisplay(Screen):
    rows=ListProperty([("Id","Name","Password")])
    #r=ListProperty([("Id","Name","Password")])
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        cur = mys.select()
        #self.r=[('Id','Name','Password'),('Id','Name','Password'),('Id','Name','Password')]
        #print(self.r)
        cur.execute("select * from doctor")
        self.rows = cur.fetchall()
        print(self.rows)
        '''for row in myresult:
        for col in row:
        data=data+col+' '
        data=data+"\n"
        self.result.text=data
        print(type(col))
        '''
        def logout(self):
            sm.current = "login"

class LoginWindow(Screen):
    docid = ObjectProperty(None)
    password = ObjectProperty(None)
    def loginBtn(self):
        if mys.validate(self.docid.text,self.password.text) == True:
            self.reset()
            sm.current = "main"
        else:
            #self.reset()
            invalidLogin()
            #sm.current = "login"

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def createBtn1(self):
        self.reset1()
        sm.current = "create1"

    def reset(self):
        self.docid.text = ""
        self.password.text = ""

    def reset1(self):
        self.password.text = ""

class MainWindow(Screen):
    def logOut(self):
        sm.current = "login"

    def createDisp(self):
        self.ids.image.source="D:\image.png "
        sm.current = "Disp"

    def selected(self,filename):
        global file
        file=filename[0]
        self.ids.image.source = filename[0]
        print(file)
        self.reset()

    def reset(self):
        self.filename= ""

    def show(self):
        global file
        global pred
        pred=Myclass.load(file)
        print(pred)

class Display(Screen):
    val=ObjectProperty(None)
    fil=ObjectProperty(None)
    def view(self):
        global pred
        global file
        val = "The X-ray image is " + pred
        fil=file
        self.tree.text=val
        self.ids.image.source = fil

    def checkanother(self):
        sm.current = "main"

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
sm = WindowManager()
#sm.add_widget(AdminDisplay(name="addisp"))
screens = [LoginWindow(name="login"),
    CreateAccountWindow(name="create"),Admin(name="create1"),
    MainWindow(name="main"),Display(name="Disp"),AdminDisplay(name="addisp")]

for screen in screens:
    sm.add_widget(screen)
sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()