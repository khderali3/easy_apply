

 
import Link from "next/link"
 


const Page = () =>{


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

        <h1 className="page-title mb-4">Service Request Application</h1>
        <p className="lead text-light">Join our network of partners and grow your business with us</p>
      </div>

      {/* Form Card */}
      <div className="row justify-content-center">
        <div className="col-12 col-lg-8">
          <div className="custom_form_style p-4 p-md-5">
            <form>
              <div className="row g-4">
                {/* Personal Information */}
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light" 
                      id="fullName" 
                      placeholder="Full Name"
                    />
                    <label htmlFor="fullName" className="text-light">Full Name</label>
                  </div>
                </div>
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="email" 
                      className="form-control bg-transparent text-light" 
                      id="email" 
                      placeholder="Email Address"
                    />
                    <label htmlFor="email" className="text-light">Email Address</label>
                  </div>
                </div>
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light" 
                      id="phone" 
                      placeholder="Phone Number"
                    />
                    <label htmlFor="phone" className="text-light">Phone Number</label>
                  </div>
                </div>
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">

                    {/* <select 
                      className="form-select bg-transparent text-light" 
                      id="country"
                    >
                      <option value="">Select Country</option>
                      <option value="US">United States</option>
                      <option value="UK">United Kingdom</option>
                      <option value="CA">Canada</option>
                    </select> */}


                    <select 
                    className="form-select bg-transparent text-light border-info" 
                    id="country"
                    style={{background: "transparent", color: "white"}}
                    >
                    <option value="" style={{background: "#003366"}}>Select Country</option>
                    <option value="US" style={{background: "#003366"}}>United States</option>
                    <option value="UK" style={{background: "#003366"}}>United Kingdom</option>
                    <option value="CA" style={{background: "#003366"}}>Canada</option>
                    </select>





                    <label htmlFor="country" className="text-light">Country</label>
                  </div>
                </div>
                
 

                <div className="mb-4">
                <label className="d-block text-light mb-2">Partner Type</label>
                
                <div className="d-flex flex-row gap-4"> {/* Add this flex container */}
                    <div className="form-check">
                    <input 
                        className="form-check-input border-info bg-transparent" 
                        type="radio" 
                        name="partnerType" 
                        id="agent" 
                        value="agent"
                    />
                    <label className="form-check-label text-light ms-2" htmlFor="agent">
                        Agent
                    </label>
                    </div>
                    
                    <div className="form-check">
                    <input 
                        className="form-check-input border-info bg-transparent" 
                        type="radio" 
                        name="partnerType" 
                        id="reseller" 
                        value="reseller"
                    />
                    <label className="form-check-label text-light ms-2" htmlFor="reseller">
                        Reseller
                    </label>
                    </div>
                </div>
                </div>






                {/* Business Information */}
                <div className="col-12">
                  <hr className="my-4 border-info opacity-25" />
                  <h5 className="text-info mb-4">Business Information</h5>
                </div>
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light" 
                      id="company" 
                      placeholder="Company Name"
                    />
                    <label htmlFor="company" className="text-light">Company Name (if applicable)</label>
                  </div>
                </div>
                
                <div className="col-12 col-md-6">
                  <div className="form-floating">
                    <input 
                      type="text" 
                      className="form-control bg-transparent text-light" 
                      id="website" 
                      placeholder="Website"
                    />
                    <label htmlFor="website" className="text-light">Website (if applicable)</label>
                  </div>
                </div>
                
                <div className="col-12">
                  <div className="form-floating">
                    <textarea 
                      className="form-control bg-transparent text-light" 
                      id="experience" 
                      placeholder="Your experience"
                      style={{height: "100px"}}
                    ></textarea>
                    <label htmlFor="experience" className="text-light">Relevant Experience</label>
                  </div>
                </div>
                
                <div className="col-12">
                  <div className="form-check">
                    <input 
                      className="form-check-input" 
                      type="checkbox" 
                      id="terms"
                    />
                    <label className="form-check-label text-light" htmlFor="terms">
                      I agree to the terms and conditions
                    </label>
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

