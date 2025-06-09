import type { Metadata } from "next";
 
 

import "@/app/globals.css"


export const metadata: Metadata = {
  title: "Easy Apply dashboard ",
  description: "Easy Apply",
};


export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
  <html lang="en" style={{ backgroundColor: 'yellow' }}>
      <body  >
        {children}
      </body>
    </html>
  );
}
