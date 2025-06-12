"use client";

import React, { useState, ReactNode } from "react";
import { Canvas } from "@react-three/fiber";
import NetworkBackground from "./NetworkBackground";


import LanguageSwitcherComponent from "./languge_switcher/languge_switcher";



interface CanvasLayoutProps {
  children: ReactNode;
}

const CanvasLayout: React.FC<CanvasLayoutProps> = ({ children }) => {
  const [language, setLanguage] = useState("en");

  const handleLanguageChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setLanguage(e.target.value);
    // Add your language switching logic here
  };

  return (
    <div className="page-wrapper">



    <LanguageSwitcherComponent />  


 


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
        {children}
      </div>
      {/* end content */}
    </div>
  );
};

export default CanvasLayout;
