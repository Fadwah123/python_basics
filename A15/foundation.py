from abc import ABC,abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def power_on(self):
        """Turning on different devices"""
class Smartphone(SmartDevice):
    def power_on(self):
        print("Booting mobile OS...")

class Smartwatch(SmartDevice):
    def power_on(self):
        print("Starting wearable system...")

devices=[Smartphone(),Smartwatch()]

print("Turning on device...")
for device in devices:
    print(f"{device.__class__.__name__}:",end=" ")
    device.power_on()
