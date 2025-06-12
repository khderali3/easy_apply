"use client"

import { useState } from "react";
 
import { toast } from "react-toastify";
import { useCustomFetchMutation } from "@/app/[locale]/(site)/_components/redux/features/siteApiSlice";
import { getErrorMessage } from "../utils";



export function usePageDataFetcher() {
 
  const [customFetch] = useCustomFetchMutation();
  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState(null);


  const fetchData: any =  async (pageUrl: string) => {
    setIsLoading(true);
    try {
      const response = await customFetch({
        url: pageUrl,
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })

      if (response?.data) {
        setData(response.data);
      } else {
        toast.error(getErrorMessage(response.error.data));
      } 

    } catch (error) {
      const message = getErrorMessage(error);
      toast.error(message);
      console.error("Error fetching data:", error);
    } finally {
      setIsLoading(false);
    }
  } 

  return {
    fetchData,
    isLoading,
    data,
  };
}
