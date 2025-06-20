---
title: Roadmap
description: The roadmap of the project, the features that are implemented and the features that are in progress.
tags:
  - project
  - roadmap
  - robot
  - robot-ia
hide:
  - tags
---

Bellow you can see the roadmap of the project, the features that are implemented and the features that are in progress.

## Body

1. [x] Assemble the chassis
    1. [x] [Assemble the chassis](../assembly/chassis.md)
    2. [x] [Motors and the wheels](../assembly/chassis.md)

2. [ ] Install the components <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    1. [ ] ESP32-S3 <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    2. [x] Buzzer
    3. [x] Ultrasonic sensor
    4. [x] Temperature and humidity sensor <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    5. [ ] Camera
    6. [ ] Display

## Brain

1. [ ] Connect the ESP32-S3 to the components
    1. [ ] Connect the ESP32-S3 to the computer <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    2. [ ] Connect the motors <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    3. [ ] Connect the ESP32-S3 to the power supply <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    4. [ ] Connect the buzzer <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    5. [ ] Connect the ultrasonic sensor <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    6. [ ] Connect the temperature and humidity sensor <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    7. [ ] Connect the display
    8. [ ] Connect the camera

2. [ ] Test the robot
    1. [ ] Test the motors <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    2. [ ] Test the camera <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    3. [ ] Test the buzzer <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    4. [ ] Test the ultrasonic sensor <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    5. [ ] Test the display
    6. [ ] Test the ESP32-S3

### Cognition

1. [ ] Connect the ROBOT microservice with IA model
    1. [ ] Install [ollama](https://ollama.com/){ target="_blank" } in the server
    2. [ ] Download the IA model
    3. [ ] Connect the IA model with the ROBOT microservice to generate the actions
    4. [ ] Show emotions in the display

## Integration

### Application Interface (Brain - Body)

1. [ ] Create a interface to control the robot <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    1. [ ] Connect the ESP32-S3 to the computer <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    2. [ ] Connect the wifi to the robot <small style='color:green'><b>:material-progress-clock: In Progress</b></small>

2. [ ] Create API to control the robot with actions interface
    1. [ ] Service to control the movements of the robot
    2. [ ] Service to control the camera of the robot
    3. [ ] Service to control the buzzer of the robot
    4. [ ] Service to control the ultrasonic sensor of the robot
    5. [ ] Service to control the display of the robot
    6. [ ] Service to control the ESP32-S3 of the robot

### Display

1. [X] Create a react-app application
2. [ ] Create a application to show the current status of the robot <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    1. [ ] Show the sensors data <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    2. [ ] Show the actions taken by the robot <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    3. [ ] Show the emotions of the robot <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
3. [ ] Use [gluestack](https://gluestack.io/) to create the application
    1. [ ] Create a application to control the robot with actions interface <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
    2. [ ] Create a dashboard to show the current status of the robot, show the sensors data and the actions taken by the robot <small style='color:green'><b>:material-progress-clock: In Progress</b></small>
