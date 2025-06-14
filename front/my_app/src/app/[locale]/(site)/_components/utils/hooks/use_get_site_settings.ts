'use client'

import { useEffect } from 'react';
import { useDispatch } from 'react-redux';

import  {finishIntialLoad, setSettings} from "@/app/[locale]/(site)/_components/redux/features/site_settings_slice"

import { usePageDataFetcher } from "@/app/public_utils/hooks/custom_api_hooks"

 
export default function useGetSiteSettings() {
	const dispatch = useDispatch();
 
    const { fetchData   , isLoading  , isError ,  data  } = usePageDataFetcher()

useEffect(() => {
	if(data && !isError){
		dispatch(setSettings(data));
		dispatch(finishIntialLoad());
	}
} , [data])
 

useEffect(() => {
      fetchData(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/systemSettingsApp/site/site_settings/`, "GET")

}, [ ]);

 
}


