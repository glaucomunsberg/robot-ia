---
title: Configuration File
description: The configuration file for the Robot AI environment.
tags:
  - setup
  - development
  - config
  - robot-ia.json
  - debugging
  - Web REPL
  - wifi
hide:
  - tags
---

The file `robot-ia.json` is used to configure the Robot AI environment. It contains the following fields:

```json
{
  "name": "robot-ia",
    "description": "Robot IA",
    "version": "0.0.1",
    "debug": true,
    "configs": {
      // ...
      "wifi": {
        "ssid": "my_wifi_name",
        "password": "my_wifi_password"
        // ...
      }
      // ...
    }
  }
```

## Fields Structure

The JSON file is structured to include the following sections:

- `robot`: Contains information about the robot, such as its name, version, and description.
- `configs`: Contains configuration settings for the environment, such as Wi-Fi SSID and password.

``` json
{
    "name": "robot-ia",
    "description": "Robot IA",
    "version": "0.0.1",
    "debug": true,
    "configs": {
      "time": {
        "timezone": "America/Sao_Paulo",
        "timezone_offset": -3
      },
      "communication": {
        "web_repl": {
          "enabled": true
        },
        "wifi": {
          "ssid": "my_wifi_name",
          "password": "my_wifi_password",
          "ip": "192.168.18.21",
          "subnet": "255.255.255.0",
          "gateway": "192.168.18.1",
          "dns": "8.8.8.8"
        }
      },
      "api": {
        "server": {
          "port": 80
        }
      }
    }
}
```

## Usage

1. Open the `robot-ai.json` file in your preferred text editor.
2. Modify the fields as needed.
3. Save the file.
4. Run the application to apply the changes.
5. The application will read the configuration from the `robot-ai.json` file and apply the settings.

!!! note "Important Note"
    - Ensure that the JSON structure is maintained while editing the file.
    - Use double quotes for keys and string values.
    - Avoid trailing commas after the last item in objects or arrays.

### Configuration Details

#### Common Fields

- `name`: The name of the robot.
- `description`: A brief description of the robot.
- `version`: The version of the robot software.
- `debug`: A boolean value indicating whether debug mode is enabled or not showing debug information in the logs.

#### Communication Settings

##### Web REPL

- `enabled`: A boolean value indicating whether Web REPL is enabled or not. If set to `true`, you can access the Web REPL interface.

##### Wi-Fi

- `ssid`: The SSID of the Wi-Fi network to connect to.
- `password`: The password for the Wi-Fi network.
- `ip`: The static IP address to assign to the robot.
- `subnet`: The subnet mask for the network.
- `gateway`: The gateway IP address for the network.
- `dns`: The DNS server to use for name resolution.

!!! note "Configuration Notes"
    - The `wifi->ssid` and `wifi->password` fields are essential for the robot to connect to the Wi-Fi network.
    - The `ip`, `subnet`, `gateway`, and `dns` fields are optional and can be set according to your network configuration.

#### API

Contains settings for the API server.

- `port`: The port on which the API server will listen for incoming requests.
