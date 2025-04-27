import {
  Platform,
  StyleSheet,
  View,
  Text,
  Button,
  TouchableOpacity,
  Dimensions,
} from "react-native";
import React, { useEffect, useState } from "react";
import { AppContainer } from "@/components/AppContainer";
import { RobotStatusBar } from "@/components/ui/RobotStatusBar";
import { RobotAlert } from "@/components/ui/RobotAlert";
import { ReactNativeJoystick } from "@korsolutions/react-native-joystick";
import { CameraView, CameraType, useCameraPermissions } from "expo-camera";
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
import { TabView, SceneMap, TabBar } from "react-native-tab-view";
import { useSelector, useDispatch } from "react-redux";
import { usePathname } from "expo-router";
import { ScrollView } from "react-native-gesture-handler";
import { UseAccessAPI } from "@/helpers/accessApi";
import { updateJoystickData } from "@/reducers/JoystickReducer";
import { decrement, increment } from "@/reducers/counterReducer";
import { JsonEditor, monoLightTheme } from "json-edit-react";
import { IRootState } from "@/reduxStore";
function SettingsTabRoute() {
  // const { data, error, isLoading } = useGetStateByNameQuery("sensors", {
  //   pollingInterval: 10000,
  // });

  const apiResult = useSelector((state: IRootState) => state.robotAPI.value);

  return (
    <View>
      {apiResult &&
        (Platform.OS == "web" ? (
          <>
            <Text>API Response</Text>
            <JsonEditor
              theme={monoLightTheme}
              restrictEdit={true}
              restrictDelete={true}
              restrictAdd={true}
              enableClipboard={false}
              data={apiResult}
            />
          </>
        ) : (
          <>
            <Text>API Response</Text>
            <Text>{JSON.stringify(apiResult)}</Text>
          </>
        ))}
    </View>
  );
}

function StatusTabRoute() {
  const [index, setIndex] = useState(0);
  const pathname = usePathname();
  const joystickData = useSelector((state: IRootState) => state.joystick.value);
  const count = useSelector((state: IRootState) => state.counter.value);
  return (
    <ScrollView>
      <View
        style={{
          justifyContent: "center",
          alignItems: "stretch",
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
        <View style={{}}>
          <Text
            style={{
              fontSize: 20,
              color: Colors.light.text,
              fontFamily: "SFCompactRounded",
            }}
          >
            Current route: {pathname}
          </Text>
        </View>
        <View style={{}}>
          <Text
            style={{
              fontSize: 20,
              color: Colors.light.text,
              fontFamily: "SFCompactRounded",
            }}
          >
            Joystick data: <Text>{JSON.stringify(joystickData)}</Text>
          </Text>
        </View>

        <View style={{}}>
          <Text
            style={{
              fontSize: 20,
              color: Colors.light.text,
              fontFamily: "SFCompactRounded",
            }}
          >
            Current count {count}
          </Text>
        </View>
        <View style={{}}>
          <Text
            style={{
              fontSize: 20,
              color: Colors.light.text,
              fontFamily: "SFCompactRounded",
            }}
          >
            Platform {Platform.OS}
          </Text>
        </View>
      </View>
    </ScrollView>
  );
}

function CameraRoute() {
  const [facing, setFacing] = useState<CameraType>("back");
  const [permission, requestPermission] = useCameraPermissions();
  useEffect(() => {
    console.log("permission", permission);
  }, [permission]);

  if (!permission) {
    // Camera permissions are still loading.
    return (
      <View>
        <Text style={styles.message}>Loading camera...</Text>
      </View>
    );
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet.
    return (
      <View style={styles.container}>
        <Text style={styles.message}>
          We need your permission to show the camera
        </Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  function toggleCameraFacing() {
    setFacing((current) => (current === "back" ? "front" : "back"));
  }

  return (
    <View style={styles.container}>
      <CameraView style={styles.camera} facing={facing}>
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.button} onPress={toggleCameraFacing}>
            <Text style={styles.text}>Flip Camera</Text>
          </TouchableOpacity>
        </View>
      </CameraView>
    </View>
  );
}

function LoggerTabRoute() {
  const count = useSelector((state: IRootState) => state.counter.value);

  const dispatch = useDispatch();

  return (
    <View>
      <Text>Count: {count}</Text>
      <Button title="Increment" onPress={() => dispatch(increment())} />
      <Button title="Decrement" onPress={() => dispatch(decrement())} />
    </View>
  );
}
export default function RobotAI() {
  const dispatch = useDispatch();
  // store the last logged data
  const routes = [
    { key: "first", title: "Camera", icon: "map" },
    { key: "second", title: "Logger", icon: "map" },
    { key: "third", title: "Settings", icon: "map" },
    { key: "fourth", title: "Status", icon: "map" },
  ];
  const [index, setIndex] = useState(3);
  const renderScene = SceneMap({
    first: () => <CameraRoute />,
    second: () => <LoggerTabRoute />,
    third: () => <SettingsTabRoute />,
    fourth: () => <StatusTabRoute />,
  });

  const renderTabBar = (props: any) => (
    <TabBar
      {...props}
      indicatorStyle={{ backgroundColor: "white" }}
      style={{ backgroundColor: Colors.light.blueDark }}
      // renderLabel={({ route, color }) => (
      //   <Text
      //     style={{
      //       color: color,
      //       fontSize: getFontSize(14),
      //       fontFamily: "SFCompactRounded",
      //     }}
      //   >
      //     {route.title}
      //   </Text>
      // )}
    />
  );
  const [isLandscape, setIsLandscape] = useState(false);

  const [isWeb] = useState(Platform.OS === "web");

  Dimensions.addEventListener("change", () => {
    const { width, height } = Dimensions.get("window");
    setIsLandscape(width > height);
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
            flexDirection: isWeb
              ? "row"
              : isLandscape
              ? "row"
              : "column-reverse",
            justifyContent: "center",
            alignItems: "stretch",
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
                dispatch(updateJoystickData(data));
              }}
              onStop={(data) => {
                //console.log("onStop", data);
                dispatch(updateJoystickData(data));
              }}
              onMove={(data) => {
                //console.log("onMove", data);
                //dispatch(updateJoystickData(data));
              }}
            />
          </View>
          <View
            style={{
              flex: 1,
              backgroundColor: "blue",
            }}
          >
            <TabView
              lazy
              navigationState={{ index, routes }}
              renderScene={renderScene}
              onIndexChange={setIndex}
              initialLayout={{}}
              renderTabBar={renderTabBar}
              style={{
                backgroundColor: Colors.light.background,
                flex: 1,
              }}
            />
          </View>
        </View>
      </View>

      <View style={styles.alertBar}>
        <RobotAlert />
        <UseAccessAPI />
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
    height: getIconSize(20),
  },
  alertBar: {
    height: getIconSize(20),
  },
  message: {
    textAlign: "center",
    paddingBottom: 10,
  },
  camera: {
    flex: 1,
    minHeight: 200,
    minWidth: 200,
    backgroundColor: Colors.light.background,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: "row",
    backgroundColor: "transparent",
    margin: 64,
  },
  button: {
    flex: 1,
    alignSelf: "flex-end",
    alignItems: "center",
  },
  text: {
    fontSize: 24,
    fontWeight: "bold",
    color: "white",
  },
});
