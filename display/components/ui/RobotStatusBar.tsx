import { AppContainer } from "@/components/AppContainer";
import { useState, useEffect } from "react";
import { PropsWithChildren } from "react";
import { StyleSheet, View, TouchableHighlight } from "react-native";
import { Colors } from "@/constants/Colors";
import { getIconSize } from "@/helpers/responsive";
import { useSelector } from "react-redux";

import { useColorScheme } from "@/hooks/useColorScheme";
import { Text } from "react-native";
import { Dimensions } from "react-native";

import IconWheelBold from "@/assets/icons/solar_wheel-angle-bold.svg";
import IconWheelBoldOff from "@/assets/icons/custom_wheel-angle-bold.svg";

import IconMicLine from "@/assets/icons/mingcute_mic-line.svg";
import IconMicOffLine from "@/assets/icons/mingcute_mic-off-line.svg";

import IconDetectorOutline from "@/assets/icons/material-symbols_detector-outline.svg";
import IconDetectorOfflineOutline from "@/assets/icons/material-symbols_detector-offline-outline.svg";

import IconBacklightHight from "@/assets/icons/material-symbols_backlight-high.svg";
import IconBacklightOff from "@/assets/icons/material-symbols_backlight-high-off.svg";

import IconTemperaturCelsius from "@/assets/icons/carbon_temperature-celsius.svg";
import IconTemperaturCelsiusOff from "@/assets/icons/tabler_temperature-off.svg";

import IconCameraLine from "@/assets/icons/mingcute_computer-camera-line.svg";
import IconCameraOffLine from "@/assets/icons/mingcute_computer-camera-off-line.svg";

import IconBattery5Percent from "@/assets/icons/material-symbols_battery-vert-005.svg";
import IconBattery50Percent from "@/assets/icons/material-symbols_battery-vert-050.svg";
import IconBattery75Percent from "@/assets/icons/material-symbols_battery-6-bar-sharp.svg";
import IconBatteryFull from "@/assets/icons/material-symbols_battery-full.svg";
import IconBatteryAlert from "@/assets/icons/material-symbols_battery-alert.svg";

import IconServer16Regular from "@/assets/icons/fluent_server-16-regular.svg";
import IconServerLink16Regular from "@/assets/icons/fluent_server-link-16-regular.svg";

import IconVolumeUp from "@/assets/icons/material-symbols_volume-up-off-rounded.svg";
import IconVolumeUpOff from "@/assets/icons/material-symbols_volume-up-rounded.svg";

export interface listIconsTypes {
  status: "online" | "offline";
  iconName:
    | "wheel"
    | "mic"
    | "detector"
    | "temperature"
    | "camera"
    | "battery"
    | "server"
    | "led"
    | "ultrasonic";
}

export function RobotStatusBar() {
  const theme = useColorScheme() ?? "light";
  const apiResult = useSelector((state) => state.robotAPI.value);
  //padding lef 0 when landscape and 20 when portrait
  const [paddingLeft, setPaddingLeft] = useState(0);
  const setCurrentPadding = (width: number, height: number) => {
    if (width > height) {
      setPaddingLeft(20);
    } else {
      setPaddingLeft(0);
    }
  };
  const listIcons = {
    wheel: {
      online: IconWheelBold,
      offline: IconWheelBoldOff,
    },
    mic: {
      online: IconMicLine,
      offline: IconMicOffLine,
    },
    ultrasonic: {
      online: IconDetectorOutline,
      offline: IconDetectorOfflineOutline,
    },
    temperature: {
      online: IconTemperaturCelsius,
      offline: IconTemperaturCelsiusOff,
    },
    camera: {
      online: IconCameraLine,
      offline: IconCameraOffLine,
    },
    battery: {
      online: IconBatteryFull,
      offline: IconBatteryAlert,
      fivePercent: IconBattery5Percent,
      fiftyPercent: IconBattery50Percent,
      seventyFivePercent: IconBattery75Percent,
    },
    server: {
      online: IconServer16Regular,
      offline: IconServerLink16Regular,
    },
    led: {
      online: IconBacklightHight,
      offline: IconBacklightOff,
    },
    buzzer: {
      online: IconVolumeUp,
      offline: IconVolumeUpOff,
    },
  };

  const onPressButton = () => {
    //TODO: Add action for button press
  };
  const styles = StyleSheet.create({
    container: {
      padding: 0,
      gap: 3,
      height: getIconSize(18),
      minHeight: getIconSize(18),
    },
    item: {
      width: "auto",
    },
    itemIcon: {
      width: getIconSize(20),
      height: getIconSize(20),
    },
  });

  useEffect(() => {
    const { width, height } = Dimensions.get("window");
    setCurrentPadding(width, height);
  }, []);

  Dimensions.addEventListener("change", () => {
    const { width, height } = Dimensions.get("window");
    setCurrentPadding(width, height);
  });

  const returnIconFromList = ({ status, iconName }: listIconsTypes) => {
    const icon = listIcons[iconName];
    if (icon) {
      if (status === "online") {
        return icon.online;
      } else {
        return icon.offline;
      }
    } else {
      console.warn(`Icon ${iconName} not found`);
      return null;
    }
  };

  const currentIconsToDisplay = () => {
    let listIconsToDisplay = [] as any;
    if (apiResult?.sensors) {
      for (const [key, value] of Object.entries(apiResult.sensors)) {
        const iconName = key as keyof typeof listIcons;
        const status = value.status as "online" | "offline";
        const icon = returnIconFromList({ status, iconName });
        if (icon) {
          listIconsToDisplay.push(icon);
        }
        //listIconsToDisplay.push(icon);
      }
      for (const [key, value] of Object.entries(apiResult.actuators)) {
        const iconName = key as keyof typeof listIcons;
        const status = value.status as "online" | "offline";
        const icon = returnIconFromList({ status, iconName });
        if (icon) {
          listIconsToDisplay.push(icon);
        }
        //listIconsToDisplay.push(icon);
      }
      for (const [key, value] of Object.entries(apiResult.energy)) {
        let icon = null;
        if (apiResult.energy.battery) {
          if (apiResult.energy.battery.status === "online") {
            if (apiResult.energy.battery.level > 75) {
              icon = listIcons.battery.online;
            } else if (apiResult.energy.battery.level >= 50) {
              icon = listIcons.battery.seventyFivePercent;
            } else if (apiResult.energy.battery.level >= 25) {
              icon = listIcons.battery.fiftyPercent;
            } else if (apiResult.energy.battery.level > 10) {
              icon = listIcons.battery.fivePercent;
            }
          } else {
            icon = listIcons.battery.offline;
          }
        }
        if (icon) {
          listIconsToDisplay.push(icon);
        }
        //listIconsToDisplay.push(icon);
      }
    } else {
      listIconsToDisplay = [
        listIcons.wheel.offline,
        listIcons.mic.offline,
        listIcons.ultrasonic.offline,
        listIcons.temperature.offline,
        listIcons.camera.offline,
        listIcons.battery.offline,
        listIcons.server.offline,
      ];
    }
    return listIconsToDisplay;
  };

  return (
    <AppContainer
      flexDirection="row"
      customStyle={{ paddingLeft, ...styles.container }}
    >
      {currentIconsToDisplay().map((Icon, index) => (
        <View key={index} style={styles.item}>
          <TouchableHighlight onPress={onPressButton} underlayColor="none">
            <Icon
              height={styles.itemIcon.height}
              width={styles.itemIcon.width}
              fill={
                theme === "light" ? Colors.light.grayDark : Colors.dark.grayDark
              }
            />
          </TouchableHighlight>
        </View>
      ))}
    </AppContainer>
  );
}
