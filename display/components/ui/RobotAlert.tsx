import React from "react";
import { StyleSheet, View, Text } from "react-native";
import { useColorScheme } from "react-native";
import { Colors } from "@/constants/Colors";
import { AppContainer } from "@/components/AppContainer";
import IconInfoTriangle from "@/assets/icons/tabler_info-triangle.svg";
import { getFontSize, getIconSize } from "@/helpers/responsive";

import { Link } from "expo-router";
const styles = StyleSheet.create({
  container: {
    flex: 1,
    gap: 3,
  },
  item: {
    width: "auto",
  },
  text: {
    fontSize: getFontSize(8),
    color: Colors.light.text,
    fontFamily: "SFCompactRounded",
    padding: 0,
    margin: 0,
  },
  itemIcon: {
    width: getIconSize(8),
    height: getIconSize(8),
  },
});

export function RobotAlert() {
  const theme = useColorScheme() ?? "light";
  const textColor = theme === "light" ? Colors.light.text : Colors.dark.text;

  return (
    <Link href="/welcome">
      <AppContainer flexDirection="row" customStyle={styles.container}>
        <View style={styles.item}>
          <IconInfoTriangle
            style={styles.itemIcon}
            fill={theme === "light" ? "#161424" : "#161424"}
          />
        </View>
        <View style={styles.item}>
          <Text style={styles.text}>Houston, we have a problem</Text>
        </View>
      </AppContainer>
    </Link>
  );
}
