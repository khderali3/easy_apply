"use client"

 
import Link from "next/link"
import { usePageDataFetcher } from "@/app/public_utils/hooks/custom_api_hooks"
import { useEffect, useState, useRef } from "react"
import { useRouter } from "next/navigation"

import { useLocale, useTranslations } from "next-intl"
import { toast } from "react-toastify"

import { useSelector  } from 'react-redux';
import { stringify } from "querystring"




const Page = () =>{


  const { settings } = useSelector((state: any) => state.site_settings);


    const router : any = useRouter()
    const locale : any = useLocale()
    const t : any = useTranslations('easy_apply_request_agent.agent_request')

    const { fetchData : callCaptchApi  , isLoading : isCaptchaLoading , isError:callCaptchApiIsError ,  data : captcha_result } = usePageDataFetcher()

    const { fetchData : submitDataApi  , isLoading : isLoadingSubmitDataApi ,  isError:submitDataApiIsError , data : submitDataApiData } = usePageDataFetcher()


    const { fetchData : pageInfoApi  , isLoading : pageInfoApiIsLoading ,  isError:pageInfoApiIsError , data : pageInfoApiData } = usePageDataFetcher()

 
    const handleOnSuccess : any = () => {
      router.push('/')
    }

    const [data, setData] = useState<any>({
      full_name  : "",
      phone_number : "",
      city : "",
      address: "",
      business_type : "",
      agent_type : "",
      captcha_id : "",
      captcha_input: ""
    })



    const handleSubmit : any = (e:any) =>{
      e.preventDefault()
      const excludeFields = settings?.is_captcha_enabled ? [] : ["captcha_id", "captcha_input"];

      const emptyFields = Object.entries(data)
        // .filter(([_, value]) => typeof value === "string" && value.trim() === "")


        // .map(([key]) => key.replace("_", " "))


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

        submitDataApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/request_agent/`, "POST", formData , handleOnSuccess )

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
     pageInfoApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/get_app_index/?q=card_request_agent_label`, "GET")
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
        {pageInfoApiData?.card_request_agent_label ? (
          locale === "ar" ? (
            <>
              <h1 className="page-title mb-4">
                {pageInfoApiData.card_request_agent_label.request_form_title_ar}
              </h1>
              <p className="lead text-light">
                {pageInfoApiData.card_request_agent_label.request_form_sub_title_ar}
              </p>
            </>
          ) : (
            <>
              <h1 className="page-title mb-4">
                {pageInfoApiData.card_request_agent_label.request_form_title}
              </h1>
              <p className="lead text-light">
                {pageInfoApiData.card_request_agent_label.request_form_sub_title}
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
            <form   onSubmit={handleSubmit}>
              <div className="row g-4">


                {/* Personal Information */}
                <div className="col-12 col-md-6">
                  <div className="form-floating   ">
                    <input 
                    
                      type="text" 
                      className="form-control   bg-transparent text-light    border-info" 
                      id="full_name" 
                      name="full_name"
                      value={data.full_name}
                      onChange={handleChange}
                      placeholder="Full Name"
                      spellCheck="false" 
                    />
                    <label htmlFor="full_name" className="text-light   ">{t('form.Full_Name')}</label>
                  </div>
                </div>
                
 
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light  border-info" 
                      id="phone_number" 
                      name = "phone_number"
                      onChange={handleChange}
                      value={data.phone_number}
                      placeholder="Phone Number"
                      spellCheck="false" 

                    />
                    <label htmlFor="phone_number" className="text-light">{t('form.Phone_Number')}</label>
                  </div>
                </div>

                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light  border-info" 
                      id="city" 
                      name ="city"
                      value={data.city}
                      onChange={handleChange}
                      placeholder="city"
                      spellCheck="false" 

                    />
                    <label htmlFor="city" className="text-light">{t('form.City')}</label>
                  </div>
                </div>
  

                <div className="col-12  ">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light  border-info t " 
                      id="address"
                      name = "address" 
                      onChange={handleChange}
                      value={data.address}
                      placeholder="Address"
                      spellCheck="false" 

                     />
                    <label htmlFor="address" className="text-light">{t('form.Address')}</label>
                  </div>
                </div>


  







                <div className="mb-4">
                  <label className="d-block text-light mb-2">{t('form.Agent_Type')}</label>

                  <div className="d-flex flex-row gap-4">
                    <div className={locale === "ar" ? "form-check-reverse" : "form-check"}>
                      <input
                        className="form-check-input border-info bg-transparent"
                        type="radio"
                        name="agent_type"
                        id="Sub_Provider"
                        value="sub_provider"
                        onChange={handleChange}
                        checked={data.agent_type === "sub_provider"}
                      />
                      <label className="form-check-label text-light ms-2" htmlFor="Sub_Provider">
                        {t('form.Sub_Provider')}
                      </label>
                    </div>

                    <div className={locale === "ar" ? "form-check-reverse" : "form-check"}>
                      <input
                        className="form-check-input border-info bg-transparent"
                        type="radio"
                        name="agent_type"
                        id="Distributor"
                        value="distributor"
                        onChange={handleChange}
                        checked={data.agent_type === "distributor"}
                      />
                      <label className="form-check-label text-light ms-2" htmlFor="Distributor">
                        {t('form.Distributor')}
                      </label>
                    </div>

                    <div className={locale === "ar" ? "form-check-reverse" : "form-check"}>
                      <input
                        className="form-check-input border-info bg-transparent"
                        type="radio"
                        name="agent_type"
                        id="pos"
                        value="pos"
                        onChange={handleChange}
                        checked={data.agent_type === "pos"}
                      />
                      <label className="form-check-label text-light ms-2" htmlFor="pos">
                        {t('form.POS')}
                      </label>
                    </div>
                  </div>


                  {/* Conditionally render note */}
                  {data.agent_type === "sub_provider" && (
                    <small className="text-info d-block mt-2">{t('form.notes.sub_provider')}</small>
                  )}
                  {data.agent_type === "distributor" && (
                    <small className="text-info d-block mt-2">{t('form.notes.distributor')}</small>
                  )}
                  {data.agent_type === "pos" && (
                    <small className="text-info d-block mt-2">{t('form.notes.pos')}</small>
                  )}





                </div>


                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <select 
                    className="form-select bg-transparent text-light border-info" 
                    id="business_type"
                    name="business_type"
                    onChange={handleChange}
                    value={data.business_type}
                    style={{background: "transparent", color: "white"}}
                    >
                      <option value="" disabled style={{background: "#003366"}}> {t('form.Please_Select')}</option>
                      <option value="shop" style={{background: "#003366"}}>{t('form.Shop')}</option>
                      <option value="company" style={{background: "#003366"}}>{t('form.Company')}</option>
                     </select>

                    <label htmlFor="business_type" className="text-light">{t('form.Business_Type')}</label>
                  </div>
                </div>





 
              {settings.is_captcha_enabled && 
              
                <div className="col-12 mb-4">
                  <label className="form-label text-light mb-2">{t('form.Security_Check')}</label>

                  <div className="d-flex align-items-center gap-3">
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
                      title={t('form.Refresh_CAPTCHA')}
                      disabled={isCaptchaLoading}
                    >
                      <i className="bi bi-arrow-clockwise"></i>
                    </button>
                  </div>

                  <div className="mt-3 col-md-4">
                    <input
                      type="text"
                      className="form-control bg-transparent text-light border-info"
                      id="captcha_input"
                      dir="ltr"
                      name="captcha_input"
                      onChange={handleChange}
                      value={data.captcha_input}
                      placeholder={t('form.capcha_input_ph')}
                      autoComplete="new-password"
                      spellCheck="false"
                    />
                  </div>
                </div>

 
              }




 
                
                <div className="col-12 text-center mt-5">
                  <button 
                    type="submit" 
                    className="btn btn-info btn-lg px-5 py-3 rounded-pill text-dark fw-bold"
                    disabled={isLoadingSubmitDataApi}
                  >
                    {t('form.Submit_Application')}
                  </button>
                </div>


                {/* Add this right after your submit button div */}
                <div className="col-12 text-center mt-4 mb-5">
                  <Link href="/" className="back-to-home-link">
                      <i className={`bi  ${locale === "ar" ? "bi-arrow-right ms-2" : "bi-arrow-left me-2"} ` } ></i>
                      {t('back_to_home')}
                  </Link>
                </div>




              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>     
    )
}


export default Page

