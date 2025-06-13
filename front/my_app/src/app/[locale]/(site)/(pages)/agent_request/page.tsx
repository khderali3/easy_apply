"use client"

 
import Link from "next/link"
import { usePageDataFetcher } from "@/app/public_utils/hooks/custom_api_hooks"
import { useEffect } from "react"



const Page = () =>{

   const { fetchData, isLoading : isCaptchaLoading , data : captcha_result } = usePageDataFetcher()





   

  useEffect(()=>{
     console.log(captcha_result)
  } , [captcha_result]  )


  const requestCaptcha = () => {
    fetchData(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/captcha/generate_image_captcha/`, "GET")

  }




  useEffect(()=>{
    requestCaptcha()
  } , []  )




    return (

<div className=" ">
  <div className=" "></div>
  
  <div className="  py-5">
    <div className="container">
      {/* Logo and Title */}
      <div className="text-center mb-5">
        <img 
            src="/company_logo.png"     
            alt="Company Logo" 
            className="logo-img mb-2"
        />

        <h1 className="page-title mb-4">Agent/Reseller Application</h1>
        <p className="lead text-light">Join our network of partners and grow your business with us</p>
      </div>

      {/* Form Card */}
      <div className="row justify-content-center">
        <div className="col-12 col-lg-8">
          <div className="custom_form_style p-4 p-md-5">
            <form   >
              <div className="row g-4">
                {/* Personal Information */}
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light" 
                      id="fullName" 
                      placeholder="Full Name"
                      autoComplete="new-password" 
                    />
                    <label htmlFor="fullName" className="text-light">Full Name</label>
                  </div>
                </div>
                
 
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light" 
                      id="phone" 
                      placeholder="Phone Number"
                      autoComplete="new-password" 

                    />
                    <label htmlFor="phone" className="text-light">Phone Number</label>
                  </div>
                </div>

                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light" 
                      id="City" 
                      placeholder="City"
                      autoComplete="new-password" 

                    />
                    <label htmlFor="City" className="text-light">City</label>
                  </div>
                </div>
  

                <div className="col-12  ">
                  <div className="form-floating">
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light" 
                      id="Address" 
                      placeholder="Address"
                      autoComplete="new-password" 
                    />
                    <label htmlFor="Address" className="text-light">Address</label>
                  </div>
                </div>

 


                <div className="mb-4">
                  <label className="d-block text-light mb-2">Agent Type</label>
                  
                  <div className="d-flex flex-row gap-4"> {/* Add this flex container */}
                      <div className="form-check">
                      <input 
                          className="form-check-input border-info bg-transparent" 
                          type="radio" 
                          name="agentType" 
                          id="Sub_Provider" 
                          value="agent"
                      />
                      <label className="form-check-label text-light ms-2" htmlFor="Sub_Provider">
                          Sub-Provider
                      </label>
                      </div>
                      
                      <div className="form-check">
                        <input 
                            className="form-check-input border-info bg-transparent" 
                            type="radio" 
                            name="agentType" 
                            id="Distributor" 
                            value="Distributor"
                        />
                        <label className="form-check-label text-light ms-2" htmlFor="Distributor">
                            Distributor
                        </label>
                      </div>

                      <div className="form-check">
                        <input 
                            className="form-check-input border-info bg-transparent" 
                            type="radio" 
                            name="agentType" 
                            id="POS" 
                            value="reseller"
                        />
                        <label className="form-check-label text-light ms-2" htmlFor="POS">
                            POS
                        </label>
                      </div>




                  </div>
                </div>




{/* CAPTCHA Field */}
<div className="col-12 mb-4">
  <label className="form-label text-light mb-2">Security Check (CAPTCHA)</label>
  <div className="d-flex align-items-center gap-3">
    {captcha_result?.captcha_image && (
      <img
        src={captcha_result?.captcha_image}
        alt="Captcha"
        style={{ height: "50px", borderRadius: "5px" }}
      />
    )}
    <button
      type="button"
      onClick={requestCaptcha}
      className="btn btn-outline-light btn-sm"
      title="Refresh CAPTCHA"
      disabled={isCaptchaLoading}
    >
      <i className="bi bi-arrow-clockwise"></i>
    </button>
  </div>

  <div className="mt-3 col-md-4">
    <input
      type="text"
      className="form-control bg-transparent text-light"
      id="captchaInput"
      placeholder="Enter the text you see above"
      autoComplete="new-password"
    />
  </div>
</div>








 
                
                <div className="col-12 text-center mt-4">
                  <button 
                    type="submit" 
                    className="btn btn-info btn-lg px-5 py-3 rounded-pill text-dark fw-bold"
                  >
                    Submit Application
                  </button>
                </div>


                {/* Add this right after your submit button div */}
                <div className="col-12 text-center mt-4 mb-5">
                <Link href="/" className="back-to-home-link">
                    <i className="bi bi-arrow-left me-2"></i>
                    Back to Home Page
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

