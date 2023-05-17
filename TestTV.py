# import television
from Television import TV

# create tv1 
tv1 = TV(30, 3, False)
print(f"\ntv1's channel is {tv1.channel} and volume level is {tv1.volume_level}")
 # create tv2
tv2 = TV(3, 2, True)
print(f"\ntv2's channel is {tv2.channel} and volume level is {tv2.volume_level}\n")

# calling methods
print(tv1.turn_on())
print(tv1.get_channel())
print(tv1.set_channel(50))
print(tv1.get_volume())
print(tv1.set_volume(6))
print(tv1.channel_up(3))
print(tv1.channel_down(1))
print(tv1.volume_up(1))
print(tv1.volume_down(3))