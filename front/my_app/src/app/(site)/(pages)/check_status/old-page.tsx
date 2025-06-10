

 
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

        <h1 className="page-title mb-4">Check you request Application Status</h1>
        <p className="lead text-light">Join our network of partners and grow your business with us</p>
      </div>

      {/* Form Card */}
      <div className="row justify-content-center">
        <div className="col-12 col-lg-8">
          <div className="custom_form_style p-4 p-md-5">
            <form>
              <div className="row g-4">
 
                <div className="col-12">
                  <div className="form-floating mx-auto" style={{maxWidth: "400px"}}>
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light text-center" 
                      id="phone" 
                      placeholder="Phone Number"
                    />
                    <label htmlFor="phone" className="text-light">Phone Number</label>
                  </div>
                </div>

                <div className="mb-4 text-center">
                  <label className="d-block text-light mb-2">Request Type</label>
                  
                  <div className="d-flex flex-row gap-4 justify-content-center">
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
                        Service
                      </label>
                    </div>
                  </div>
                </div>





 
                
                <div className="col-12 text-center mt-4">
                  <button 
                    type="submit" 
                    className="btn btn-info btn-lg px-5 py-3 rounded-pill text-dark fw-bold"
                  >
                    Check Application Status
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

