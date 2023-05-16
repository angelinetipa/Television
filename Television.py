# class named TV
class TV:
    # constructor channel, volume_level, on
    def __init__(tv, channel, volume_level, on):
        tv.channel = channel
        tv.volume_level = volume_level
        tv.on = on


    # method to turn on
    def turn_on(tv):
        tv.on = True
        return "The TV is on!"
    # method to turn off
    def turn_off(tv):
        tv.on = False
        return "The TV is off!"
    # method to get channel
    def get_channel(tv):
        print(f"The channel for this TV is {tv.channel}")
    # method to set a new channel
    def set_channel(tv, new_channel):
        tv.channel = new_channel
    # method to get volume
    def get_volume(tv):
        print(f"The volume for this TV is {tv.volume_level}")
    # method to set a new volume
    def set_volume(tv, new_volume):
        tv.channel = new_volume
    # method to channel up
    # method to channel down
    # method to volume up
    # method to volumw down
    # call function