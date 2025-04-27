// Or from '@reduxjs/toolkit/query/react'
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { createSlice } from "@reduxjs/toolkit";

export interface RobotAPIStateType {
  status: string | null;
  sensors: {
    [key: string]: any;
  };
  actuators: {
    [key: string]: any;
  };
  energy: {
    battery: {
      status: string;
      level: number;
    };
  };
}
export const robotAPISlice = createSlice({
  name: "robotAPI",
  initialState: {
    value: {
      status: null,
      sensors: {},
      actuators: {},
      energy: {
        battery: {
          status: "",
          level: 0,
        },
      },
    },
  },
  reducers: {
    updateRobotAPIData: (state, action) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the Immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes

      // concat and update the values
      state.value = { ...state.value, ...action.payload };
    },
    reset: (state) => {
      state.value = {
        status: null,
        sensors: {},
        actuators: {},
        energy: {
          battery: {
            status: "",
            level: 0,
          },
        },
      };
    },
  },
});

// Action creators are generated for each case reducer function
export const { updateRobotAPIData, reset } = robotAPISlice.actions;

export const robotApi = createApi({
  // Set the baseUrl for every endpoint below
  reducerPath: "robotApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://192.168.18.39:8863/" }),
  tagTypes: ["robotData"],
  endpoints: (build) => ({
    getStateByName: build.query({
      query: (name: string) => `${name}`,
    }),
    createState: build.mutation({
      query: ({ name, patch }) => ({
        url: `${name}`,
        // When performing a mutation, you typically use a method of
        // PATCH/PUT/POST/DELETE for REST endpoints
        method: "PATCH",
        // fetchBaseQuery automatically adds `content-type: application/json` to
        // the Headers and calls `JSON.stringify(patch)`
        body: patch,
      }),
    }),
  }),
});

export const { useGetStateByNameQuery, reducer, middleware } = robotApi;

export default robotAPISlice.reducer;
