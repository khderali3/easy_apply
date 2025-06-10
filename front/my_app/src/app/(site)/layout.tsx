
import "@/app/(site)/_components/assets/css/bootstrap.min.css"
import 'bootstrap-icons/font/bootstrap-icons.css';
import "@/app/globals.css";



import "@/app/(site)/_components/assets/css/style.css"


 
import Script from "next/script";
 
 
import CanvasLayout from "./_components/jsx/canvas_layout";



 

export default  async function   RootLayout(
    {children} :  Readonly<{ children: React.ReactNode;}>
  ) {



  return (
  
     
    <html   >


    <head>

    <meta charSet="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
      {/* <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"></link> */}
      <meta name="theme-color" content="#000000" />

     </head>

      
      <body >

  

      <div className="    "> 

 


      <CanvasLayout>
        {children}
      </CanvasLayout>





      </div>
  
        <Script src={`${process.env.NEXT_PUBLIC_FRONTEND_URL}/js/bootstrap.bundle.min.js`} />


      </body>
    </html>

   
  );
}



