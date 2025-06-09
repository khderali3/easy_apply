"use client";

import React, { useRef } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import * as THREE from "three";

const Particles: React.FC = () => {
  const pointsRef = useRef<THREE.Points>(null);

  const particleCount = 600;

  // Create initial positions once
  const positions = useRef(new Float32Array(particleCount * 3));
  if (!positions.current.length) {
    for (let i = 0; i < particleCount; i++) {
      positions.current[i * 3] = (Math.random() - 0.5) * 30; // X spread wider
      positions.current[i * 3 + 1] = (Math.random() - 0.5) * 20; // Y
      positions.current[i * 3 + 2] = (Math.random() - 0.5) * 30; // Z
    }
  }

  // Create sizes for each particle randomly
  const sizes = useRef(new Float32Array(particleCount));
  if (!sizes.current.length) {
    for (let i = 0; i < particleCount; i++) {
      sizes.current[i] = 0.05 + Math.random() * 0.15;
    }
  }

  // Create a color attribute that will be updated each frame
  const colors = useRef(new Float32Array(particleCount * 3));
  if (!colors.current.length) {
    for (let i = 0; i < particleCount; i++) {
      // Initial colors set to light blue
      colors.current[i * 3] = 0.38; // R (0 to 1)
      colors.current[i * 3 + 1] = 0.75; // G
      colors.current[i * 3 + 2] = 0.98; // B
    }
  }

  useFrame(({ clock }) => {
    if (!pointsRef.current) return;
    const time = clock.getElapsedTime();

    // Rotate slowly
    pointsRef.current.rotation.y = time * 0.06;
    pointsRef.current.rotation.x = time * 0.03;

    const posArray = pointsRef.current.geometry.attributes.position.array as Float32Array;
    const colorArray = pointsRef.current.geometry.attributes.color.array as Float32Array;

    for (let i = 0; i < particleCount; i++) {
      // Gentle vertical floating oscillation
      posArray[i * 3 + 1] = positions.current[i * 3 + 1] + Math.sin(time * 0.8 + i) * 0.5;

      // Cycle colors through hues over time (rainbow effect)
      const hue = (time * 20 + i * 360 / particleCount) % 360; // 0-360 degrees
      const rgb = hsvToRgb(hue / 360, 0.7, 1);

      colorArray[i * 3] = rgb.r;
      colorArray[i * 3 + 1] = rgb.g;
      colorArray[i * 3 + 2] = rgb.b;
    }

    pointsRef.current.geometry.attributes.position.needsUpdate = true;
    pointsRef.current.geometry.attributes.color.needsUpdate = true;
  });

  // Utility: HSV to RGB converter (values between 0-1)
  function hsvToRgb(h: number, s: number, v: number) {
    let r = 0,
      g = 0,
      b = 0;
    let i = Math.floor(h * 6);
    let f = h * 6 - i;
    let p = v * (1 - s);
    let q = v * (1 - f * s);
    let t = v * (1 - (1 - f) * s);
    switch (i % 6) {
      case 0:
        (r = v), (g = t), (b = p);
        break;
      case 1:
        (r = q), (g = v), (b = p);
        break;
      case 2:
        (r = p), (g = v), (b = t);
        break;
      case 3:
        (r = p), (g = q), (b = v);
        break;
      case 4:
        (r = t), (g = p), (b = v);
        break;
      case 5:
        (r = v), (g = p), (b = q);
        break;
    }
    return { r, g, b };
  }

  return (
    <points ref={pointsRef}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={particleCount}
          array={positions.current}
          itemSize={3}
        />
        <bufferAttribute
          attach="attributes-color"
          count={particleCount}
          array={colors.current}
          itemSize={3}
        />
        <bufferAttribute
          attach="attributes-size"
          count={particleCount}
          array={sizes.current}
          itemSize={1}
        />
      </bufferGeometry>
      <pointsMaterial
        vertexColors
        size={0.15}
        sizeAttenuation
        transparent
        opacity={0.8}
        blending={THREE.AdditiveBlending}
      />
    </points>
  );
};

const Page: React.FC = () => {
  return (
    <>
      {/* Bootstrap CDN */}
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet"
      />

      <div style={{ width: "100vw", height: "100vh", position: "relative", overflow: "hidden" }}>
        {/* Particle Background */}
        <Canvas
          // style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%", zIndex: 0 }}
          // camera={{ position: [0, 0, 15], fov: 75 }}

  style={{
    position: "absolute",
    top: 0,
    left: 0,
    width: "100%",
    height: "100%",
    zIndex: 0,
    backgroundColor: "#0d0d0d", // Dark background on Canvas
  }}
  camera={{ position: [0, 0, 15], fov: 75 }}



        >
          <ambientLight intensity={0.5} />
          <Particles />
        </Canvas>

        {/* Content on top */}
        <div
          className="container py-5"
          style={{
            position: "relative",
            zIndex: 10,
            color: "white",
            minHeight: "100vh",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
          }}
        >
          <h1 className="text-center mb-5" style={{ textShadow: "0 0 10px rgba(0,0,0,0.7)" }}>
            React-Three-Fiber Particle Background
          </h1>

          <div className="row g-4 justify-content-center">
            {[1, 2, 3, 4].map((n) => (
              <div key={n} className="col-12 col-sm-6 col-lg-3">
                <div
                  className="card h-100"
                  style={{
                    background: "rgba(0, 0, 0, 0.5)",
                    border: "1px solid rgba(255, 255, 255, 0.2)",
                    boxShadow: "0 0 15px rgba(97, 218, 251, 0.4)",
                  }}
                >
                  <div className="card-body">
                    <h5 className="card-title">Card {n}</h5>
                    <p className="card-text">
                      This is a cool card with transparent dark background so the glowing particles
                      show behind it.
                    </p>
                    <button className="btn btn-info">Action</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
};

export default Page;

// --------------

// and here is the component 


"use client";

import React, { useRef, useMemo } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

const NetworkBackground: React.FC = () => {
  const pointsRef = useRef<THREE.Points>(null);
  const linesRef = useRef<THREE.LineSegments>(null);

  const particleCount = 100;
  const maxDistance = 4;

  const positions = useMemo(() => {
    const arr = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount; i++) {
      arr[i * 3] = (Math.random() - 0.5) * 20;
      arr[i * 3 + 1] = (Math.random() - 0.5) * 12;
      arr[i * 3 + 2] = (Math.random() - 0.5) * 20;
    }
    return arr;
  }, [particleCount]);

  const linePositions = useMemo(() => {
    const lineSegments: number[] = [];
    for (let i = 0; i < particleCount; i++) {
      for (let j = i + 1; j < particleCount; j++) {
        const dx = positions[i * 3] - positions[j * 3];
        const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
        const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
        const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
        if (dist < maxDistance) {
          lineSegments.push(
            positions[i * 3],
            positions[i * 3 + 1],
            positions[i * 3 + 2],
            positions[j * 3],
            positions[j * 3 + 1],
            positions[j * 3 + 2]
          );
        }
      }
    }
    return new Float32Array(lineSegments);
  }, [positions, particleCount]);

  useFrame(({ clock }) => {
    const time = clock.getElapsedTime();

    if (pointsRef.current) {
      pointsRef.current.rotation.y = time * 0.1;
      pointsRef.current.rotation.x = time * 0.05;

      const posAttr = pointsRef.current.geometry.attributes.position;
      for (let i = 0; i < particleCount; i++) {
        const yBase = positions[i * 3 + 1];
        posAttr.array[i * 3 + 1] = yBase + Math.sin(time * 2 + i) * 0.3;
      }
      posAttr.needsUpdate = true;
    }

    if (linesRef.current) {
      linesRef.current.rotation.y = time * 0.1;
      linesRef.current.rotation.x = time * 0.05;
    }
  });

  return (
    <>
      <points ref={pointsRef}>
        <bufferGeometry>
          <bufferAttribute
            attach="attributes-position"
            count={particleCount}
            array={positions.slice()}
            itemSize={3}
          />
        </bufferGeometry>
        <pointsMaterial
          color="#61dafb"
          size={0.2}
          sizeAttenuation
          transparent
          opacity={0.9}
          depthWrite={false}
        />
      </points>

      <lineSegments ref={linesRef}>
        <bufferGeometry>
          <bufferAttribute
            attach="attributes-position"
            count={linePositions.length / 3}
            array={linePositions}
            itemSize={3}
          />
        </bufferGeometry>
        <lineBasicMaterial
          color="#61dafb"
          transparent
          opacity={0.2}
          depthWrite={false}
        />
      </lineSegments>
    </>
  );
};

export default NetworkBackground;

