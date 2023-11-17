class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if not self.__status:
            return
        if not self.__muted:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self):
        if not self.__status:
            return
        if self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self):
        if not self.__status:
            return
        if self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self):
        if not self.__status:
            return
        if self.__muted:
            self.mute()
        if self.__volume == self.MAX_VOLUME:
            return
        self.__volume += 1

    def volume_down(self):
        if not self.__status:
            return
        if self.__muted:
            self.mute()
        if self.__volume == self.MIN_VOLUME:
            return
        self.__volume -= 1

    def __str__(self):
        out_vol = self.__volume
        if self.__muted:
            out_vol = self.MIN_VOLUME
        return f'Power = {self.__status}, Channel; = {self.__channel}, Volume = {out_vol}'
