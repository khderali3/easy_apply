'use client'

import { useLocale } from 'next-intl'
import { ar, enUS } from "date-fns/locale"; // Import necessary locales
import { parseISO, format } from "date-fns";
 


export function useFormatNumber() {
  const locale = useLocale()

  const formatNumber = (number:number) => {
    if(number){
        const formatter = new Intl.NumberFormat(locale === 'ar' ? 'ar-EG' : 'en-US');
        return formatter.format(number);
    }
  };

  return formatNumber;
}





export const useFormatData = () => {

    const locale = useLocale()

    const currentLocale = locale === "ar" ? ar : enUS;

    const getformatDate = (dateString:any) => {

        if (dateString) {
            return format(parseISO(dateString), 'dd MMM yyyy - h:mm a', { locale: currentLocale });
        }
    };

    return getformatDate


}


 


