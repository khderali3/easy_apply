 
 
"use client"

 

import React  from "react";
 

import Link from "next/link";
 
 
  

const Page: React.FC =   () =>  {
 
   

return (
  <div>
    <div className="text-center mb-5">
      <img src="/company_logo.png" alt="Logo" className="logo-img" />
      {/* <h1 className="page-title">Wi-Fi Outdoor Service</h1> */}



      <h1 className="page-title"> test </h1>



    </div>

    <div className="container">
      <div className="row g-4 justify-content-center">
        {/* Card 1 */}
        <div className="col-12 col-sm-6 col-lg-3 d-flex">
          <Link href={`/agent_request`} className="service-card-link w-100">
            <div className="service-card h-100">
              <div className="card-body text-center">
                <div className="mb-2">
                  <i className="bi bi-wifi display-4 text-info"></i>
                </div>
                <h5 className="card-title">Request to be agent or redistributer</h5>
                <p className="card-text mb-3">
                  Description for ISP service card number. This card floats above
                  the animated network background.
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
                  <i className="bi bi-wifi display-4 text-info"></i>
                </div>
                <h5 className="card-title">request to subscripe wi-fi serive</h5>
                <p className="card-text mb-3 ">
                  Description for ISP service card number. This card floats above
                  the animated network background.
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
                  <i className="bi bi-wifi display-4 text-info"></i>
                </div>
                <h5 className="card-title">check your request status</h5>
                <p className="card-text mb-3">
                  Description for ISP service card number. This card floats above
                  the animated network background.
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
                  <i className="bi bi-wifi display-4 text-info"></i>
                </div>
                <h5 className="card-title">Service Prices</h5>
                <p className="card-text mb-3 ">
                  Description for ISP service card number. This card floats above
                  the animated network background.
                </p>
 
              </div>
            </div>
          </Link>
        </div>



        
      </div>
    </div>
  </div>
);

};

export default Page;
