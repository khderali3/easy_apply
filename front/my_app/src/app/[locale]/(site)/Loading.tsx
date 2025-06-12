 
"use client"

import { useLocale } from "next-intl";





 
const Loading =  () => { 

 const locale = useLocale()
 

  return(
    <div
      style={{ background: "linear-gradient(135deg, #001f3f 0%, #003366 100%)" }}
      className="d-flex align-items-center justify-content-center min-vh-100"
      >
        <h1 className="text-light">{locale === "ar" ? "جاري تحميل المحتوى" : "Loading Content...."}</h1>
    </div>
  )

}
export default Loading;
 