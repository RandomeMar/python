class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to set default values of television object
        :return: None
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to flip value of status variable
        :return: None
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to flip value of muted variable
        :return: None
        """
        if not self.__status:
            return
        if not self.__muted:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self) -> None:
        """
        Method to raise channel level and cycle from the maximum channel to the minimum
        :return: None
        """
        if not self.__status:
            return
        if self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to lower channel level and cycle from the minimum channel to the maximum
        :return: None
        """
        if not self.__status:
            return
        if self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase volume level unless volume is maxed out
        :return: None
        """
        if not self.__status:
            return
        if self.__muted:
            self.mute()
        if self.__volume == Television.MAX_VOLUME:
            return
        self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease volume level unless volume is at its minimum
        :return: None
        """
        if not self.__status:
            return
        if self.__muted:
            self.mute()
        if self.__volume == Television.MIN_VOLUME:
            return
        self.__volume -= 1

    def __str__(self) -> str:
        """
        Method that returns power status, channel level, and volume level when the object is printed
        :return: String containing the status, channel, and volume variables
        """
        out_vol: int = self.__volume
        if self.__muted:
            out_vol = Television.MIN_VOLUME
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {out_vol}'
