#!/bin/bash

# GET THE FIRST PARAMETER PASSED TO THE SCRIPT
# IF THE PARAMETER IS NOT EMPTY, SET TO SYNC THE FILES
if [ -z "$1" ]
then
    SYNC_FILES="false"
else
    SYNC_FILES="true"
fi

# VARIABLE IF THE PORT IS /dev/ttyUSB0 OR /dev/ttyACM0
if [ -e /dev/ttyUSB0 ]
then
    PORT="/dev/ttyUSB0"
else
    PORT="/dev/ttyACM9"
fi

# find the /dev/ttyACM* port
if [ -e /dev/ttyACM* ]
then
    PORT="/dev/ttyACM*"
fi

echo ""
echo "ROBOT IA - RUNNING SCRIPT"
echo "==========================="
echo "PORT CONFIGURATION"
echo "Port: $PORT"
echo "Done!"
echo "---------------------------"

# Delete all folders called __pycache__ and all files with extension .pyc

echo ""
echo "REMOVING CACHE FILES"
find application -name "__pycache__" -type d -exec rm -r "{}" \;
find application -name "*.pyc" -type f -exec rm "{}" \;
echo "Done!"
echo "---------------------------"

# Sync files to the ESP32-S3

echo "SYNCING FILES"
echo ""
if [ $SYNC_FILES = "false" ]
    echo "Sync skipped"
then
    echo "Do you want to sync the files to the ESP32-S3? (y/n)"
    read SYNC_FILES
    if [ $SYNC_FILES = "y" ]
    then
        echo "1/6 - Actuators"
        #ampy --port $PORT put application/actuators /actuators
        #echo "2/6 - Sensors"
        #ampy --port $PORT put application/sensors /sensors
        #echo "3/6 - Brain"
        #ampy --port $PORT put application/brain /brain
        #echo "3/6 - Brain Limbic"
        #ampy --port $PORT put application/brain/limbic /brain/limbic
        echo "3/6 - Brain Neocortex"
        ampy --port $PORT put application/brain/neocortex /brain/neocortex
        #echo "3/6 - Brain Reptilian"
        ampy --port $PORT put application/brain/reptilian /brain/reptilian
        echo "3/6 - Brain Cortex"
        #ampy --port $PORT put application/brain/cortex.py /brain/cortex.py
        #echo "4/6 - Common"
        #ampy --port $PORT put application/common /common
        echo "5/6 - Communication"
        ampy --port $PORT put application/communication /communication
        #echo "6/6 - Main"
        #ampy --port $PORT put application/main.py /main.py
    else
        echo "Sync skipped"
    fi
fi
echo "Done!"
echo "---------------------------"


if [ -z "$2" ]
then
    RUN_APP="false"
else
    RUN_APP="true"
fi

# Run the main script
echo ""
echo "RUNNING MAIN SCRIPT"
if [ $RUN_APP = "false" ]
then
    echo "Do you want to run the main script? (y/n)"
    read RUN_APP
    if [ $RUN_APP = "y" ]
    then
        ampy --port $PORT run application/main.py
    else
        echo "Main script skipped"
    fi
else
    ampy --port $PORT run application/main.py
fi