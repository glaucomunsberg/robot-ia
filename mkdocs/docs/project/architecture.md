## High Level Components Architecture


```mermaid
architecture-beta
    group local(cloud)[Network]
    group api(cloud)[API] in local
    group olhama(cloud)[Ollama Server] in local
    group esp32s3(cloud)[ESP S3]
    group sensors(cloud)[Sensors] in esp32s3
    group chassis(cloud)[Chassis] in esp32s3

    %% Internet
    service gateway(carbon:network-public)[Web]

    %% API SERVICES
    service mongoDB(simple-icons:mongodb)[MongoDB] in api
    service serverAPI(carbon:bare-metal-server)[Server] in api

    %% OLLAMA SERVICES
    service ollamaModel(simple-icons:ollama)[Llama32] in olhama

    %% ESP32-S3 SERVICES
    service breadboard(codicon:circuit-board)[Protoboard] in esp32s3
    service microprocessor(heroicons:cpu-chip-16-solid)[microprocessor ESP32_S3] in esp32s3
    service dh11(carbon:temperature)[Temperature and Humidity Sensor] in sensors
    service hcsr04(material-symbols:nest-remote-comfort-sensor-outline)[Ultrasonic Sensor] in sensors
    service buzzer(material-symbols:sound-detection-loud-sound)[Buzzer 5V] in sensors
    service led(heroicons:light-bulb)[LED] in sensors
    service wheelDriver(carbon:asset)[Wheel Driver] in sensors
    service motor1(solar:suspension-bold)[Motor 1] in chassis
    service motor2(solar:suspension-bold)[Motor 2] in chassis
    service motor3(solar:suspension-bold)[Motor 3] in chassis
    service motor4(solar:suspension-bold)[Motor 4] in chassis

    %% connections IN ESP32-S3
    breadboard:R -- L:microprocessor
    dh11:R -- L:breadboard
    hcsr04:R -- L:breadboard
    buzzer:R -- L:breadboard
    led:R -- L:breadboard
    wheelDriver:R -- L:breadboard
    motor1:R -- L:wheelDriver
    motor2:R -- L:wheelDriver
    motor3:R -- L:wheelDriver
    motor4:R -- L:wheelDriver

    %% Connections 
    mongoDB:L -- R:serverAPI
    ollamaModel:T -- B:serverAPI
    microprocessor:R -- L:serverAPI

    serverAPI:B -- R:gateway

```