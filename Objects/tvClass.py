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
        
    #get TV channel
    def get_TVchannel(self):
        self.TVchannel = simpledialog.askinteger("CHANNEL", "Enter channel number: ", parent=ws)
        return self.TVchannel
    #Set TV channel
    def set_TVchannel(self, TVchannel):
        if self.status and 1 <= TVchannel <= 120:
            self.TVchannel = TVchannel
            
    #get volume
    def get_volume(self):
        self.volume = simpledialog.askinteger("VOLUME", "Select Volume : ", parent=ws)
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
          


        