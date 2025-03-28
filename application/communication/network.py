import time
import network


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
            # cls.variables = Variables().configs

        return cls._instance

    def __init__(self):
        if self.wifi is None:
            self.wifi = network.WLAN(  # pylint: disable=no-member
                network.STA_IF)  # pylint: disable=no-member
            self.wifi.ifconfig(
                ('192.168.18.21', '255.255.255.0', '192.168.18.1', '8.8.8.8'))
            self.wifi.active(True)
            wifi_ssid = "OsirMax_Anascience_5G"  # Substitua pelo nome da sua rede Wi-Fi
            wifi_password = "20102020"  # Substitua pela senha do Wi-Fi)
            self.wifi.connect(wifi_ssid, wifi_password)

            while not self.wifi.isconnected() and self.tries < 10:
                self.tries += 1
                print("Conectando ao Wi-Fi...")
                time.sleep(1)

    def is_connected(self) -> bool:
        """Check if the Wi-Fi is connected
        """
        return self.wifi.isconnected()
