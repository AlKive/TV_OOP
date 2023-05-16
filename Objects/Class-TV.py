
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
        