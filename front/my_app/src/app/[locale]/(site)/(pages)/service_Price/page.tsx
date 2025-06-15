import React from "react";
import Link from "next/link";
import { getLocale, getTranslations } from "next-intl/server";
import { getErrorMessage } from "@/app/public_utils/utils";

const Page = async () => {
  const locale = await getLocale();
  const t = await getTranslations('easy_apply_request_agent.prices_page')


  let data: any ;
  let errorMessage: any;

  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/prices/`,
      { cache: "no-store" }
    );

    const json = await res.json();

    if (!res.ok) {
      throw json;
    }
    data = json;
  } catch (error: any) {
    errorMessage = 
      getErrorMessage(error?.data || error?.message) ||
      "Something went wrong";
  }





  return (
    <div>
      <div>
        {errorMessage && (
          <div className="custom-error-box my-3 mx-auto">
            <div className="custom-error-title">
              {locale === "ar" ? "خطأ" : "Error"}
            </div>
            <div className="custom-error-message">{errorMessage}</div>
          </div>
        )}
      </div>

      <div className="py-5">
        <div className="container">
          <div className="text-center mb-5">
            {data?.compoany_logo ? (
              <img
                src={data.compoany_logo}
                alt="Logo"
                className="logo-img"
                style={{ maxWidth: "150px" }}
              />
            ) : (
              <div className="placeholder-glow mx-auto">
                <span
                  className="placeholder rounded-circle"
                  style={{
                    width: "150px",
                    height: "150px",
                    display: "inline-block",
                  }}
                ></span>
              </div>
            )}

            {data?.app_prices_title?.title || data?.app_index_title?.title_ar ? (
              <>
                <h1 className="page-title mt-3">
                  {locale === "ar"
                    ? data.app_prices_title?.title_ar
                    : data.app_prices_title?.title}
                </h1>
                <p className="lead text-light">
                  {locale === "ar"
                    ? data.app_prices_title?.title_hint_ar
                    : data.app_prices_title?.title_hint}
                </p>
              </>
            ) : (
              <h1 className="page-title mt-3 placeholder-glow">
                <span className="placeholder col-6"></span>
              </h1>
            )}
          </div>











        {/* Form Card */}

        {data ? (
          <div className="row justify-content-center">
            <div className="col-12">
              <div className="custom_form_style p-4 p-md-5">
                <div className="prices mx-auto col-md-6">
                  {/* Wi-Fi Outdoor Packages */}
                  <div className="mb-5">
                    <h3 className="text-info mb-4 text-center">
                      {/* Wi-Fi Outdoor Packages */}
                      {t('Wi_Fi_Outdoor_Packages')}

                    </h3>
                    <div className="table-responsive">
                      <table className="table table-borderless align-middle">
                        <thead className="border-bottom border-info">
                          <tr>
                            <th className="text-start ps-3 text-light">{t('Speed')}</th>
                            <th className="text-center text-light">{t('traffc_limit')}</th>
                            <th className="text-end pe-3 text-light">{t('Monthly_Price')}</th>
                          </tr>
                        </thead>
                        <tbody>
                          {data?.speed_packages?.map((obj: any) => (
                            <tr
                              key={`wifi-${obj?.id}`}
                              className="border-bottom border-secondary text-light"
                            >
                              <td className="text-start ps-3">{locale === "ar" ?  obj?.speed_ar :   obj?.speed}</td>
                              <td className="text-center">{ locale === "ar" ? obj?.traffic_limit_ar : obj?.traffic_limit }</td>
                              <td className="text-end pe-3 fw-bold text-info">
                                {Math.floor(obj?.price)} {t('SYP')}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                {/* Traffic Packages (remain side by side) */}
                <div className="row g-4">
                  <div className="col-md-6">
                    <div
                      className="border rounded p-3"
                      style={{ backgroundColor: "rgba(0, 51, 102, 0.5)" }}
                    >
                      <h4 className="text-center text-light mb-3 border-bottom border-info pb-2">
                        
                        {t('Standard_Traffic')}
                      </h4>
                      <table className="table table-borderless mb-0">
                        <thead className="border-bottom border-info">
                          <tr className="text-light">
                            <th className="text-start ps-2"> {t('traffic_package')}</th>
                            <th className="text-end pe-2">{t('price')}</th>
                          </tr>
                        </thead>
                        <tbody>
                          {data?.traffic_packages?.map((obj: any) => (
                            <tr
                              key={obj?.id}
                              className="border-bottom border-secondary text-light"
                            >
                              <td className="text-start ps-2">{ locale === "ar" ? obj?.traffic_ar :   obj?.traffic}</td>
                              <td className="text-end pe-2 fw-bold text-info">
                                {Math.floor(obj?.price)} {t('SYP')}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <div className="col-md-6">
                    <div
                      className="border rounded p-3"
                      style={{ backgroundColor: "rgba(0, 51, 102, 0.5)" }}
                    >
                      <h4 className="text-center text-light mb-3 border-bottom border-info pb-2">
                          {t('Unlimited_Speed_traffic')}
                      </h4>
                      <table className="table table-borderless mb-0">
                        <thead className="border-bottom border-info">
                          <tr>
                            <th className="text-start ps-2 text-light">
                              {t('traffic_package')}
                            </th>
                            <th className="text-end pe-2 text-light">{t('price')}</th>
                          </tr>
                        </thead>
                        <tbody>
                          {data?.unlimited_speed_packages?.map((obj: any) => (
                            <tr
                              key={obj?.id}
                              className="border-bottom border-secondary text-light"
                            >
                              <td className="text-start ps-2">{ locale === "ar" ? obj?.traffic_ar : obj?.traffic }</td>
                              <td className="text-end pe-2 fw-bold text-info">
                                {Math.floor(obj?.price)} {t('SYP')}
                              
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                {/* Back to Home */}


                  <div className="col-12 text-center mt-4 mb-5">
                    <Link href="/" className="back-to-home-link">
                      <i className={`bi  ${locale === "ar" ? "bi-arrow-right ms-2" : "bi-arrow-left me-2"}`}></i>
                      {t('back_to_home')}
                    </Link>
                  </div>






              </div>
            </div>
          </div>


        )
        :( 



          <div className="row justify-content-center">
            <div className="col-12">
              <div className="custom_form_style p-4 p-md-5">
                <div className="prices mx-auto col-md-6">
                  {/* Wi-Fi Outdoor Packages */}
                  <div className="mb-5">
                    <h3 className="text-info mb-4 text-center placeholder-glow">
                      <span className="placeholder col-6"></span>
                    </h3>
                    <div className="table-responsive">
                      <table className="table table-borderless align-middle">
                        <thead className="border-bottom border-info">
                          <tr>
                            <th className="text-start ps-3 text-light placeholder-glow"><span className="placeholder col-4"></span></th>
                            <th className="text-center text-light placeholder-glow"><span className="placeholder col-4"></span></th>
                            <th className="text-end pe-3 text-light placeholder-glow"><span className="placeholder col-4"></span></th>
                          </tr>
                        </thead>
                        <tbody>
                          {[...Array(3)].map((_, index) => (
                            <tr key={index} className="border-bottom border-secondary text-light placeholder-glow">
                              <td className="text-start ps-3"><span className="placeholder col-6"></span></td>
                              <td className="text-center"><span className="placeholder col-4"></span></td>
                              <td className="text-end pe-3 fw-bold text-info"><span className="placeholder col-5"></span></td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                {/* Traffic Packages */}
                <div className="row g-4">
                  <div className="col-md-6">
                    <div className="border rounded p-3" style={{ backgroundColor: "rgba(0, 51, 102, 0.5)" }}>
                      <h4 className="text-center text-light mb-3 border-bottom border-info pb-2 placeholder-glow">
                        <span className="placeholder col-6"></span>
                      </h4>
                      <table className="table table-borderless mb-0">
                        <thead className="border-bottom border-info">
                          <tr className="text-light">
                            <th className="text-start ps-2 placeholder-glow"><span className="placeholder col-5"></span></th>
                            <th className="text-end pe-2 placeholder-glow"><span className="placeholder col-4"></span></th>
                          </tr>
                        </thead>
                        <tbody>
                          {[...Array(3)].map((_, index) => (
                            <tr key={index} className="border-bottom border-secondary text-light placeholder-glow">
                              <td className="text-start ps-2"><span className="placeholder col-6"></span></td>
                              <td className="text-end pe-2 fw-bold text-info"><span className="placeholder col-4"></span></td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <div className="col-md-6">
                    <div className="border rounded p-3" style={{ backgroundColor: "rgba(0, 51, 102, 0.5)" }}>
                      <h4 className="text-center text-light mb-3 border-bottom border-info pb-2 placeholder-glow">
                        <span className="placeholder col-6"></span>
                      </h4>
                      <table className="table table-borderless mb-0">
                        <thead className="border-bottom border-info">
                          <tr>
                            <th className="text-start ps-2 text-light placeholder-glow"><span className="placeholder col-5"></span></th>
                            <th className="text-end pe-2 text-light placeholder-glow"><span className="placeholder col-4"></span></th>
                          </tr>
                        </thead>
                        <tbody>
                          {[...Array(3)].map((_, index) => (
                            <tr key={index} className="border-bottom border-secondary text-light placeholder-glow">
                              <td className="text-start ps-2"><span className="placeholder col-6"></span></td>
                              <td className="text-end pe-2 fw-bold text-info"><span className="placeholder col-4"></span></td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                {/* Back to Home */}
                <div className="col-12 text-center mt-4 mb-5">
                  <Link href="/" className="back-to-home-link">
                    <i className={`bi  ${locale === "ar" ? "bi-arrow-right ms-2" : "bi-arrow-left me-2"}`}></i>
                    {t('back_to_home')}
                  </Link>
                </div>
              </div>
            </div>
          </div>
        ) }









          
        </div>
      </div>  
    </div>
  );
};

export default Page;
