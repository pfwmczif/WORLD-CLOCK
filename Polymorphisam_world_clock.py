from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x450")


india_image= ImageTk.PhotoImage(Image.open ("india.jpg"))
usa_image= ImageTk.PhotoImage(Image.open ("usa.png"))
australia_image= ImageTk.PhotoImage(Image.open ("aussie.jpg"))
japan_image= ImageTk.PhotoImage(Image.open ("japan.jpg"))











india_label = Label(root,text="India")
india_label.place(relx=0.2,rely=0.05, anchor=CENTER)

india_image = Label(root)
india_image= ImageTk.PhotoImage(Image.open ("india.jpg"))
india_image.place(relx= 0.2,rely=0.35,anchor = CENTER)


india_time = Label(root)
india_time.place(relx=0.2,rely=0.65,anchor = CENTER)



usa_label = Label(root,text="USA")
usa_label.place(relx=0.7,rely=0.05, anchor=CENTER)

usa_image = Label(root)
usa_image= ImageTk.PhotoImage(Image.open ("usa.png"))
usa_image.place(relx= 0.7,rely=0.35,anchor = CENTER)


usa_time = Label(root)
usa_time.place(relx=0.7,rely=0.65,anchor = CENTER)





australia_label = Label(root,text="Australia")
australia_label.place(relx=0.25,rely=0.5, anchor=CENTER)

australia_image = Label(root)
australia_image= ImageTk.PhotoImage(Image.open ("aussie.jpg"))
australia_image.place(relx= 0.7,rely=0.35,anchor = CENTER)


australia_time = Label(root)
australia_time.place(relx=0.7,rely=0.65,anchor = CENTER)






japan_label = Label(root,text="Japan")
japan_label.place(relx=0.25,rely=0.5, anchor=CENTER)

japan_image = Label(root)
japan_image= ImageTk.PhotoImage(Image.open ("japan.jpg"))
japan_image.place(relx= 0.7,rely=0.35,anchor = CENTER)


japan_time = Label(root)
japan_time.place(relx=0.7,rely=0.65,anchor = CENTER)



class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"]="Time :" + current_time
        india_time.after(200,self.times)
        
        
   
        
class USA():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time :" + current_time
        usa_time.after(200,self.times)
        
        
        
        
        
class Australia():
    def times(self):
        home = pytz.timezone("Australia/ACT")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        australia_time["text"]="Time :" + current_time
        australia_time.after(200,self.times)
        
        
        
class Japan():
    def times(self):
        home = pytz.timezone("Japan")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        japan_time["text"]="Time :" + current_time
        japan_time.after(200,self.times)
        
        
        
obj_india = India()
obj_usa = USA()
obj_australia = Australia()
obj_japan = Japan()
        

india_btn=Button(root,text="Show Time" , command = obj_india.times)  
india_btn.place(relx=0.2,rely=0.8, anchor= CENTER)


usa_btn=Button(root,text="Show Time" , command = obj_usa.times)  
usa_btn.place(relx=0.7,rely=0.8, anchor= CENTER)


australia_btn=Button(root,text="Show Time" , command = obj_australia.times)  
australia_btn.place(relx=0.25,rely=0.92, anchor= CENTER)

japan_btn=Button(root,text="Show Time" , command = obj_japan.times)  
japan_btn.place(relx=0.2,rely=0.8, anchor= CENTER)


root.mainloop()


        
        
        