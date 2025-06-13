"use client"

import { useState } from "react";
 
import { toast } from "react-toastify";
import { useCustomFetchMutation } from "@/app/[locale]/(site)/_components/redux/features/siteApiSlice";
import { getErrorMessage } from "../utils";
import { useLocale } from "next-intl";


export function usePageDataFetcher() {
 
  const [customFetch] = useCustomFetchMutation();
  const [isLoading, setIsLoading] = useState<boolean>(false);
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






  const fetchData: any =  async (
    pageUrl: string,
    method_type: MethodType,
    body : any = null,
    onSuccessMessage:string|null = null ,
    onErrorMessage:string|null = null, 
    handleFunctionAfterSuccess : any = null 
       
  ) => {
    setIsLoading(true);
    try {
      const response = await customFetch({
        url: pageUrl,
        method: method_type,
        body: body,
        headers: {
          "Content-Type": "application/json",
        },
      })

      if (response?.data) {
        setData(response.data);


        if (!onSuccessMessage) {
           const msg = getSuccessMessage(method_type);
          if (msg) {
            toast.error(msg);
          }

        } else {
          toast.success(onSuccessMessage);
        }

 
        if(handleFunctionAfterSuccess){handleFunctionAfterSuccess()}

       } else {


       if (!onErrorMessage) {
          const msg = getErrorMessageByMethod(method_type);
          if (msg) {
            toast.error(msg);
          }
        
      } else {
        toast.error(onErrorMessage);
      }

        toast.error(getErrorMessage(response?.error?.data));
      } 

    } catch (error) {
      const message = getErrorMessage(error);


       if (!onErrorMessage) {
          const msg = getErrorMessageByMethod(method_type);
          if (msg) {
            toast.error(msg);
          }
      } else {
        toast.error(onErrorMessage);
      }

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
