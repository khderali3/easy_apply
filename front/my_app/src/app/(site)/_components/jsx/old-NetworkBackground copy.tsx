"use client";

import React, { useRef, useMemo } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

const NetworkBackground: React.FC = () => {
  const pointsRef = useRef<THREE.Points>(null);
  const linesRef = useRef<THREE.LineSegments>(null);
  const lastTimeRef = useRef(0);

  const particleCount = 50;
  const maxDistance = 4;

  // Generate fixed random points once
  const positions = useMemo(() => {
    const arr = new Float32Array(particleCount * 3);
    for (let i = 0; i < particleCount; i++) {
      arr[i * 3] = (Math.random() - 0.5) * 20;
      arr[i * 3 + 1] = (Math.random() - 0.5) * 12;
      arr[i * 3 + 2] = (Math.random() - 0.5) * 20;
    }
    return arr;
  }, [particleCount]);

  // Calculate line segments between close points once
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

    // Throttle updates to ~60fps (16ms)
    if (time - lastTimeRef.current < 0.016) return;
    lastTimeRef.current = time;

    if (pointsRef.current) {
      pointsRef.current.rotation.y = time * 0.1;
      pointsRef.current.rotation.x = time * 0.05;

      const posAttr = pointsRef.current.geometry.attributes.position as THREE.BufferAttribute;
      const posArray = posAttr.array as Float32Array;

      // Update y position with sine wave, based on fixed base y position
      for (let i = 0; i < particleCount; i++) {
        const yBase = positions[i * 3 + 1];
        posArray[i * 3 + 1] = yBase + Math.sin(time * 2 + i) * 0.3;
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
            args={[positions, 3]} // Use positions directly, no slice
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
            args={[linePositions, 3]} // Use precomputed linePositions directly
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
