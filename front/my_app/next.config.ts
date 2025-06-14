 

// const createNextIntlPlugin = require('next-intl/plugin');
// const withNextIntl = createNextIntlPlugin('./src/app/i18n/request.ts');

// import type { NextConfig } from "next";

// const nextConfig: NextConfig = {
//  	reactStrictMode: false,  // custom by khder
// 	productionBrowserSourceMaps: false,  // custom by khder
// };

// module.exports = withNextIntl(nextConfig);


/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false, // disable Strict Mode to prevent double renders in dev
  productionBrowserSourceMaps: false,
};

const createNextIntlPlugin = require('next-intl/plugin');
const withNextIntl = createNextIntlPlugin('./src/app/i18n/request.ts');

module.exports = withNextIntl(nextConfig);