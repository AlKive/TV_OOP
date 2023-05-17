
class TV:
    #cursorem(runner)
    def __init__(self, TVchannel):
        self.TVchannel = 1
        self.TVchannel = TVchannel 
    def __init__(self, status):    
        self.status = False
        self.status = status
    def __init__(self, volume):
        self.volume = 1
        self.volume = volume   

    #TVstatus ON and OFF
    def TV_ON(self):
        self.status = True    
    def TV_OFF(self):
        self.status = False    
        
    #get TV channel
    def get_TVchannel(self):
        return self.TVchannel
    #Set TV channel
    def set_TVchannel(self):
        if self.status and 1<= TVchannel >= 120:
            TVchannel = TVchannel
            
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
    def volume_up(self):
        if self.volume > 7:
            self.volume += 1
    #method to volume down tv
    def volume_down(self):
        if self.volume > 7:
            self.volume -= 1   
          


        