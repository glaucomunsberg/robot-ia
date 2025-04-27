import { StyleSheet, View } from "react-native";

import { useRouter } from "expo-router";

import { AppContainer } from "@/components/AppContainer";
import { Colors } from "@/constants/Colors";
import RobotEyeRest from "@/assets/icons/robot/eyes_resting.svg";
import RobotZzz from "@/assets/icons/robot/zzz.svg";
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withRepeat,
  Easing,
  withSequence,
} from "react-native-reanimated";

import { useEffect } from "react";
export default function HomeScreen() {
  const rotationAnimation = useSharedValue(0);
  const router = useRouter();
  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ rotate: `${rotationAnimation.value}deg` }],
  }));
  useEffect(() => {
    rotationAnimation.value = withRepeat(
      withSequence(
        withTiming(25, { duration: 150 }),
        withTiming(0, { duration: 150 })
      ),
      4 // Run the animation 4 times
    );
  }, []);

  const onPressGoToHome = () => {
    router.navigate("/");
  };

  const duration = 2000;
  const easing = Easing.bezier(0.25, -0.5, 0.25, 1);
  const sv = useSharedValue(0);
  const defaultAnim = useSharedValue<number>(10);

  const animatedDefault = useAnimatedStyle(() => ({
    transform: [{ translateY: defaultAnim.value }],
  }));
  useEffect(() => {
    defaultAnim.value = withRepeat(
      withTiming(-defaultAnim.value, {
        duration,
      }),
      -1,
      true
    );
  }, []);

  useEffect(() => {
    defaultAnim.value = withRepeat(
      withTiming(-defaultAnim.value, {
        duration,
      }),
      -1,
      true
    );
  }, []);

  useEffect(() => {
    sv.value = withRepeat(withTiming(1, { duration, easing }), -1);
  }, []);

  //Interpolation
  const progress = useSharedValue(0);

  useEffect(() => {
    progress.value = withTiming(1, { duration: 50 });
  }, []);

  // const REST_PATH = parse("M10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80");
  // const WAKEUP_PATH = parse("M10 80 C 40 150, 65 150, 95 80 S 150 10, 180 80");

  // const eyes_bored = parse(
  //   "M0 7C0 3.13401 2.98652 0 6.67059 0H74.3294C78.0135 0 81 3.13401 81 7C81 10.866 78.0135 14 74.3294 14H6.67059C2.98652 14 0 10.866 0 7Z"
  // );
  // const eyes_resting = parse(
  //   "M0 7C0 3.13401 2.98652 0 6.67059 0L41 8.5L74.3294 0C78.0135 0 81 3.13401 81 7C81 10.866 78.0135 14 74.3294 14L41 23.5L6.67059 14C2.98652 14 0 10.866 0 7Z"
  // );
  // const eyes_resting_refined = parse(
  //   "M0 7C0 3.13401 2.98652 0 6.67059 0C6.67059 0 27.189 8.59651 41 8.5C54.4322 8.40614 74.3294 0 74.3294 0C78.0135 0 81 3.13401 81 7C81 10.866 77.1588 12.5 74.3294 14C71.5 15.5 54.534 23.3958 41 23.5C27.0901 23.607 6.67059 14 6.67059 14C6.67059 14 0 10.866 0 7Z"
  // );

  // const eyes_open = parse(
  //   "M0 21.5C0 9.62588 2.98652 0 6.67059 0H74.3294C78.0135 0 81 9.62588 81 21.5C81 33.3741 78.0135 43 74.3294 43H6.67059C2.98652 43 0 33.3741 0 21.5Z"
  // );

  // const animatedProps = useAnimatedProps(() => {
  //   const d = interpolatePath(progress.value, [0, 1], [eyes_bored, eyes_open]);
  //   return { d };
  // });

  //const AnimatedPath = Animated.createAnimatedComponent(Path);

  const { navigate } = useRouter();

  const onTochOrPointerEnter = () => {
    setTimeout(() => {
      navigate("/");
    }, 1000);
    console.log("point enter");
  };
  return (
    <AppContainer
      pointerOrTouchedEnter={onTochOrPointerEnter}
      flexDirection="column"
      customStyle={styles.container}
    >
      <View style={styles.containerLeft}></View>
      <View>
        <AppContainer flexDirection="row" customStyle={styles.container}>
          <View style={styles.containerLeft}></View>
          <View style={styles.containerEyes}>
            <RobotEyeRest
              style={styles.robotZzz}
              onPress={() => {
                onPressGoToHome();
              }}
            />
          </View>
          <View style={styles.containerZzz}>
            <Animated.View style={animatedDefault}>
              <RobotZzz
                onPress={() => {
                  onPressGoToHome();
                }}
              />
            </Animated.View>
          </View>
        </AppContainer>
      </View>
      <View style={styles.containerLeft}>
        {/* <Svg width={200} height={200} viewBox="0 0 200 200">
          <AnimatedPath
            animatedProps={animatedProps}
            fill="white"
            stroke="white"
            strokeWidth={1}
          />
        </Svg> */}
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
    gap: 12,
    backgroundColor: Colors.light.back,
  },
  containerLeft: {
    flex: 1,
  },
  containerEyes: {
    alignItems: "center",
    justifyContent: "center",
  },
  containerZzz: {
    flex: 1,
    alignItems: "flex-start",
    justifyContent: "center",
    marginBottom: 200,
  },
  robotZzz: {},
});
