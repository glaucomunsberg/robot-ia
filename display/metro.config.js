const { getDefaultConfig } = require("expo/metro-config");

// const { getDefaultConfig } = require('@expo/metro-config');

// module.exports = getDefaultConfig(__dirname);


// SECOND EXAMPLE
// const { getDefaultConfig, mergeConfig } = require("@react-native/metro-config");

// const defaultConfig = getDefaultConfig(__dirname);
// const { assetExts, sourceExts } = defaultConfig.resolver;

// /**
//  * Metro configuration
//  * https://reactnative.dev/docs/metro
//  *
//  * @type {import('metro-config').MetroConfig}
//  */
// const config = {
//   resolver: {
//     assetExts: assetExts.filter((ext) => ext !== "svg"),
//     sourceExts: [...sourceExts, "svg"]
//   }
// };

// module.exports = mergeConfig(defaultConfig, config);


// THIRD EXAMPLE
// const {getDefaultConfig, mergeConfig} = require('@react-native/metro-config');


// const config = getDefaultConfig(__dirname, {
//   isCSSEnabled: true,
// });

// config.transformer.unstable_allowRequireContext = true;


// module.exports = function (baseConfig) {
//   const defaultConfig = mergeConfig(baseConfig, getDefaultConfig(__dirname));
//   const {resolver: {assetExts, sourceExts}} = defaultConfig;

//   return mergeConfig(
//     defaultConfig,
//     {
//       resolver: {
//         assetExts: assetExts.filter(ext => ext !== 'svg'),
//         sourceExts: [...sourceExts, 'svg'],
//       },
//     },
//   );
// };

// FOURTH EXAMPLE


// //metro.config.js
// const { getDefaultConfig, mergeConfig } = require("@react-native/metro-config");

// const defaultConfig = getDefaultConfig(__dirname);
// const { assetExts, sourceExts } = defaultConfig.resolver;

// /**
//  * Metro configuration
//  * https://facebook.github.io/metro/docs/configuration
//  *
//  * @type {import('metro-config').MetroConfig}
//  */
// const config = {
//   transformer: {
//     babelTransformerPath: require.resolve("react-native-svg-transformer")
//   },
//   resolver: {
//     assetExts: assetExts.filter((ext) => ext !== "svg"),
//     sourceExts: [...sourceExts, "svg"]
//   }
// };

// module.exports = mergeConfig(defaultConfig, config);



module.exports = (() => {
  const config = getDefaultConfig(__dirname);

  const { transformer, resolver } = config;

  config.transformer = {
    ...transformer,
    babelTransformerPath: require.resolve("react-native-svg-transformer/expo"),
  };
  config.resolver = {
    ...resolver,
    assetExts: resolver.assetExts.filter((ext) => ext !== "svg"),
    sourceExts: [...resolver.sourceExts, "svg"],
  };

  return config;
})();