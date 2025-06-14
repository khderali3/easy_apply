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
    const t : any = useTranslations('easy_apply_request_agent.service_request')

    const { fetchData : callCaptchApi  , isLoading : isCaptchaLoading , isError:callCaptchApiIsError ,  data : captcha_result } = usePageDataFetcher()

    const { fetchData : submitDataApi  , isLoading : isLoadingSubmitDataApi ,  isError:submitDataApiIsError , data : submitDataApiData } = usePageDataFetcher()


    const { fetchData : pageInfoApi  , isLoading : pageInfoApiIsLoading ,  isError:pageInfoApiIsError , data : pageInfoApiData } = usePageDataFetcher()

 
    const { fetchData : speedPackagesApi  , isLoading : speedPackagesApiisLoading ,  isError:speedPackagesApiIsError , data : speedPackagesApiData } = usePageDataFetcher()





    const handleOnSuccess : any = () => {
      router.push('/')
    }



 


    const [data, setData] = useState<any>({
      full_name  : "",
      phone_number : "",
      city : "",
      address: "",
      speed_package : "",
      captcha_id : "",
      captcha_input: ""
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

        submitDataApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/request_service/`, "POST", formData , handleOnSuccess )

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
     pageInfoApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/get_app_index/?q=card_request_service_label`, "GET")
     speedPackagesApi(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/speed_package_list/`, "GET")
     
    isFirstRun.current = false;
  } else if (submitDataApiIsError) {
  
    if(settings?.is_captcha_enabled){  requestCaptcha();}
  }
}, [submitDataApiIsError ]);




 useEffect(() => {
  if (
    speedPackagesApiData &&
    speedPackagesApiData.length > 0 &&
    !data.speed_package
  ) {
    setData((prev:any) => ({
      ...prev,
      speed_package: speedPackagesApiData[0].id,
    }));
  }
}, [speedPackagesApiData]);




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
        {pageInfoApiData?.card_request_service_label ? (
          locale === "ar" ? (
            <>
              <h1 className="page-title mb-4">
                {pageInfoApiData.card_request_service_label.request_form_title_ar}
              </h1>
              <p className="lead text-light">
                {pageInfoApiData.card_request_service_label.request_form_sub_title_ar}
              </p>
            </>
          ) : (
            <>
              <h1 className="page-title mb-4">
                {pageInfoApiData.card_request_service_label.request_form_title}
              </h1>
              <p className="lead text-light">
                {pageInfoApiData.card_request_service_label.request_form_sub_title}
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

                  {/* Full Name */}
                  {!speedPackagesApiData || speedPackagesApiData.length === 0 ? (
                    <div className="col-12 col-md-6">
                      <div className="placeholder-glow">
                        <span
                          className="placeholder col-12"
                          style={{ height: "58px", display: "block", borderRadius: ".375rem" }}
                        ></span>
                      </div>
                    </div>
                  ) : (
                    <div className="col-12 col-md-6">
                      <div className="form-floating">
                        <input
                          type="text"
                          className="form-control bg-transparent text-light border-info"
                          id="full_name"
                          name="full_name"
                          value={data.full_name}
                          onChange={handleChange}
                          placeholder="Full Name"
                          spellCheck="false"
                        />
                        <label htmlFor="full_name" className="text-light">
                          {t('form.Full_Name')}
                        </label>
                      </div>
                    </div>
                  )}

                  {/* Phone Number */}
                  {!speedPackagesApiData || speedPackagesApiData.length === 0 ? (
                    <div className="col-12 col-md-6">
                      <div className="placeholder-glow">
                        <span
                          className="placeholder col-12"
                          style={{ height: "58px", display: "block", borderRadius: ".375rem" }}
                        ></span>
                      </div>
                    </div>
                  ) : (
                    <div className="col-12 col-md-6">
                      <div className="form-floating">
                        <input
                          type="text"
                          className="form-control bg-transparent text-light border-info"
                          id="phone_number"
                          name="phone_number"
                          value={data.phone_number}
                          onChange={handleChange}
                          placeholder="Phone Number"
                          spellCheck="false"
                        />
                        <label htmlFor="phone_number" className="text-light">
                          {t('form.Phone_Number')}
                        </label>
                      </div>
                    </div>
                  )}

                  {/* City */}
                  {!speedPackagesApiData || speedPackagesApiData.length === 0 ? (
                    <div className="col-12 col-md-6">
                      <div className="placeholder-glow">
                        <span
                          className="placeholder col-12"
                          style={{ height: "58px", display: "block", borderRadius: ".375rem" }}
                        ></span>
                      </div>
                    </div>
                  ) : (
                    <div className="col-12 col-md-6">
                      <div className="form-floating">
                        <input
                          type="text"
                          className="form-control bg-transparent text-light border-info"
                          id="city"
                          name="city"
                          value={data.city}
                          onChange={handleChange}
                          placeholder="City"
                          spellCheck="false"
                        />
                        <label htmlFor="city" className="text-light">
                          {t('form.City')}
                        </label>
                      </div>
                    </div>
                  )}


                  {/* Speed Package Select */}
                  {!speedPackagesApiData || speedPackagesApiData.length === 0 ? (
                    <div className="col-12 col-md-6">
                      <div className="placeholder-glow">
                        <span
                          className="placeholder col-12"
                          style={{ height: "58px", display: "block", borderRadius: ".375rem" }}
                        ></span>
                      </div>
                    </div>
                  ) : (
                    <div className="col-12 col-md-6">
                      <div className="form-floating">
                        <select
                          className="form-select bg-transparent text-light border-info"
                          id="speed_package"
                          name="speed_package"
                          onChange={handleChange}
                          value={data.speed_package || ""}
                          style={{ background: "transparent", color: "white" }}
                        >
                          {speedPackagesApiData.map((obj:any) => (
                            <option
                              key={obj.id}
                              value={obj.id}
                              style={{ background: "#003366" }}
                            >
                              {locale === "ar" ? obj.speed_ar : obj.speed}
                            </option>
                          ))}
                        </select>
                        <label htmlFor="speed_package" className="text-light">
                         {t('form.speed')}
                        </label>
                      </div>
                    </div>
                  )}








                  {/* Address */}
                  {!speedPackagesApiData || speedPackagesApiData.length === 0 ? (
                    <div className="col-12">
                      <div className="placeholder-glow">
                        <span
                          className="placeholder col-12"
                          style={{ height: "58px", display: "block", borderRadius: ".375rem" }}
                        ></span>
                      </div>
                    </div>
                  ) : (
                    <div className="col-12">
                      <div className="form-floating">
                        <input
                          type="text"
                          className="form-control bg-transparent text-light border-info"
                          id="address"
                          name="address"
                          value={data.address}
                          onChange={handleChange}
                          placeholder="Address"
                          spellCheck="false"
                        />
                        <label htmlFor="address" className="text-light">
                          {t('form.Address')}
                        </label>
                      </div>
                    </div>
                  )}



                  {/* CAPTCHA Section remains as-is */}

                  {settings.is_captcha_enabled && (
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
                  )}

                  {/* Submit Button */}
                  <div className="col-12 text-center mt-5">
                    <button
                      type="submit"
                      className="btn btn-info btn-lg px-5 py-3 rounded-pill text-dark fw-bold"
                      disabled={isLoadingSubmitDataApi || (!speedPackagesApiData || speedPackagesApiData.length === 0 ) }
                    >
                      {t('form.Submit_Application')}
                    </button>
                  </div>

                  {/* Back to Home Link */}
                  <div className="col-12 text-center mt-4 mb-5">
                    <Link href="/" className="back-to-home-link">
                      <i className={`bi  ${locale === "ar" ? "bi-arrow-right ms-2" : "bi-arrow-left me-2"}`}></i>
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

