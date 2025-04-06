import { SafeAreaView, SafeAreaProvider } from "react-native-safe-area-context";
import { PropsWithChildren } from "react";
import { StyleSheet, StatusBar, View, TouchableOpacity } from "react-native";

export interface AppContainerProps {
  children: React.ReactNode;
  flexDirection: "row" | "column";
  customStyle: any | undefined;
}

export function AppContainer({
  children,
  flexDirection,
  customStyle,
}: AppContainerProps) {
  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container} edges={["top"]}>
        <View
          style={[
            styles.containerView,
            {
              // Try setting `flexDirection` to `"row"`.
              flexDirection: flexDirection,
              ...customStyle,
            },
          ]}
        >
          {children}
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: StatusBar.currentHeight || 0,
    gap: 0,
    padding: 0,
  },
  containerView: {
    flex: 1,
  },
});
