import { StyleSheet, View, Text, useWindowDimensions } from "react-native";
import React, { useState } from "react";
import { AppContainer } from "@/components/AppContainer";
import { RobotStatusBar } from "@/components/ui/RobotStatusBar";
import { RobotAlert } from "@/components/ui/RobotAlert";
import { ReactNativeJoystick } from "@korsolutions/react-native-joystick";
import {
  getDeviceType,
  getFontSize,
  getIconSize,
  getScreenWidth,
  getScreenHeight,
  getFontInfoFromSize,
  getIconInfoFromSize,
} from "@/helpers/responsive";
import { Colors } from "@/constants/Colors";
import { PixelRatio } from "react-native";
import { TabView, SceneMap, Icon } from "react-native-tab-view";
interface FirstPageProps {
  logData: string[];
}

function FirstRoute(props: FirstPageProps) {
  const [index, setIndex] = useState(0);
  return (
    <View
      style={{
        justifyContent: "center",
        alignItems: "left",
        gap: 6,
      }}
    >
      <View>
        <Text
          style={{
            fontSize: 20,
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          Device type: {getDeviceType()}
        </Text>
      </View>
      <View>
        <Text
          style={{
            fontSize: 20,
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          With/Height (Radio): {getScreenWidth()}px / {getScreenHeight()}px (
          {PixelRatio.get()})
        </Text>
      </View>
      <View>
        <Text
          style={{
            fontSize: getFontSize(14),
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          FontSize 14: {getFontSize(14)} (scale {PixelRatio.getFontScale()})
        </Text>
      </View>
      <View>
        <Text
          style={{
            fontSize: getFontSize(14),
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          FontInfo: {getFontInfoFromSize(14)}
        </Text>
      </View>
      <View>
        <Text
          style={{
            fontSize: getFontSize(14),
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          IconSize 12: {getIconSize(12)}
        </Text>
      </View>
      <View>
        <Text
          style={{
            fontSize: getFontSize(14),
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          Info: {getIconInfoFromSize(14)}
        </Text>
      </View>
      <View style={{ flex: 1 }}>
        <Text
          style={{
            fontSize: 20,
            color: Colors.light.text,
            fontFamily: "SFCompactRounded",
          }}
        >
          {props.logData.map((element, index) => {
            return <Text key={index}>{element}</Text>;
          })}
        </Text>
      </View>
    </View>
  );
}
export default function RobotAI() {
  // store the last logged data
  const routes = [
    { key: "first", title: "Camera", icon: "map" },
    { key: "second", title: "Logger", icon: "map" },
    { key: "third", title: "Settings", icon: "map" },
    { key: "fourth", title: "Status", icon: "map" },
  ];
  const [index, setIndex] = useState(3);

  const [logData, setLogData] = useState([""]);
  const renderScene = SceneMap({
    first: () => <View></View>,
    second: () => <View></View>,
    third: () => <View></View>,
    fourth: () => <FirstRoute logData={logData} />,
  });

  return (
    <AppContainer flexDirection="column" customStyle={styles.container}>
      <View style={styles.statusBar}>
        <RobotStatusBar />
      </View>
      <View style={{ flex: 1 }}>
        <View
          style={{
            flex: 1,
            flexDirection: "row",
            justifyContent: "center",
            alignItems: "left",
            gap: 6,
          }}
        >
          <View
            style={{
              flex: 1,
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <ReactNativeJoystick
              color={Colors.light.blueDark}
              radius={75}
              onStart={(data) => {
                //console.log("onStart", data);
                setLogData([JSON.stringify(data)]);
              }}
              onStop={(data) => {
                //console.log("onStop", data);
                setLogData([JSON.stringify(data)]);
              }}
              onMove={(data) => {
                //console.log("onMove", data);
                setLogData([JSON.stringify(data)]);
              }}
            />
          </View>
          <View style={{ flex: 1, backgroundColor: "blue" }}>
            <TabView
              lazy
              navigationState={{ index, routes }}
              renderScene={renderScene}
              onIndexChange={setIndex}
              initialLayout={{}}
              style={{
                backgroundColor: Colors.light.background,
              }}
              renderLabel={({ route, color }) => (
                <Text style={[styles.tabLabel, { color }]}>
                  {route.title} 1
                </Text>
              )}
            />
          </View>
        </View>
      </View>

      <View style={{}}>
        <RobotAlert />
      </View>
    </AppContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingLeft: 0,
    paddingRight: 0,
    paddingTop: 5,
    paddingBottom: 0,
    gap: 6,
  },
  statusBar: {
    minHeight: getIconSize(20),
  },
});
