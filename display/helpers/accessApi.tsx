import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useGetStateByNameQuery } from "@/reducers/robotAPI";
import { updateRobotAPIData } from "@/reducers/robotAPI";
export function UseAccessAPI() {
  const dispatch = useDispatch();

  const { data, error, isLoading } = useGetStateByNameQuery("sensors", {
    pollingInterval: 1000,
  });
  useEffect(() => {
    console.error("Error fetching sensors data:", error);
    dispatch(
      updateRobotAPIData({
        status: "error",
      })
    );
  }, [error]);
  useEffect(() => {
    console.log("Loading sensors data...");
    dispatch(
      updateRobotAPIData({
        status: "loading",
      })
    );
  }, [isLoading]);
  useEffect(() => {
    if (!data) {
      console.log("No data fetched");
      //return;
    }
    console.log("Fetched sensors data:", data);
    const result = {
      ...data,
      status: "success",
    };
    dispatch(updateRobotAPIData(result));
  }, [data]);
  return <></>;
}
