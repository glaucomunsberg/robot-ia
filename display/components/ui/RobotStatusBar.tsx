import { AppContainer } from "@/components/AppContainer";
import { useState, useEffect } from "react";
import { PropsWithChildren } from "react";
import { StyleSheet, View, TouchableHighlight } from "react-native";
import IconWheelBold from "@/assets/icons/solar_wheel-angle-bold.svg";
import IconMicLine from "@/assets/icons/mingcute_mic-line.svg";
import IconDetectorOutline from "@/assets/icons/material-symbols_detector-outline.svg";
import IconTemperaturCelsius from "@/assets/icons/carbon_temperature-celsius.svg";
import IconCameraLine from "@/assets/icons/mingcute_computer-camera-line.svg";
import IconBatteryFull from "@/assets/icons/material-symbols_battery-full.svg";
import IconServer15Regular from "@/assets/icons/fluent_server-16-regular.svg";
import { Colors } from "@/constants/Colors";
import { getIconSize } from "@/helpers/responsive";

import { useColorScheme } from "@/hooks/useColorScheme";
import { Text } from "react-native";
import { Dimensions } from "react-native";

export function RobotStatusBar() {
  const theme = useColorScheme() ?? "light";
  //padding lef 0 when landscape and 20 when portrait
  const [paddingLeft, setPaddingLeft] = useState(0);
  const setCurrentPadding = (width: number, height: number) => {
    if (width > height) {
      setPaddingLeft(20);
    } else {
      setPaddingLeft(0);
    }
  };
  const listIcons = [
    IconWheelBold,
    IconMicLine,
    IconDetectorOutline,
    IconTemperaturCelsius,
    IconCameraLine,
    IconBatteryFull,
    IconServer15Regular,
  ];

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

  return (
    <AppContainer
      flexDirection="row"
      customStyle={{ paddingLeft, ...styles.container }}
    >
      {listIcons.map((Icon, index) => (
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

      <View>
        <Text>{getIconSize(18)}</Text>
      </View>
    </AppContainer>
  );
}
