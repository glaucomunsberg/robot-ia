import time
import network  # pylint: disable=import-error
import ntptime  # pylint: disable=import-error
import webrepl  # pylint: disable=import-error
from machine import RTC  # pylint: disable=import-error
from common.variables import Variables


class Wifi:
    """Docstring for Wifi. """
    _instance = None
    code = None
    variables = None
    wifi = None
    tries = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.variables = Variables()

        return cls._instance

    def __init__(self):
        if self.wifi is None:
            self.wifi = network.WLAN(network.STA_IF)
            ip = self.variables.get_value(['communication', 'wifi', 'ip'])
            subnet = self.variables.get_value(
                ['communication', 'wifi', 'subnet'])
            gateway = self.variables.get_value(
                ['communication', 'wifi', 'gateway'])
            dns = self.variables.get_value(['communication', 'wifi', 'dns'])
            if ip is not None:
                self.wifi.ifconfig((ip, subnet, gateway, dns))
            wifi_ssid = self.variables.get_value(
                ['communication', 'wifi', 'ssid'])
            wifi_password = self.variables.get_value(
                ['communication', 'wifi', 'password'])

            if wifi_ssid is None or wifi_password is None:
                print("Wi-Fi SSID or password not found in the configuration file.")
                return
            self.wifi.active(True)
            self.wifi.connect(wifi_ssid, wifi_password)

            while not self.wifi.isconnected() and self.tries < 10:
                self.tries += 1
                print("Conectando ao Wi-Fi...")
                time.sleep(1)

            if self.wifi.isconnected():
                try:
                    rtc = RTC()
                    ntptime.settime()
                    (year, month, day, _, hours, minutes,
                     seconds, _) = rtc.datetime()
                    print(
                        f"UTC Time: {year}-{month}-{day} {hours}:{minutes}:{seconds}")

                    timezone_offset = self.variables.get_value(
                        ['time', 'timezone_offset'])

                    if timezone_offset is not None:
                        hours = hours + timezone_offset

                    rtc.datetime(
                        (year, month, day, 0, hours, minutes, seconds, 0))
                except OSError as error:
                    print(f"Wifi Error: {error}")

                try:
                    can_enable = self.variables.get_value(
                        ['communication', 'web_repl', 'enabled'])
                    if can_enable is not None and can_enable:
                        webrepl.start()
                except Exception as error:  # pylint: disable=broad-except
                    print(f"WebREPL Error: {error}")

    def is_connected(self) -> bool:
        """Check if the Wi-Fi is connected
        """
        return self.wifi.isconnected()

    def disconnect(self) -> None:
        """Disconnect the Wi-Fi
        """
        self.wifi.disconnect()
        self.wifi.active(False)

    def __del__(self):
        """Disconnect the Wi-Fi when the object is deleted"""
        self.disconnect()
        print("Wi-Fi disconnected")
