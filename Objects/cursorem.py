
from tvClass import TV
from tkinter import messagebox

TV1 = TV()
TV1.TV_ON()
TV1.set_TV1channel()
TV1.set_volume()
messagebox.showinfo("TV1 channel is " ,  TV1.get_TV1channel() , " and the volume  is " , TV1.get_volume())
  
TV2 = TV()
TV2.TV_ON()
TV2.set_TVchannel()
TV2.set_volume()
messagebox.showinfo("TV2 channel is " ,  TV2.get_TVchannel() , " and the volume  is " , TV2.get_volume())


