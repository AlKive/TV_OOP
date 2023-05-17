
from tvClass import TV
from tkinter import messagebox
TV1 = TV()
TV1.TV_ON()
TV1.set_TVchannel(1)


TV2 = TV()
TV2.TV_ON()
TV2.set_TVchannel(1)

messagebox.showinfo("TELEVISION", "TV1 channel is " + str(TV1.get_TVchannel()) + " and the volume  is " + str(TV1.get_volume()) + 
                    "\nTV2 channel is " + str(TV2.get_TVchannel()) + " and the volume  is " + str(TV2.get_volume()))


