"use client";

import React, { useState } from "react";
import { Canvas } from "@react-three/fiber";
import NetworkBackground from "../_components/jsx/NetworkBackground";

import Link from "next/link";

const Page: React.FC = () => {
  const [language, setLanguage] = useState("en");

  const handleLanguageChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setLanguage(e.target.value);
    // Add your language switching logic here
  };

return (
  <div className="page-wrapper">

    <div
      className="position-fixed top-0 start-0 m-3 rounded shadow-sm"
      style={{
        zIndex: 1050,
        width: "140px",
      }}
    >
      <select
        className="form-select form-select-sm"
        aria-label="Select language"
        value={language}
        onChange={handleLanguageChange}
      >
        <option value="en">English</option>
        <option value="ar">العربية</option>
      </select>
    </div>

    {/* 3D Canvas Background */}
    <Canvas
      className="canvas-background"
      camera={{ position: [0, 0, 25], fov: 50 }}
    >
      <ambientLight intensity={0.3} />
      <NetworkBackground />
    </Canvas>

    {/* start content */}
    <div className="foreground-container container py-5">
      <div className="text-center mb-5">
        <img src="/company_logo.png" alt="Logo" className="logo-img" />

        <h1 className="page-title">Wi-Fi Outdoor Service</h1>
      </div>

      <div className="container">
        <div className="row g-4 justify-content-center">
          {[1, 2, 3, 4].map((n) => (
            <div key={n} className="col-12 col-sm-6 col-lg-3">
              <Link href={`/services/${n}`} className="service-card-link">
                <div
                  className="service-card"
                  onMouseEnter={(e) => {
                    const el = e.currentTarget;
                    el.classList.add("service-card-hover");
                  }}
                  onMouseLeave={(e) => {
                    const el = e.currentTarget;
                    el.classList.remove("service-card-hover");
                  }}
                >
                  <div className="card-body text-center">
                    <div className="mb-2">
                      <i className="bi bi-wifi display-4 text-info"></i>
                    </div>
                    <h5 className="card-title">Service {n}</h5>
                    <p className="card-text mb-3">
                      Description for ISP service card number {n}. This card floats above
                      the animated network background.
                    </p>
                  </div>
                </div>
              </Link>
            </div>
          ))}
        </div>
      </div>
    </div>

    {/* end content */}


  </div>
);

};

export default Page;
