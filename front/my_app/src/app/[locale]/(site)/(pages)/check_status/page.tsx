"use client"

 
import Link from "next/link"
 
import { useState } from "react";

import { toast } from "react-toastify";


interface RequestStatus {

  requestId: string;
  status: 'pending' | 'approved' | 'rejected' | "Approved"; // Union type for specific values
  date: string;
  comments: string;
}


const Page = () =>{

const [statusData, setStatusData] = useState<RequestStatus[]>([]);
  const [loading, setLoading] = useState(false);


  const handleSubmit = (e:any) => {
    e.preventDefault();
    setLoading(true);
    // Simulate API call
    setTimeout(() => {
        setStatusData([
          {
            requestId: "REQ-2023-0451",
            status: "pending",  // Fixed typo here
            date: "2023-11-15",
            comments: "Your application is under review"
          },
          {
            requestId: "REQ-2023-0452",
            status: "approved",
            date: "2023-11-15",
            comments: "Your application has been approved. Welcome to our partner network!"
          }
        ]);



      setLoading(false);
    }, 1500);

    toast.success("this is test message")
    toast.info("this is test message")
    toast.warning("this is test message")
    toast.error("this is test message")
 

  };






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
            <form onSubmit={handleSubmit}>
              <div className="row g-4">
 
                <div className="col-12">
                  <div className="form-floating mx-auto" style={{maxWidth: "400px"}}>
                    <input 
                      type="tel" 
                      className="form-control bg-transparent text-light text-center" 
                      id="phone" 
                      placeholder="Phone Number"
                      autoComplete="off"                                         
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


          {/* Results Section - appears only after submission */}

              {statusData.length > 0 && (
                <div className="row justify-content-center">
                  <div className="col-12 col-lg-8">
                    <h3 className="text-center text-info mb-4">Request Status</h3>
                    
                    {statusData.map((request, index) => (
                      <div 
                        key={request.requestId}
                        className={`status-card p-4 p-md-5 mb-4 ${index !== statusData.length - 1 ? 'border-bottom border-info' : ''}`}
                      >
                        <div className="status-details">
                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">Request ID:</span>
                            <span className="fw-bold text-info">{request.requestId}</span>
                          </div>
                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">Status:</span>
                            <span className={`badge bg-${request.status === 'approved' ? 'success' : 'warning'} text-white`}>
                              {request.status.charAt(0).toUpperCase() + request.status.slice(1)}
                            </span>
                          </div>
                          <div className="d-flex justify-content-between border-bottom border-secondary py-2">
                            <span className="text-light">Submission Date:</span>
                            <span className="text-light">{request.date}</span>
                          </div>
                          <div className="mt-3 p-3 rounded border border-secondary">
                            <p className="mb-1 text-light">Staff Note:</p>
                            <p className="text-info">{request.comments}</p>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
    


            {/* Loading State */}
            {loading && (
              <div className="text-center my-4">
                <div className="spinner-border text-info" role="status">
                  <span className="visually-hidden">Loading...</span>
                </div>
                <p className="text-light mt-2">Checking status...</p>
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

