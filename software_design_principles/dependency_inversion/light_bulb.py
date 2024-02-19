from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on: bool = False

    def press(self) -> None:
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    electric_switch = ElectricPowerSwitch(light_bulb)
    electric_switch.press()
    electric_switch.press()
