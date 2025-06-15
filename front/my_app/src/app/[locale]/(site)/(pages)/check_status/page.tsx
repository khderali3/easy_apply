"use client"

 
import Link from "next/link"
import { usePageDataFetcher } from "@/app/public_utils/hooks/custom_api_hooks"
import { useEffect, useState, useRef } from "react"
import { useRouter } from "next/navigation"

import { useLocale, useTranslations } from "next-intl"
import { toast } from "react-toastify"

import { useSelector  } from 'react-redux';
 
import { useFormatData, useFormatNumber } from "@/app/public_utils/hooks/extra_hooks"
 

const Page = () =>{


    const { settings } = useSelector((state: any) => state.site_settings);

    const getFormatData = useFormatData()
    const getFormatNumber = useFormatNumber()





    const router : any = useRouter()
    const locale : any = useLocale()
    const t : any = useTranslations('easy_apply_request_agent.check_status')

    const { fetchData : callCaptchApi  , isLoading : isCaptchaLoading , isError:callCaptchApiIsError ,  data : captcha_result } = usePageDataFetcher()

    const { fetchData : submitDataApi  , isLoading : SubmitDataApiIsLoading ,  isError:submitDataApiIsError , data : submitDataApiData  } = usePageDataFetcher() 


    const { fetchData : pageInfoApi  , isLoading : pageInfoApiIsLoading ,  isError:pageInfoApiIsError , data : pageInfoApiData } = usePageDataFetcher()

 
 



 
 


    const [data, setData] = useState<any>({
 
      phone_number : "",
      type_of_request: "",
      captcha_id : "",
      captcha_input: "",
    })



    const handleSubmit : any = (e:any) =>{
      e.preventDefault()
      const excludeFields = settings?.is_captcha_enabled ? [] : ["captcha_id", "captcha_input"];

      const emptyFields = Object.entries(data)

      .filter(([key, value]) => {
        // Skip excluded fields
        if (excludeFields.includes(key)) return false;
        // Check for empty strings only
        return typeof value === "string" && value.trim() === "";
      })
      .map(([key]) => key.replace("_", " "));




      const message_txt = locale === "ar" ? "يرجى ملئ الحقول التالية" : "Please fill in"
      if (emptyFields.length > 0) {
        const message = `${message_txt}: ${emptyFields.join(", ")}`;
        toast.error(message);  
        return;
      }

 

      const formData: any = new FormData()
        Object.entries(data).forEach(([key, value]) => {
            formData.append(key, value);
          });

        submitDataApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/check_request_status/`, "POST", formData, undefined,  true  )

    }




    const handleChange = (
      e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
    ) => {
      const { name, value, type } = e.target;

      const fieldValue =
        type === 'checkbox' && e.target instanceof HTMLInputElement
          ? e.target.checked
          : value;

      setData((prevData: any) => ({
        ...prevData,
        [name]: fieldValue,
      }));
    };

   

  useEffect(()=>{
 
 
      setData((prevData: any) => ({
        ...prevData,
        "captcha_id": captcha_result?.captcha_id,
      }));
 
 

  } , [captcha_result]  )


  const requestCaptcha = () => {
       callCaptchApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/captcha/generate_image_captcha/`, "GET")

  }



const isFirstRun = useRef(true);



useEffect(()=>{
  if(settings?.is_captcha_enabled){  requestCaptcha();}
}, [settings?.is_captcha_enabled])


useEffect(() => {


  if (isFirstRun.current) {
     pageInfoApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/get_app_index/?q=card_check_request_label`, "GET")
      
    isFirstRun.current = false;
  } else if (submitDataApiIsError) {
  
    if(settings?.is_captcha_enabled){  requestCaptcha();}
  }
}, [submitDataApiIsError ]);



 



    return (

<div className=" ">
   
  <div className="  py-5">
    <div className="container">
 
      <div className="text-center mb-5">
        {/* Company Logo */}
        {pageInfoApiData?.compoany_logo ? (
          <img
            src={pageInfoApiData.compoany_logo}
            alt="Company Logo"
            className="logo-img mb-2"
          />
        ) : (
            <div className="placeholder-glow mx-auto mb-2">
              <span
                className="placeholder rounded-circle"
                style={{ width: "150px", height: "150px", display: "inline-block" }}
              ></span>
            </div>
        )}

        {/* Page Title & Subtitle */}
        {pageInfoApiData?.card_check_request_label ? (
          locale === "ar" ? (
            <>
              <h1 className="page-title mb-4">
                {pageInfoApiData.card_check_request_label.request_form_title_ar}
              </h1>
              <p className="lead text-light">
                {pageInfoApiData.card_check_request_label.request_form_sub_title_ar}
              </p>
            </>
          ) : (
            <>
              <h1 className="page-title mb-4">
                {pageInfoApiData.card_check_request_label.request_form_title}
              </h1>
              <p className="lead text-light">
                {pageInfoApiData.card_check_request_label.request_form_sub_title}
              </p>
            </>
          )
        ) : (
      <div className="placeholder-glow">
        <div className="mb-3">
          <span className="placeholder col-6 d-block mx-auto" style={{ height: "2.5rem" }}></span>
        </div>
        <div>
          <span className="placeholder col-4 d-block mx-auto" style={{ height: "1.5rem" }}></span>
        </div>
      </div>
        )}
      </div>

















      {/* Form Card */}
      <div className="row justify-content-center">
        <div className="col-12 col-lg-8">
          <div className="custom_form_style p-4 p-md-5">
 


            <form onSubmit={handleSubmit}>
              <div className="row g-4">
 

 
                <div className="col-12">
                  <div className="form-floating mx-auto" style={{maxWidth: "400px"}}>
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light text-center  border-info" 
                      id="phone" 
                      name="phone_number"
                      placeholder="Phone Number"
                      autoComplete="off"  
                      value={data.phone_number}
                      onChange={handleChange}
 
                      />
                    <label htmlFor="phone" className="text-light">{t('Phone_Number')}</label>
                  </div>
                </div>

 





                <div className="mb-4 text-center">
                  <label className="d-block text-light mb-2">{t('request_type')}</label>
                  
                  <div className="d-flex flex-row gap-4 justify-content-center">
                    <div className="form-check">
                      <input 
                        className="form-check-input border-info bg-transparent" 
                        type="radio" 
                        name="type_of_request" 
                        id="agent" 
                        value="agent"
                        onChange={handleChange}
                        checked={data.type_of_request === "agent"}
 

                      />
                      <label className="form-check-label text-light ms-2" htmlFor="agent">
                        {t('Agent')}
                      </label>
                    </div>
                    
                    <div className="form-check">
                      <input 
                        className="form-check-input border-info bg-transparent" 
                        type="radio" 
                        name="type_of_request" 
                        id="client" 
                        value="client"
                        onChange={handleChange}
                        checked={data.type_of_request === "client"}

                      />
                      <label className="form-check-label text-light ms-2" htmlFor="client">
                         {t('Service')}
                      </label>
                    </div>
                  </div>
                </div>



              {settings.is_captcha_enabled && 
                  <div className="col-12 mb-4  text-center  ">
                    <label className="form-label text-light mb-2">{t('Security_Check')}</label>

                    <div className=" align-items-center   d-flex flex-row gap-4 justify-content-center">
                      {captcha_result?.captcha_image ? (
                        <img
                          src={captcha_result.captcha_image}
                          alt="Captcha"
                          style={{ height: "50px", borderRadius: "5px" }}
                        />
                      ) : (
                        <div
                          className="placeholder-glow"
                          style={{ height: "50px", width: "120px", borderRadius: "5px" }}
                        >
                          <div className="placeholder col-12 h-100 w-100 rounded"></div>
                        </div>
                      )}

                      <button
                        type="button"
                        onClick={requestCaptcha}
                        className="btn btn-outline-info btn-sm"
                        title={t('Refresh_CAPTCHA')}
                        disabled={isCaptchaLoading}
                      >
                        <i className="bi bi-arrow-clockwise"></i>
                      </button>
                    </div>

                    <div className="mt-3 col-md-4   mx-auto ">
                      <input
                        type="text"
                        className="form-control bg-transparent text-light text-center border-info"
                        id="captcha_input"
                        dir="ltr"
                        name="captcha_input"
                        onChange={handleChange}
                        value={data.captcha_input}
                        placeholder={t('capcha_input_ph')}
                        autoComplete="new-password"
                        spellCheck="false"
                      />
                    </div>
                  </div>
              }

 
                
                <div className="col-12 text-center mt-4">
                  <button 
                    type="submit" 
                    className="btn btn-info btn-lg px-5 py-3 rounded-pill text-dark fw-bold"
                  >
                     {t('check_application_status')}
                  </button>
                </div>


                {/* Add this right after your submit button div */}
                  <div className="col-12 text-center mt-4 mb-5">
                    <Link href="/" className="back-to-home-link">
                      <i className={`bi  ${locale === "ar" ? "bi-arrow-right ms-2" : "bi-arrow-left me-2"}`}></i>
                      {t('back_to_home')}
                    </Link>
                  </div>




              </div>
 



            </form>


            {/* Results Section - appears only after submission */}

              {submitDataApiData?.length > 0 && (
                <div className="row justify-content-center">
                  <div className="col-12 col-lg-8">
                    <h3 className="text-center text-info mb-4"> {t('request_status')}</h3>
                    {submitDataApiData?.map((obj: any, index: any) => (
                      <div 
                        key={obj.id}
                        className={`status-card p-4 p-md-5 mb-4 ${index !== submitDataApiData.length - 1 ? 'border-bottom border-info' : ''}`}
                      >
                        <div className="status-details">
                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">{t('request_id')} :</span>
                            <span className="fw-bold text-info">{obj?.id && getFormatNumber(obj.id)}</span>
                          </div>


                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">{t('created_data')} :</span>
                            <span className="text-light">{ obj?.created && getFormatData(obj?.created)}</span>
                          </div>




                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">{t('status')} :</span>
                            <span className={`badge bg-${obj.status === 'complated' ? 'success' : 'warning'} text-white`}>
                              {obj.status &&  t(obj?.status)}
                            
                            </span>
                          </div>

                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">{t('Full_Name')} :</span>
                            <span className="text-light">{obj.full_name}</span>
                          </div>


                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">{t('request_type')} :</span>
                            <span className="text-light"> {obj?.type && t(obj?.type) }  </span>
                          </div>

                          { obj?.type === 'service' ?

                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">{t('Speed')} :</span>
                            <span className="text-light"> { locale === "ar" ? obj?.speed_package?.speed_ar : obj?.speed_package?.speed }  </span>
                          </div>
                          :
                          <> 
                            <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                              <span className="text-light">{t('agent_type')} :</span>
                              <span className="text-light"> { obj?.agent_type && t(obj?.agent_type)   }  </span>
                            </div>

                            <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                              <span className="text-light">{t('Business_Type')} :</span>
                              <span className="text-light"> {obj?.business_type && t(obj?.business_type)}  </span>
                            </div>
                          </>
                          }


                          <div className="mt-3 p-3 rounded border border-secondary">
                            <p className="mb-1 text-light">{t('staff_note')} :</p>
                            <p dir="auto" className="text-info">{obj?.result_note ? obj?.result_note  : "-"}</p>
                          </div>
                        </div>
                      </div>
                    ) )}
                  </div>
                </div>
              )}  
             {/* Loading State */}
            {SubmitDataApiIsLoading && (
              <div className="text-center my-4">
                <div className="spinner-border text-info" role="status">
                  <span className="visually-hidden">{t('loading')} </span>
                </div>
                <p className="text-light mt-2">{t('Checking_status')}</p>
              </div>
            )}


          {/* No Results Found */}
          {!SubmitDataApiIsLoading && submitDataApiData?.length === 0 && (
            <div className="text-center my-5">
              <h5 className="text-light">{t('No_requests_found')}</h5>
              <p className="text-secondary">{t('No_requests_found_hint')}</p>
            </div>
          )}








 

            
          </div>
        </div>
      </div>
    </div>
  </div>
</div>     
    )
}


export default Page

