"use client"
import { ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';


import { useLocale } from "next-intl";
import useGetSiteSettings from "./hooks/use_get_site_settings";

const Setup = () =>{
    const locale = useLocale()

    const isRTL =  locale === 'ar' ? true : false  

    useGetSiteSettings()

    return(
        <>
        
   
            <ToastContainer
                rtl={isRTL}
                position={isRTL ? "top-left" : "top-right"}
                style={{ zIndex: 9999, marginRight: isRTL ? 0 : "20px", marginLeft: isRTL ? "20px" : 0 }}
            />
 
          
        
        </>


    )

}
 

export default Setup