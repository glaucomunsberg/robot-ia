
![ESP32-S3](/images/components/esp32-s3-n16r8.jpg){ align=right width="300" }


All steps below are based on the [ESP-IDF Getting Started Guide](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/linux-macos-setup.html#get-started-prerequisites){ target="_blank" }.

Current version used in the project is `ESP-IDF v5.3.2`

### Install requirements

go to home directory

```bash
    cd ~/
```

#### MacOS
Install `cmake`, `ninja` and `dfu-util` to build the firmware.

```bash
    brew install cmake ninja dfu-util
```

#### Ubuntu

```bash
    sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```

Install [`esptool`](https://github.com/espressif/esptool){ target="_blank" } to flash the firmware to the ESP32-S3.

```bash
    pip install esptool
```

Install [`esp-idf`](https://github.com/espressif/esp-idf){ target="_blank" } to build the firmware.

### Install ESP-IDF

```bash
    mkdir -p ~/esp
    cd ~/esp
    git clone -b v5.3.2 --recursive https://github.com/espressif/esp-idf.git
    cd esp-idf
```

Run install ESP32-S3 values

```bash
    cd ~/esp/esp-idf
    ./install.sh esp32s3
```

#### MacOS

Add ESP-IDF to your PATH

```bash
    echo 'alias get_idf=". $HOME/esp/esp-idf/export.sh"' >> ~/.zshrc
```

#### Ubuntu
```bash
    echo 'alias get_idf=". $HOME/esp/esp-idf/export.sh"' >> ~/.bashrc
```

### Install MicroPython

Install MicroPython

```bash
    cd ~/
    git clone git@github.com:micropython/micropython.git
```

Install the cross-compiler

```bash
    cd ~/micropython
    cd mpy-cross
    make
```

### Install Tommy

```bash
    pip3 install tk --break-system-packages
```

#### MacOS

```bash
    brew brew install python-tk@3.12
```

#### Ubuntu

```bash
    sudo apt install python3-tk
```


```bash
    pip3 install thonny --break-system-packages
```

## Upgrade de ESP32-S3 Firmware

```bash
    esptool.py --chip esp32s3 erase_flash
```

Download the latest firmware from the [ESP32-S3 Generic](https://micropython.org/download/ESP32_GENERIC_S3/){ target="_blank" } page.

```bash
    esptool.py --chip esp32s3 write_flash -z 0x1000 ESP32_GENERIC_S3-20241129-v1.24.1.bin
```

!!! note "Firmware version"
    The firmware version used in the project is `ESP32_GENERIC_S3-20241129-v1.24.1.bin`




