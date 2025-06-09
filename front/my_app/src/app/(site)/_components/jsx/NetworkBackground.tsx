"use client";

import React, { useRef, useMemo } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

const NetworkBackground: React.FC = () => {
  const pointsRef = useRef<THREE.Points>(null);
  const linesRef = useRef<THREE.LineSegments>(null);

  const particleCount = 100; // fewer points for clarity & performance
  const maxDistance = 4; // max distance to connect points with a line

  // Generate fixed random points in 3D space once
  const positions = useMemo(() => {
    const arr = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount; i++) {
      arr[i * 3] = (Math.random() - 0.5) * 20;
      arr[i * 3 + 1] = (Math.random() - 0.5) * 12;
      arr[i * 3 + 2] = (Math.random() - 0.5) * 20;
    }
    return arr;
  }, [particleCount]);

  // Calculate line segments between close points
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

  // Animate rotation and gentle floating effect
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
      {/* Points */}
      <points ref={pointsRef}>
        <bufferGeometry>
          <bufferAttribute
            attach="attributes-position"
            count={particleCount}
            array={positions.slice()} // copy to keep original stable
            itemSize={3}
          />
        </bufferGeometry>
        <pointsMaterial
          color="#66ccff"
          size={0.25}
          sizeAttenuation
          transparent
          opacity={0.8}
          depthWrite={false}
        />
      </points>

      {/* Lines */}
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
          color="#66ccff"
          transparent
          opacity={0.15}
          depthWrite={false}
        />
      </lineSegments>
    </>
  );
};

export default NetworkBackground;
