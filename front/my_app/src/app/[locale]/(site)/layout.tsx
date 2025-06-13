
 
import 'bootstrap/dist/css/bootstrap.min.css';

 
import 'bootstrap-icons/font/bootstrap-icons.css';


import "@/app/globals.css";


import "@/app/[locale]/(site)/_components/assets/css/style.css"

import CustomProvider from "./_components/redux/provider";


  

import Script from "next/script";
 
 
import CanvasLayout from "./_components/jsx/canvas_layout";

 

import { NextIntlClientProvider } from "next-intl";
import { getLocale, getMessages } from "next-intl/server";
 
 
import Setup from "./_components/utils/setup";


 
export default  async function   RootLayout(
    {children} :  Readonly<{ children: React.ReactNode;}>
  ) {

  const locale = await getLocale();
  const messages = await getMessages();

  return (
  
     
    <html   
    lang={locale}
    dir={ locale === "ar" ? "rtl" : " ltr"}

    >


    <head>

    <meta charSet="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
       <meta name="theme-color" content="#000000" />
 

     </head>

      
      <body >










      <NextIntlClientProvider messages={messages}>



              <CustomProvider>
                 <Setup />
                  <div className=""> 
           
 



                    <CanvasLayout>
                     

 




                      {children}


                      
                    </CanvasLayout>


                  </div>
            
              </CustomProvider>

      </NextIntlClientProvider>



        {/* <Script src={`${process.env.NEXT_PUBLIC_FRONTEND_URL}/js/bootstrap.bundle.min.js`} /> */}
        <Script src="/js/bootstrap.bundle.min.js" strategy="afterInteractive" />


      </body>
    </html>

   
  );
}



