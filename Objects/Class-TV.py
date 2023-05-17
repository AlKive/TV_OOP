
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
    def set_TVchannel(self, TVchannel):
        if TVchannel <= 1 and TVchannel >= 120:
            self.TVchannel = TVchannel
            
    #get volume
    def get_volume(self):
        return self.volume
    #set volume
    def set_volume(self, volume):
        if self.status and 1 <= volume <= 7:
            self.volume = volume
            

        