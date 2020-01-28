from random import random


class Sensor:

    def __init__(self):
        self._sensor_data = 0
        self._pressure = 0

    def sample_pressure(self):
        return_value = random(1, 100)
        return return_value
