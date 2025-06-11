import { ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';


import { useLocale } from "next-intl";


const Setup = () =>{
    const locale = useLocale()

    const isRTL =  locale === 'ar' ? true : false  

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