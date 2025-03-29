#!/bin/bash

# GET THE FIRST PARAMETER PASSED TO THE SCRIPT
# IF THE PARAMETER IS NOT EMPTY, SET TO SYNC THE FILES
SYNC_FILES="${1:-SKIP}"
RUN_APP="${2:-Y}"
COMMAND_TO_RUN="${3:-SKIP}"

# UPPER CASE THE PARAMETERS
SYNC_FILES=$(echo $SYNC_FILES | tr '[:lower:]' '[:upper:]')
RUN_APP=$(echo $RUN_APP | tr '[:lower:]' '[:upper:]')
COMMAND_TO_RUN=$(echo $COMMAND_TO_RUN | tr '[:lower:]' '[:upper:]')

BLACK="\033[1m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[1;94m"
BLUE_LIGHT="\033[1;96m"
NORMAL="\033[0;39m"

echo -e "$BLUE"
echo -e "ROBOT IA $NORMAL"
echo -e "===========================$BLUE_LIGHT"
echo -e "DEVICES $NORMAL"
DEVICES=$(mpremote connect list | grep -v "None")
echo "  Port: $DEVICES"
if [ -z "$DEVICES" ]
then
    echo -e "  No devices found $NORMAL"
else
    echo -e "  Device Info: $(mpremote exec 'import uos; print(uos.uname())')"
fi
echo -e "---------------------------$BLUE_LIGHT" 

echo -e "SET UP CLOCK $NORMAL"
mpremote rtc --set
echo "  Clock set to $(mpremote rtc)"
echo -e "---------------------------$BLUE_LIGHT"

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
    echo "  No cache files found"
fi
echo -e "---------------------------$BLUE_LIGHT"

# Sync files to the ESP32-S3
echo -e "SYNCING FILES $NORMAL"
if [ $SYNC_FILES = "SKIP" ]
then
    echo "  Skipped by parameter"
else
    
    if [ $SYNC_FILES = "ASK" ]
    then
       echo "Do you want to sync the files to the ESP32-S3? (y/n)"
       read SYNC_FILES
       SYNC_FILES=$(echo $SYNC_FILES | tr '[:lower:]' '[:upper:]')
    else
       SYNC_FILES="Y"
    fi
    
    if [ $SYNC_FILES = "Y" ] || [ $SYNC_FILES = "YES" ]
    then
        time_start=$(date +"%Y%m%d%H%M%S")
        echo "1/7 - Actuators"
        mpremote fs cp -r application/actuators :
        echo "2/7 - Sensors"
        mpremote fs cp -r application/sensors :
        echo "3/7 - Brain"
        mpremote fs cp -r application/brain :
        echo "4/7 - Common"
        mpremote fs cp -rf application/common :
        echo "5/7 - Communication"
        mpremote fs cp -r application/communication :
        echo "6/7 - Tests"
        mpremote fs cp -r application/tests :
        echo "6/7 - Main and Config"
        mpremote fs cp application/robot-ia.json :/robot-ia.json
        mpremote fs cp application/main.py :/main.py
        mpremote fs cp application/webrepl_cfg.py :/webrepl_cfg.py
        time_finish=$(date +"%Y%m%d%H%M%S")
        echo "Time elapsed: $(($time_finish-$time_start))"
    else
        echo "Sync skipped by '$SYNC_FILES'"
    fi
fi
echo -e "---------------------------$BLUE_LIGHT"

# Run the main script
echo -e "RUN ROBOT IA $NORMAL"
if [ $RUN_APP = "SKIP" ]
then
    echo "  Skipped by parameter"
else
    echo "Do you want to run the main script? (y/n)"
    if [ $RUN_APP = "ASK" ]
    then
       echo "Do you want to run the main script? (y/n)"
       read RUN_APP
       RUN_APP=$(echo $RUN_APP | tr '[:lower:]' '[:upper:]')
    else
       RUN_APP="Y"
    fi
    if [ $RUN_APP = "Y" ] || [ $RUN_APP = "YES" ]
    then
        time_start=$(date +"%Y%m%d%H%M%S")
        mpremote run application/main.py
        time_finish=$(date +"%Y%m%d%H%M%S")
        echo "Time elapsed: $(($time_finish-$time_start))"
    else
        echo "  Run skipped by '$RUN_APP'"
    fi
fi

if [ $COMMAND_TO_RUN != "SKIP" ]
then
    time_start=$(date +"%Y%m%d%H%M%S")
    echo -e "---------------------------$BLUE_LIGHT"
    echo -e "RUN COMMAND $NORMAL"
    echo "Running: mpremote run $COMMAND_TO_RUN"
    mpremote run $COMMAND_TO_RUN
    time_finish=$(date +"%Y%m%d%H%M%S")
    echo "Time elapsed: $(($time_finish-$time_start))"
fi
echo -e "---------------------------$NORMAL"