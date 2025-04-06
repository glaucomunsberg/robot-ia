import { Dimensions, PixelRatio } from "react-native";
const { width: SCREEN_WIDTH, height: SCREEN_HEIGHT } = Dimensions.get("window");
const SCALE = SCREEN_WIDTH > SCREEN_HEIGHT ? SCREEN_HEIGHT : SCREEN_WIDTH;
const BASE_WIDTH = 375; //375;
const fontConfig = {
  phone: {
    small: { min: 0.8, max: 1 },
    medium: { min: 0.9, max: 1 },
    large: { min: 1, max: 1.2 },
  },
  tablet: {
    small: { min: 1.2, max: 1.3 },
    medium: { min: 1.3, max: 1.4 },
    large: { min: 1.4, max: 1.5 },
  },
  desktop: {
    small: { min: 0.8, max: 1 },
    medium: { min: 0.9, max: 1 },
    large: { min: 1, max: 1.2 },
  },
};
const iconsConfig = {
  phone: {
    small: { min: 0.8, max: 1 },
    medium: { min: 0.9, max: 1 },
    large: { min: 0.8, max: 1.2 },
  },
  tablet: {
    small: { min: 1.2, max: 1.3 },
    medium: { min: 1.3, max: 1.4 },
    large: { min: 1.4, max: 1.5 },
  },
  desktop: {
    small: { min: 1.5, max: 1.6 },
    medium: { min: 1.6, max: 1.7 },
    large: { min: 1.7, max: 2 },
  },
};
export const getScreenWidth = (): number => {
  const pixelDensity = PixelRatio.get();
  const adjustedWidth = SCREEN_WIDTH * pixelDensity;
  return adjustedWidth;
};
export const getScreenHeight = (): number => {
  const pixelDensity = PixelRatio.get();
  const adjustedHeight = SCREEN_HEIGHT * pixelDensity;
  return adjustedHeight;
};

export const getDeviceType = (): "phone" | "tablet" | "desktop" => {
  const pixelDensity = PixelRatio.get();
  const adjustedWidth = SCREEN_WIDTH * pixelDensity;
  const adjustedHeight = SCREEN_HEIGHT * pixelDensity;
  if (pixelDensity < 2 && adjustedWidth >= 1400 && adjustedHeight >= 566) {
    return "desktop";
  } else if (
    pixelDensity <= 2 &&
    adjustedWidth >= 1024 &&
    adjustedHeight >= 1024
  ) {
    return "tablet";
  } else if (
    pixelDensity > 2 &&
    (adjustedWidth >= 830 || adjustedHeight >= 1800)
  ) {
    return "phone";
  } else {
    return "phone";
  }
};
const getScreenSizeCategory = (): "small" | "medium" | "large" => {
  if (SCALE < 350) return "small";
  if (SCALE > 500) return "large";
  return "medium";
};

export const getFontSize = (size: number): number => {
  const deviceType = getDeviceType();
  const screenCategory = getScreenSizeCategory();
  const config = fontConfig[deviceType][screenCategory];

  const scaleFactor = SCALE / BASE_WIDTH;
  const clampedScaleFactor = Math.min(
    Math.max(scaleFactor, config.min),
    config.max
  );
  let newSize = size * clampedScaleFactor;
  if (deviceType === "tablet") {
    newSize *= 1; // Increase tablet font sizes by an additional 10%
  } else if (deviceType === "phone") {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  } else {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  }
  return (
    Math.round(PixelRatio.roundToNearestPixel(newSize)) /
    PixelRatio.getFontScale()
  );
};

export const getFontInfoFromSize = (size: number): String => {
  const deviceType = getDeviceType();
  const screenCategory = getScreenSizeCategory();
  const config = fontConfig[deviceType][screenCategory];

  const scaleFactor = SCALE / BASE_WIDTH;
  const clampedScaleFactor = Math.min(
    Math.max(scaleFactor, config.min),
    config.max
  );
  let newSize = size * clampedScaleFactor;
  if (deviceType === "tablet") {
    newSize *= 1; // Increase tablet font sizes by an additional 10%
  } else if (deviceType === "phone") {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  } else {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  }
  return `Device Type: ${deviceType}, Screen Category: ${screenCategory}, Scale Factor: ${scaleFactor}, Clamped Scale Factor: ${clampedScaleFactor}, New Size: ${newSize}, Pixel Ratio: ${PixelRatio.get()}, Font Scale: ${PixelRatio.getFontScale()}, Value Size: ${
    Math.round(PixelRatio.roundToNearestPixel(newSize)) /
    PixelRatio.getFontScale()
  }`;
};

export const getIconInfoFromSize = (size: number): String => {
  const deviceType = getDeviceType();
  const screenCategory = getScreenSizeCategory();
  const config = iconsConfig[deviceType][screenCategory];

  const scaleFactor = SCALE / BASE_WIDTH;
  const clampedScaleFactor = Math.min(
    Math.max(scaleFactor, config.min),
    config.max
  );
  let newSize = size * clampedScaleFactor;
  if (deviceType === "tablet") {
    newSize *= 1; // Increase tablet font sizes by an additional 10%
  } else if (deviceType === "phone") {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  } else {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  }
  return `Device Type: ${deviceType}, Screen Category: ${screenCategory}, Scale Factor: ${scaleFactor}, Clamped Scale Factor: ${clampedScaleFactor}, New Size: ${newSize}, Pixel Ratio: ${PixelRatio.get()}, Font Scale: ${PixelRatio.getFontScale()}, Value Size: ${
    Math.round(PixelRatio.roundToNearestPixel(newSize)) /
    PixelRatio.getFontScale()
  }`;
};

export const getIconSize = (size: number): number => {
  const deviceType = getDeviceType();
  const screenCategory = getScreenSizeCategory();
  const config = iconsConfig[deviceType][screenCategory];

  const scaleFactor = SCALE / BASE_WIDTH;
  const clampedScaleFactor = Math.min(
    Math.max(scaleFactor, config.min),
    config.max
  );
  let newSize = size * clampedScaleFactor;
  if (deviceType === "tablet") {
    newSize *= 1.1; // Increase tablet font sizes by an additional 10%
  } else if (deviceType === "phone") {
    newSize *= 1; // Decrease phone font sizes by an additional 10%
  } else {
    newSize *= 1.2; // Decrease phone font sizes by an additional 10%
  }
  return (
    Math.round(PixelRatio.roundToNearestPixel(newSize)) /
    PixelRatio.getFontScale()
  );
};

export function isLandscape(): boolean {
  return SCREEN_WIDTH > SCREEN_HEIGHT;
}
export function isPortrait(): boolean {
  return SCREEN_HEIGHT > SCREEN_WIDTH;
}
