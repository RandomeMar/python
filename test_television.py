import unittest
from television import *

class MyTestCase(unittest.TestCase):
    def test__init__(self):
        tv_1 = Television()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        tv_1 = Television()
        tv_1.power()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 0'
        tv_1.power()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        tv_1 = Television()
        tv_1.power()
        tv_1.volume_up()
        tv_1.mute()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 0'
        tv_1.mute()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 1'
        tv_1.power()
        tv_1.mute()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 1'
        tv_1.power()
        tv_1.mute()
        tv_1.power()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        tv_1 = Television()
        tv_1.channel_up()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'
        tv_1.power()
        tv_1.channel_up()
        assert tv_1.__str__() == f'Power = True, Channel = 1, Volume = 0'
        tv_1.mute()
        tv_1.channel_up()
        assert tv_1.__str__() == f'Power = True, Channel = 2, Volume = 0'
        tv_1.channel_up()
        tv_1.channel_up()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        tv_1 = Television()
        tv_1.channel_down()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'
        tv_1.power()
        tv_1.channel_down()
        assert tv_1.__str__() == f'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        tv_1 = Television()
        tv_1.volume_up()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'
        tv_1.power()
        tv_1.volume_up()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 1'
        tv_1.mute()
        tv_1.volume_up()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 2'
        tv_1.volume_up()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        tv_1 = Television()
        tv_1.volume_down()
        assert tv_1.__str__() == f'Power = False, Channel = 0, Volume = 0'
        tv_1.power()
        tv_1.volume_up()
        tv_1.volume_up()
        tv_1.volume_down()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 1'
        tv_1.mute()
        tv_1.volume_down()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 0'
        tv_1.volume_down()
        assert tv_1.__str__() == f'Power = True, Channel = 0, Volume = 0'









