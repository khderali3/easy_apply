// import { getRequestConfig } from "next-intl/server";
// import { cookies } from "next/headers";

// export default getRequestConfig(async () => {
  
//   const cookieStore = await cookies();
//   const locale = cookieStore.get("language")?.value || "en";

//   return {
//     locale,
//     messages: (await import(`../messages/${locale}.js`)).default,
//   };
// });


 


 

import { getRequestConfig } from 'next-intl/server';
import { cookies } from 'next/headers';

export default getRequestConfig(async ({ params } : any) => {
  const cookieStore = await cookies();  // <-- await here!
  const localeCookie = cookieStore.get('NEXT_LOCALE'); // now works
  const cookieLocale = localeCookie?.value;

  const localeFromParams = params?.locale;
  const locale = localeFromParams || cookieLocale || 'en';

  return {
    locale,
    messages: (await import(`../messages/${locale}.js`)).default,
  };
});

