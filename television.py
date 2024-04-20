class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2 
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3 

    def _init_(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def mute(self):
        if self.__status:
            self._muted = not self._muted

    def is_muted(self):
        return self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self._status and not self._muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self._status and not self._muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def _str_(self):
        power_status = 'On' if self.__status else 'Off'
        volume_display = 'Muted' if self._muted else self._volume
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {volume_display}"
