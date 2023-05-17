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
    @property
    def turn_on(tv):
        tv.on = True
        
    # method to turn off
    def turn_off(tv):
        tv.on = False
        
    # method to get channel
    def get_channel(tv):
        return f"TV's current channel:  {tv.channel}"
    # method to set a new channel
    def set_channel(tv, new_channel):
        tv.channel = new_channel
        return f"TV's new channel:  {tv.channel}"
    # method to get volume
    def get_volume(tv):
        return f"TV'S current volume:  {tv.volume_level}"
    # method to set a new volume
    def set_volume(tv, new_volume):
        tv.volume_level = new_volume
        return f"TV's new volume:  {tv.volume_level}"
    # method to channel up
    def channel_up(tv, channel_up):
        tv.channel += channel_up
        return f"TV's new channel:  {tv.channel}"
    # method to channel down
    def channel_down(tv, channel_down):
        tv.channel -= channel_down
        return f"TV's new channel:  {tv.channel}"
    # method to volume up
    def volume_up(tv, volume_up):
        tv.volume_level += volume_up
        return f"TV's new volume:  {tv.volume_level}"
    # method to volume down
    def volume_down(tv, volume_down):
        tv.volume_level += volume_down
        return f"TV's new volume:  {tv.volume_level}"
