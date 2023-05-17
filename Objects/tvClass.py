from tkinter import *
from tkinter import simpledialog

ws = Tk()
class TV:
    #cursorem(runner)
    def __init__(self, channel = 1, volume_level = 1, status = False):
        self.channel = channel
        self.volume_level = volume_level
        self.status = status 

    #TVstatus ON and OFF
    def TV_ON(self):
        self.status = True    
    def TV_OFF(self):
        self.status = False    
        
    #get TV1 channel
    def get_TV1channel(self):
        self.TV1channel = simpledialog.askinteger("CHANNEL", "ENTER TV1 CHANNEL : ", parent=ws)
        return self.TV1channel
    #Set TV1 channel
    def set_TV1channel(self, TV1channel):
        if self.status and 1 <= TV1channel <= 120:
            self.TV1channel = TV1channel
    #get TV2 channel
    def get_TV2channel(self):
        self.TV2channel = simpledialog.askinteger("CHANNEL", "ENTER TV1 CHANNEL : ", parent=ws)
        return self.TV2channel
    #Set TV1 channel
    def set_TV2channel(self, TV2channel):
        if self.status and 1 <= TV2channel <= 120:
            self.TV2channel = TV2channel
            
    #get volume
    def get_volume(self):
        return self.volume
    #set volume
    def set_volume(self, volume):
        if self.status and 1 <= volume <= 7:
            self.volume = volume
    #Channel UP
    def channel_up(self, TVchannel):
        if self.status and 1 <= TVchannel <= 7:
            self.TVchannel += 1        
    #Channel Down
    def channel_up(self, TVchannel):
        if self.status and 1 <= TVchannel  >= 120:
            self.TVchannel += 1        
    #Volume Up
    def volume_up(self, volume):
        if self.status and 1 <= volume <= 7 :
            self.volume += 1
    #method to volume down tv
    def volume_down(self):
        if self.volume > 7:
            self.volume -= 1   
          


        