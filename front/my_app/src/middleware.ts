import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
  locales: ['en', 'ar'],
  defaultLocale: 'en',
  localePrefix: 'always' // force /en, /ar in all URLs
});

export const config = {
  matcher: ['/', '/((?!api|_next|.*\\..*).*)'] // Exclude API, static files, etc.
};