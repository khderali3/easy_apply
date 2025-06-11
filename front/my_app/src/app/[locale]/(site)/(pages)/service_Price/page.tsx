

 
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

        <h1 className="page-title mb-4">Service Name</h1>
        <p className="lead text-light">Service Prices</p>
      </div>

      {/* Form Card */}
      <div className="row justify-content-center">
        <div className="col-12  ">
          <div className="custom_form_style p-4 p-md-5">
 






          <div className="prices mb-5">
            {/* Wi-Fi Outdoor Packages */}
            <div className="mb-5">
              <h3 className="text-info mb-4 text-center">Wi-Fi Outdoor Packages</h3>
              <div className="table-responsive">
                <table className="table table-borderless align-middle">
                  <thead className="border-bottom border-info">
                    <tr>
                      <th className="text-start ps-3 text-light">Speed</th>
                      <th className="text-center text-light">Data Limit</th>
                      <th className="text-end pe-3 text-light">Monthly Price</th>
                    </tr>
                  </thead>
                  <tbody>
                    {[
                      { speed: '2 Mbps', data: '50 GB', price: '$10' },
                      { speed: '5 Mbps', data: '100 GB', price: '$20' },
                      { speed: '10 Mbps', data: '200 GB', price: '$35' },
                      { speed: '20 Mbps', data: 'Unlimited', price: '$50' },
                      { speed: '50 Mbps', data: 'Unlimited', price: '$80' }
                    ].map((pkg, index) => (
                      <tr key={`wifi-${index}`} className="border-bottom border-secondary text-light">
                        <td className="text-start ps-3">{pkg.speed}</td>
                        <td className="text-center">{pkg.data}</td>
                        <td className="text-end pe-3 fw-bold  text-info">{pkg.price}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Traffic Packages */}
            <div className="row g-4">
              <div className="col-md-6">
                <div className="border rounded p-3" style={{ backgroundColor: 'rgba(0, 51, 102, 0.5)' }}>
                  <h4 className="text-center text-light mb-3 border-bottom border-info pb-2">Standard Traffic</h4>
                  <table className="table table-borderless mb-0">
                    <thead className="border-bottom border-info">
                      <tr className=" text-light">
                        <th className="text-start ps-2  ">Data Package</th>
                        <th className="text-end pe-2 ">Price</th>
                      </tr>
                    </thead>
                    <tbody>
                      {[
                        { data: '5 GB', price: '$3' },
                        { data: '10 GB', price: '$5' },
                        { data: '20 GB', price: '$8' },
                        { data: '50 GB', price: '$15' },
                        { data: '100 GB', price: '$25' }
                      ].map((pkg, index) => (
                        <tr key={`standard-${index}`} className="border-bottom border-secondary  text-light">
                          <td className="text-start ps-2">{pkg.data}</td>
                          <td className="text-end pe-2 fw-bold text-info">{pkg.price}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              <div className="col-md-6">
                <div className="border rounded p-3" style={{ backgroundColor: 'rgba(0, 51, 102, 0.5)' }}>
                  <h4 className="text-center text-light mb-3 border-bottom border-info pb-2">Unlimited Speed</h4>
                  <table className="table table-borderless mb-0">
                    <thead className="border-bottom border-info">
                      <tr>
                        <th className="text-start ps-2 text-light">Data Package</th>
                        <th className="text-end pe-2 text-light">Price</th>
                      </tr>
                    </thead>
                    <tbody>
                      {[
                        { data: '5 GB', price: '$4' },
                        { data: '10 GB', price: '$7' },
                        { data: '20 GB', price: '$12' },
                        { data: '50 GB', price: '$20' },
                        { data: '100 GB', price: '$30' }
                      ].map((pkg, index) => (
                        <tr key={`unlimited-${index}`} className="border-bottom border-secondary  text-light">
                          <td className="text-start ps-2">{pkg.data}</td>
                          <td className="text-end pe-2 fw-bold text-info">{pkg.price}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>










 



              {/* Add this right after your submit button div */}
              <div className="col-12 text-center    ">
              <Link href="/" className="back-to-home-link">
                  <i className="bi bi-arrow-left me-2"></i>
                  Back to Home Page
              </Link>
              </div>


          </div>
        </div>
      </div>
    </div>
  </div>
</div>     
    )
}


export default Page

