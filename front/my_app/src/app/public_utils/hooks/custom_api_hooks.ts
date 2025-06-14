"use client"

import { useState } from "react";
 
import { toast } from "react-toastify";
import { useCustomFetchMutation } from "@/app/[locale]/(site)/_components/redux/features/siteApiSlice";
import { getErrorMessage } from "../utils";
import { useLocale } from "next-intl";


export function usePageDataFetcher() {
 
  const [customFetch] = useCustomFetchMutation();
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isError, setIsError] = useState<boolean>(false)
  const [data, setData] = useState<any>(null);
 




  const locale = useLocale()

  const default_post_success_message = locale === "ar" ? "تم إرسال البيانات بنجاح" : "Your data has been submitted successfully";
  const default_post_error_message = locale === "ar" ? "حدث خطأ في إرسال البيانات" : "Error with submitting data";

  const default_put_success_message = locale === "ar" ? "تم تعديل البيانات بنجاح" : "Your data has been updated successfully";
  const default_put_error_message = locale === "ar" ? "حدث خطأ في تعديل البيانات" : "Error with updating data";

  const default_delete_success_message = locale === "ar" ? "تم حذف البيانات بنجاح" : "Your data has been deleted successfully";
  const default_delete_error_message = locale === "ar" ? "حدث خطأ في حذف البيانات" : "Error with deleting data";



  type MethodType = "POST" | "PUT" | "DELETE" | "GET";



  const getSuccessMessage = (method: MethodType) => {
    switch (method) {
      case "POST": return default_post_success_message;
      case "PUT": return default_put_success_message;
      case "DELETE": return default_delete_success_message;
      default: return "";
    }
  };

  const getErrorMessageByMethod = (method: MethodType) => {
    switch (method) {
      case "POST": return default_post_error_message;
      case "PUT": return default_put_error_message;
      case "DELETE": return default_delete_error_message;
      default: return "";
    }
  };





const fetchData: any = async (
  pageUrl: string,
  method_type: MethodType,
  body: any = null,
  handleFunctionAfterSuccess: any = null,
  dontSendSuccessMessage:any = false,
  onSuccessMessage: string | null = null,
  onErrorMessage: string | null = null,
) => {
  setIsLoading(true);
  setIsError(false)
  try {
    const response = await customFetch({
      url: pageUrl,
      method: method_type,
      body: body,
    }).unwrap(); // Will throw if the backend returns an error

    setData(response);
    if(!dontSendSuccessMessage){
      const msg = onSuccessMessage || getSuccessMessage(method_type);
      if (msg) toast.success(msg);
    }


    if (handleFunctionAfterSuccess) handleFunctionAfterSuccess();

  } catch (error: any) {
    setIsError(true)
    const fallbackMsg = onErrorMessage || getErrorMessageByMethod(method_type);
    if (fallbackMsg) toast.error(fallbackMsg);

    const extracted = getErrorMessage(error);
    toast.error(extracted);
    console.log("Error fetching data:", error);

  } finally {
    setIsLoading(false);
  }
};

  return {
    fetchData,
    isLoading,
    isError,
    data,
  };
}
