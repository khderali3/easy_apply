
 
import "@/app/(site)/_components/assets/css/bootstrap.min.css"


import "@/app/globals.css";
import "@/app/(site)/_components/assets/css/style.css"


 
import Script from "next/script";
 
 



 

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
 
      <meta name="theme-color" content="#000000" />

     </head>

      
      <body >

  

      <div className="    "> 


      
        {children} 
      
         


      </div>
  
        <Script src={`${process.env.NEXT_PUBLIC_FRONTEND_URL}/js/bootstrap.bundle.min.js`} />


      </body>
    </html>

   
  );
}



