import React from "react";
import Link from "next/link";
import { getLocale } from "next-intl/server";
import { getErrorMessage } from "@/app/public_utils/utils";

const Page: React.FC = async () => {
  const locale = await getLocale();
  let data: any = {};
  let errorMessage: any;

  try {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/easyApplyApp/site/get_app_index/`,
      { cache: "no-store" }
    );

    const json = await res.json();

    if (!res.ok) {
      throw new Error(
        typeof json === "object" ? JSON.stringify(json) : String(json)
      );
    }

    data = json;
  } catch (error: any) {
    errorMessage =
      getErrorMessage(error?.data || error?.message) ||
      "Something went wrong";
  }

  // Check if critical data is missing or empty
  const hasData =
    data &&
    (data.compoany_logo ||
      data.app_index_title?.title ||
      data.app_index_title?.title_ar) &&
    (data.card_request_agent_label ||
      data.card_request_service_label ||
      data.card_check_request_label ||
      data.card_service_prices_label);

  return (
    <div>
      {/* Show error message if exists */}
      {errorMessage && (
        <div className="custom-error-box my-3 mx-auto">
          <div className="custom-error-title">
            {locale === "ar" ? "خطأ" : "Error"}
          </div>
          <div className="custom-error-message">{errorMessage}</div>
        </div>
      )}

      {/* Show content - real data or placeholders */}
      <div>
        <div className="text-center mb-5">
          {data?.compoany_logo ? (
            <img
              src={data.compoany_logo}
              alt="Logo"
              className="logo-img"
              style={{ maxWidth: "150px" }}
            />
          ) : (
            // Logo Placeholder (circle)
            <div className="placeholder-glow mx-auto">
              <span
                className="placeholder rounded-circle"
                style={{ width: "150px", height: "150px", display: "inline-block" }}
              ></span>
            </div>

          )}

          {data?.app_index_title?.title || data?.app_index_title?.title_ar ? (
            <h1 className="page-title mt-3">
              {locale === "ar"
                ? data.app_index_title?.title_ar
                : data.app_index_title?.title}
            </h1>
          ) : (
            // Title placeholder
            <h1 className="page-title mt-3 placeholder-glow">
              <span className="placeholder col-6"></span>
            </h1>
          )}
        </div>

        <div className="container">
          <div className="row g-4 justify-content-center">
            {[
              {
                href: "/agent_request",
                label: data?.card_request_agent_label,
              },
              {
                href: "/service_request",
                label: data?.card_request_service_label,
              },
              {
                href: "/check_status",
                label: data?.card_check_request_label,
              },
              {
                href: "/service_Price",
                label: data?.card_service_prices_label,
              },
            ].map((card, idx) => (
              <div key={idx} className="col-12 col-sm-6 col-lg-3 d-flex">
                {card.label ? (
                  <Link href={card.href} className="service-card-link w-100">
                    <div className="service-card h-100">
                      <div className="card-body text-center p-2">
                        <div className="mb-2">
                          <i
                            className={`bi display-4 text-info ${card.label.bootstrap_icon}`}
                          ></i>
                        </div>
                        <h5 className="card-title">
                          {locale === "ar"
                            ? card.label.title_ar
                            : card.label.title}
                        </h5>
                        <p className="card-text mb-3">
                          {locale === "ar"
                            ? card.label.details_ar
                            : card.label.details}
                        </p>
                      </div>
                    </div>
                  </Link>
                ) : (
                  <div className="service-card h-100 w-100 placeholder-glow">
                    <div className="card-body text-center p-2">
                      <div className="mb-2">
                        {/* icon placeholder */}
                        <span className="placeholder col-6 display-4"></span>
                      </div>
                      <h5 className="card-title">
                        <span className="placeholder col-7"></span>
                      </h5>
                      <p className="card-text mb-3">
                        <span className="placeholder col-10"></span>
                        <span className="placeholder col-8"></span>
                        <span className="placeholder col-6"></span>
                      </p>
                    </div>
                  </div>
                )}
              </div>
            ))}

 





          </div>
        </div>
      </div>
    </div>
  );
};

export default Page;
