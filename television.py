class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Method to set default values of television object
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        """
        Method to flip value of status variable
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        """
        Method to flip value of muted variable
        """
        if not self.__status:
            return
        if not self.__muted:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self):
        """
        Method to raise channel level and cycle from the maximum channel to the minimum
        """
        if not self.__status:
            return
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self):
        """
        Method to lower channel level and cycle from the minimum channel to the maximum
        """
        if not self.__status:
            return
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self):
        """
        Method to increase volume level unless volume is maxed out
        """
        if not self.__status:
            return
        if self.__muted:
            self.mute()
        if self.__volume == self.MAX_VOLUME:
            return
        self.__volume += 1

    def volume_down(self):
        """
        Method to decrease volume level unless volume is at its minimum
        """
        if not self.__status:
            return
        if self.__muted:
            self.mute()
        if self.__volume == self.MIN_VOLUME:
            return
        self.__volume -= 1

    def __str__(self) -> str:
        """
        Method that returns power status, channel level, and volume level when the object is printed
        """
        out_vol: int = self.__volume
        if self.__muted:
            out_vol = self.MIN_VOLUME
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {out_vol}'
