// import type { NextConfig } from "next";

// const nextConfig: NextConfig = {
 
// };

// export default nextConfig;





const createNextIntlPlugin = require('next-intl/plugin');
 
// const withNextIntl = createNextIntlPlugin('@/app/i18n/request.ts');
 
const withNextIntl = createNextIntlPlugin('./src/app/i18n/request.ts');



import type { NextConfig } from "next";

const nextConfig: NextConfig = {
 	reactStrictMode: false,  // custom by khder
	productionBrowserSourceMaps: false,  // custom by khder
};

 

module.exports = withNextIntl(nextConfig);

