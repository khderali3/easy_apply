import { configureStore } from "@reduxjs/toolkit";
import authReducer from './features/authSlice'
import { apiSlice } from "./services/apiSlice";

import siteSettingsSlice  from "./features/site_settings_slice";


export const store = configureStore({
                reducer: {
                    [apiSlice.reducerPath] : apiSlice.reducer,
                    auth: authReducer,
                    site_settings : siteSettingsSlice,
                    },
                middleware: getDefaultMiddleware =>
                    getDefaultMiddleware().concat(apiSlice.middleware),
                devTools: true
            })

