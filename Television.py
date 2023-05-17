# class named TV
class TV:
    # constructor channel, volume_level, on
    def __init__(tv, channel, volume_level, on):
        tv.channel = channel
        # raise ValueError
        if channel <= 0 and channel >= 121:
            raise ValueError(f"channel expected only 1 to 120, got {channel}")
        tv.volume_level = volume_level
        if volume_level <= 0 and volume_level >= 8:
            raise ValueError(f"channel expected only 1 to 7, got {volume_level}")
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
        tv.volume_level = new_volume
    # method to channel up
    def channel_up(tv, channel_up):
        tv.channel += channel_up
    # method to channel down
    def channel_down(tv, channel_down):
        tv.channel -= channel_down
    # method to volume up
    def volume_up(tv, volume_up):
        tv.volume_level += volume_up
    # method to volume down
    def volume_down(tv, volume_down):
        tv.volume_level += volume_down
