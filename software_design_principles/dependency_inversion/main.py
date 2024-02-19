## ElectricPowerSwitch is dependent on LightBulb

class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.light_bulb = l
        self.on: bool = False

    def press(self) -> None:
        if self.on:
            self.light_bulb.turn_off()
            self.on = False
        else:
            self.light_bulb.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    electric_switch = ElectricPowerSwitch(light_bulb)
    electric_switch.press()
    electric_switch.press()
