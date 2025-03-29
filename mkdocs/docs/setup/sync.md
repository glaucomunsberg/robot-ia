# Transfer files to ESP32-S3


## Transfer Files


Go to the root of the project
```bash
cd robot-ai
```

Transfer Files to ESP32-S3. We use the [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html){ target="_blank" } tool to transfer files to the ESP32-S3, feel free to use any other tool you prefer.

```bash
mpremote fs cp -r application :/
```


## Run the application

```bash
mpremote run application/main.py
```


!!! tip "Tip"
    If you are using a different port, replace `/dev/ttyUSB0` with the correct port, e.g. `/dev/ttyACM0`.