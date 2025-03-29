#!/bin/bash

# GET THE FIRST PARAMETER PASSED TO THE SCRIPT
# IF THE PARAMETER IS NOT EMPTY, SET TO SYNC THE FILES
if [ -z "$1" ]
then
    SYNC_FILES="false"
else
    SYNC_FILES="true"
fi

if [ -z "$2" ]
then
    RUN_APP="false"
else
    RUN_APP="true"
fi
BLACK="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[1;94m"
NORMAL="\033[0;39m"

echo -e "$BLUE"
echo -e "ROBOT IA $NORMAL"
echo -e "===========================$BLACK"
echo -e "CONNECTING TO DEVICE $NORMAL"
DEVICES=$(mpremote connect list | grep -v "None")
echo "Devices found:"
echo "  $DEVICES"
echo -e "---------------------------$BLACK" 

echo -e "SET UP CLOCK $NORMAL"
mpremote rtc --set
echo -e "---------------------------$BLACK"

# Delete all folders called __pycache__ and all files with extension .pyc

echo -e "REMOVING CACHE FILES $NORMAL"
# count __pycache__ folders and .pyc files
count_pycache=$(find application -name "__pycache__" -type d | wc -l)
count_pyc=$(find application -name "*.pyc" -type f | wc -l)
if [ $count_pycache -gt 0 ] || [ $count_pyc -gt 0 ]
then
    echo "Found $count_pycache __pycache__ folders and $count_pyc .pyc files"
    find application -name "__pycache__" -type d -exec rm -r "{}" \;
    find application -name "*.pyc" -type f -exec rm "{}" \;
else
    echo "No cache files found"
fi
echo -e "---------------------------$BLACK"

# Sync files to the ESP32-S3
echo -e "SYNCING FILES $NORMAL"
if [ $SYNC_FILES = "false" ]
    echo "Sync skipped by parameter"
then
    echo "Do you want to sync the files to the ESP32-S3? (y/n)"
    read SYNC_FILES
    SYNC_FILES=$(echo $SYNC_FILES | tr '[:lower:]' '[:upper:]')
    if [ $SYNC_FILES = "Y" ] || [ $SYNC_FILES = "YES" ]
    then
        time_start=$(date +"%Y%m%d%H%M%S")
        echo "1/7 - Actuators"
        mpremote fs cp -r application/actuators :/actuators
        echo "2/7 - Sensors"
        mpremote fs cp -r application/sensors :/sensors
        echo "3/7 - Brain"
        mpremote fs cp -r application/brain :/brain
        echo "4/7 - Common"
        mpremote fs cp -r application/common :/common
        echo "5/7 - Communication"
        mpremote fs cp -r application/communication :/communication
        echo "6/7 - Tests"
        mpremote fs mkdir :/tests
        mpremote fs cp -r application/tests :/tests
        echo "6/7 - Main and Config"
        mpremote fs cp application/robot-ia.json :/robot-ia.json
        mpremote fs cp application/main.py :/main.py
        time_finish=$(date +"%Y%m%d%H%M%S")
        echo "Time elapsed: $(($time_finish-$time_start))"
    else
        echo "Sync skipped by '$SYNC_FILES'"
    fi
fi
echo -e "---------------------------$BLACK"

# Run the main script
echo -e "RUN ROBOT IA $NORMAL"
if [ $RUN_APP = "false" ]
    echo "Run skipped by parameter"
then
    echo "Do you want to run the main script? (y/n)"
    read RUN_APP
    RUN_APP=$(echo $RUN_APP | tr '[:lower:]' '[:upper:]')
    if [ $RUN_APP = "Y" ] || [ $RUN_APP = "YES" ]
    then
        mpremote run application/main.py
    else
        echo "Run skipped by '$RUN_APP'"
    fi
else
    mpremote run run application/main.py
fi
echo -e "---------------------------$NORMAL"