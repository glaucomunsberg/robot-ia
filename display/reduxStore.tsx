import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./reducers/counterReducer";
import joystickReducer from "./reducers/JoystickReducer";
import robotAPIReducer, { robotApi } from "./reducers/robotAPI";
export default configureStore({
  reducer: {
    counter: counterReducer,
    joystick: joystickReducer,
    robotAPI: robotAPIReducer,
    [robotApi.reducerPath]: robotApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(robotApi.middleware),
});
