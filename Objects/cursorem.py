
from tvClass import TV


TV1 = TV()
TV1.TV_ON()
TV1.set_TVchannel(7)
TV1.set_volume(7)
print("TV1 channel is " ,  TV1.get_TVchannel() , " and the volume  is " , TV1.get_volume())
  
TV2 = TV()
TV2.TV_ON()
TV2.set_TVchannel(7)
TV2.set_volume(5)
print("TV2 channel is " ,  TV2.get_TVchannel() , " and the volume  is " , TV2.get_volume())


