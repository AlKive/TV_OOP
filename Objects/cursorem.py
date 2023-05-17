
from tvClass import TV

TV1 = TV()
TV1.TV_ON()
TV1.set_TVchannel(1)
print("TV1 channel is " ,  TV1.get_TVchannel() , " and the volume  is " , TV1.get_volume())
  
TV2 = TV()
TV2.TV_ON()
TV2.set_TVchannel(1)
print("TV2 channel is " ,  TV2.get_TVchannel() , " and the volume  is " , TV2.get_volume())


