"use client";
import { useLocale } from "next-intl";

import { toast } from "react-toastify";
 
import { useRouter, usePathname } from 'next/navigation';


const LanguageSwitcherComponent = () => {
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();
 
  const handleChangeLanguage = (e:any) => {
 
    document.cookie = `NEXT_LOCALE=${e.target.value}; path=/`;

    const newPathname = pathname.replace(/^\/(en|ar)/, `/${e.target.value}`);

 
    router.push(newPathname);




  };

  return (
 
 

    <div
      className={`  position-fixed top-0 m-3 rounded shadow-sm ${locale === "ar" ? 'end-0' : 'start-0'}`}
      style={{
        zIndex: 1050,
        width: "140px",
      }}
    >
      <select
        className="form-select form-select-sm"
        aria-label="Select language"
        value={locale}
        onChange={handleChangeLanguage}
      >
        <option value="en">English</option>
        <option value="ar">العربية</option>
      </select>
    </div>

  );
};

export default LanguageSwitcherComponent;
