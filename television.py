class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Setting the default values:
        -Power status: OFF (False)
        -Mute status: Not muted (False)
        -Volume: Minimum volume
        -Channel: Minimum channel
        -Previous volume: stores the last volume before muting it
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__previous_volume = self.MIN_VOLUME

    def power(self) -> None:
        """
        Switches the power status of the Television,
        if the Tv is off, it turns on, if the tv is on, it turns off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Initiates the mute status of the Television.
        If muted, restores the volume to its previous value.
        If unmuted, saves the current volume and sets it to the minimum.
        """
        if self.__status:
           if self.__muted:
               self.__muted = False
               self.__volume = self.__previous_volume
           else:
               self.__muted = True
               self.__previous_volume = self.__volume
               self.__volume = self.MIN_VOLUME


    def channel_up(self) -> None:
        """
        Increases the channel by 1
        If the current channel is the maximum
        it will loop back to the minimum channel
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by 1
        If the current channel is the minimum
        it will loop back to the maximum channel.
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1, up to the maximum volume
        If the Television is muted it unmutes and restores the previous volume
        before adjusting it.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 down to the minimum volume
        If the Television is muted it will unmute and restores the previous
        volume before adjusting it.
        :return:
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returning the Televisions statuses
        :return: The status of the Television's current state including: Power, Channel, and Volume.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
