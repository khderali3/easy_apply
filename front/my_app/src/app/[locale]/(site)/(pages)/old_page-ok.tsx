 

import React  from "react";
 

import Link from "next/link";
import { getLocale } from "next-intl/server";
import { getErrorMessage } from "@/app/public_utils/utils";
import { div } from "three/tsl";
  

const Page: React.FC = async   () =>  {


    const  locale = await getLocale()
    let data : any = {}
    let errorMessage: any;

    try {

      const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/get_app_index/`,
      { cache: 'no-store',}  // Disable caching
      );

 
      const json = await res.json();

      if (!res.ok) {
        // If backend sends a structured error, stringify the whole response
        throw new Error(typeof json === 'object' ? JSON.stringify(json) : String(json));
 
      }

      data = json;
    } catch (error: any) {
      errorMessage = getErrorMessage(error?.data || error?.message) || "Something went wrong"
 
    }


 

 
return (
 
 <div>

  {errorMessage ? (
 
 

  <div className="custom-error-box my-3 mx-auto">
    <div className="custom-error-title">{locale === "ar" ? "خطأ" : "Error"}</div>
    <div className="custom-error-message">{errorMessage}</div>
  </div>
 


  ) : (


  <div>
    <div className="text-center mb-5">

      {data?.compoany_logo ?
            <img src={data.compoany_logo} alt="Logo" className="logo-img" />
      :    <img src="/company_logo.png" alt="Logo" className="logo-img" />

      }




      <h1 className="page-title"> {locale === "ar" ?  data?.app_index_title?.title_ar :  data?.app_index_title?.title } </h1>



    </div>

    <div className="container">
      <div className="row g-4 justify-content-center">
 
        <div className="col-12 col-sm-6 col-lg-3 d-flex">
          <Link href={`/agent_request`} className="service-card-link w-100">
            <div className="service-card h-100">
              <div className="card-body text-center">
                <div className="mb-2">
                  <i className={`bi display-4 text-info ${data?.card_request_agent_label?.bootstrap_icon}`}></i>
                </div>
                <h5 className="card-title">  { locale === "ar" ? data?.card_request_agent_label?.title_ar  :  data?.card_request_agent_label?.title }</h5>
                <p className="card-text mb-3">
                  { locale === "ar" ? data?.card_request_agent_label?.details_ar :  data?.card_request_agent_label?.details}
                 </p>
              </div>
            </div>
          </Link>
        </div>

        {/* Card 2 */}
        <div className="col-12 col-sm-6 col-lg-3 d-flex">
          <Link href={`/service_request`} className="service-card-link w-100">
            <div className="service-card h-100">
              <div className="card-body text-center">
                <div className="mb-2">
                  <i className={`bi display-4 text-info ${data?.card_request_service_label?.bootstrap_icon}`}></i>
                </div>
                <h5 className="card-title">  { locale === "ar" ? data?.card_request_service_label?.title_ar  :  data?.card_request_service_label?.title }</h5>
                <p className="card-text mb-3 ">
                  { locale === "ar" ? data?.card_request_service_label?.details_ar :  data?.card_request_service_label?.details}

                </p>
              </div>
            </div>
          </Link>
        </div>

        {/* Card 3 */}
        <div className="col-12 col-sm-6 col-lg-3 d-flex">
          <Link href={`/check_status`} className="service-card-link w-100">
            <div className="service-card h-100">
              <div className="card-body text-center">
                <div className="mb-2">
                  <i className={`bi display-4 text-info ${data?.card_check_request_label?.bootstrap_icon}`}></i>
                </div>
                <h5 className="card-title">  { locale === "ar" ? data?.card_check_request_label?.title_ar  :  data?.card_check_request_label?.title }</h5>
                <p className="card-text mb-3">
                  { locale === "ar" ? data?.card_check_request_label?.details_ar :  data?.card_check_request_label?.details}
                </p>
              </div>
            </div>
          </Link>
        </div>

        {/* Card 4 */}
        <div className="col-12 col-sm-6 col-lg-3 d-flex">
          <Link href={`/service_Price`} className="service-card-link w-100">
            <div className="service-card h-100">
              <div className="card-body text-center ">
                <div className="mb-2">
                  <i className={`bi display-4 text-info ${data?.card_service_prices_label?.bootstrap_icon}`}></i>
                </div>
                <h5 className="card-title">  { locale === "ar" ? data?.card_service_prices_label?.title_ar  :  data?.card_service_prices_label?.title }</h5>
                <p className="card-text mb-3 ">
                  { locale === "ar" ? data?.card_service_prices_label?.details_ar :  data?.card_service_prices_label?.details}

                </p>
 
              </div>
            </div>
          </Link>
        </div>

 








        
      </div>
    </div>


 



  </div>



  )}





 </div>

);

};

export default Page;
