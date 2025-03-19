# Transfer files to ESP32-S3


## Transfer Files


Go to the root of the project
```bash
cd robot-ai
```


Transfer Files to ESP32-S3
```bash
ampy --port /dev/ttyUSB0 put application/
```


## Run the application

```bash
ampy --port /dev/ttyUSB0 run main.py
```


!!! tip "Tip"
    If you are using a different port, replace `/dev/ttyUSB0` with the correct port, e.g. `/dev/ttyACM0`.