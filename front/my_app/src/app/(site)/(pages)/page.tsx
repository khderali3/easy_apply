"use client";

import React from "react";
import { Canvas } from "@react-three/fiber";
import NetworkBackground from "../_components/jsx/NetworkBackground";

const Page: React.FC = () => {
  return (
    <>
      <div
        style={{
          width: "100vw",
          height: "100vh",
          position: "relative",
          overflowY: "auto", // <-- Changed here to enable vertical scroll if needed
          background: "linear-gradient(135deg, #001f3f 0%, #003366 100%)",
          color: "white",
          fontFamily:
            '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif',
        }}
      >
        {/* 3D Canvas Background */}
        <Canvas
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100vw",
            height: "100vh",
            zIndex: 0,
            backgroundColor: "transparent",
            pointerEvents: "none",
          }}
          // camera={{ position: [0, 0, 25], fov: 60 }}
            camera={{ position: [0, 0, 25], fov: 50 }}

        >
          <ambientLight intensity={0.3} />
          <NetworkBackground />
        </Canvas>

        {/* Foreground content */}
        <div
          className="container py-5"
          style={{
            position: "relative",
            zIndex: 10,
            minHeight: "100vh",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
          }}
        >

          <div className=" text-center mb-5">

            <img
              // src="https://wifi.aya.sy/storage/images/AYA-LOGO.png"
              src="/company_logo.png"
              alt="Logo"
              className="img-fluid text-light"
            style={{ maxWidth: "150px", height: "auto", filter: "brightness(1.5)" }}
            />

              <h1
                className=" "
                style={{
                  textShadow:
                    "0 0 8px rgba(102,204,255,0.9), 0 0 20px rgba(102,204,255,0.7)",
                }}
              >
                {/* ISP Network Visualizer */}
                Wi-Fi Outdoor Service
              </h1>

          </div>



          {/* <h1
            className="text-center mb-5"
            style={{
              textShadow:
                "0 0 8px rgba(102,204,255,0.9), 0 0 20px rgba(102,204,255,0.7)",
            }}
          >
            ISP Network Visualizer
          </h1> */}

            <div className="container ">

              <div className="row g-4 justify-content-center">
                {[1, 2, 3, 4].map((n) => (
                  <div key={n} className="col-12 col-sm-6 col-lg-3">
                    <div
                      className="card h-100"
                      style={{
                        // background: "linear-gradient(145deg, #004466, #00334d)",
                        background: "linear-gradient(145deg, rgba(0, 68, 102, 0.9), rgba(0, 51, 77, 0.9))",

                        border: "1px solid rgba(102, 204, 255, 0.6)",
                        boxShadow:
                          "0 4px 15px rgba(102, 204, 255, 0.5), inset 0 0 8px rgba(102, 204, 255, 0.4)",
                        color: "#cceeff",
                        transition: "transform 0.3s ease, box-shadow 0.3s ease",
                        cursor: "default",
                        userSelect: "none",
    
                      }}
                      onMouseEnter={(e) => {
                        const el = e.currentTarget;
                        el.style.transform = "scale(1.05)";
                        el.style.boxShadow =
                          "0 8px 30px rgba(102, 204, 255, 0.8), inset 0 0 15px rgba(102, 204, 255, 0.6)";
                      }}
                      onMouseLeave={(e) => {
                        const el = e.currentTarget;
                        el.style.transform = "scale(1)";
                        el.style.boxShadow =
                          "0 4px 15px rgba(102, 204, 255, 0.5), inset 0 0 8px rgba(102, 204, 255, 0.4)";
                      }}
                    >
                      <div className="card-body">
                        <h5 className="card-title">Service {n}</h5>
                        <p className="card-text">
                          Description for ISP service card number {n}. This card floats above the
                          animated network background.
                        </p>
                        <button className="btn btn-info">Learn More</button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>

            </div>




        </div>
      </div>
    </>
  );
};

export default Page;
