---
title: Syncing Files to ESP32-S3
description: How to transfer files to the ESP32-S3 using MicroPython tools like mpremote and WebREPL.
tags:
  - setup
  - advanced
  - mpremote
  - robot-ai.json
  - development
  - Web REPL
hide:
  - tags
---

## MicroPython Remote

The `mpremote` tool is a command-line utility for interacting with MicroPython devices over a serial connection. It allows you to execute commands, transfer files, and manage the file system on the device.

### Transfer Files

Go to the root of the project

```bash
cd robot-ai
```

Transfer Files to ESP32-S3. We use the [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html){ target="_blank" } tool to transfer files to the ESP32-S3, feel free to use any other tool you prefer.

```bash
mpremote fs cp -r application :/
```

### Run the application

```bash
mpremote run application/main.py
```

!!! tip "Tip"
    If you are using a different port, replace `/dev/ttyUSB0` with the correct port, e.g. `/dev/ttyACM0`. Check the port with the command `mpremote connect list`.

## WebREPL

WebREPL is a web-based REPL (Read-Eval-Print Loop) for MicroPython devices. It allows you to interact with the device through a web browser, making it easier to run commands and manage files without needing a serial connection.

### Enable WebREPL

To enable WebREPL, you need to change the configuration in the `robot-ai.json` file. Open the file and ensure the following section is present:

```json
{
    // Other configuration settings...
    "communication": {
        "web_repl": {
            "enabled": true
        }
    }
    // ... Other configuration settings...
}
```

### Browser Access

After enabling WebREPL, you can access it by navigating to the following URL in your web browser:

```plaintext
    http://<ESP32-S3_IP>:8266
```

Find the IP address of your ESP32-S3 in the `robot-ai.json` file under the `communication` section, or use the default IP address if you haven't changed it.
