import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./reducers/counterReducer";
import joystickReducer from "./reducers/JoystickReducer";
import robotAPIReducer, { robotApi } from "./reducers/robotAPIReducer";
export default configureStore({
  reducer: {
    counter: counterReducer,
    joystick: joystickReducer,
    robotAPI: robotAPIReducer,
    [robotApi.reducerPath]: robotApi.reducer,
  },
  // Adding the api middleware enables caching, invalidation, polling, and other features of `createApi`
  // When creating an api slice, `createApi` automatically adds `api.middleware` to the store's middleware array
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(robotApi.middleware),
});
const store = configureStore({
  reducer: {
    counter: counterReducer,
    joystick: joystickReducer,
    robotAPI: robotAPIReducer,
    [robotApi.reducerPath]: robotApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(robotApi.middleware),
});

export type IRootState = ReturnType<typeof store.getState>;
export { store };
