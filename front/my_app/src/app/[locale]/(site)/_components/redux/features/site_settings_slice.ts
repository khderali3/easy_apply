import { createSlice } from "@reduxjs/toolkit";


 interface Settings {
  // define the shape of your settings object here, e.g.:
  email_service_enabled?: boolean;
  is_captcha_enabled?: boolean;
  maintenance_mode?: boolean;
  allow_user_registration?: boolean;
  allow_registration_without_email_verification?: boolean;
  // add other fields as needed
}

interface InitialState {
  isLoading: boolean;
  settings: Settings;
}


const initialState : InitialState = {
    isLoading : true,
    settings  :{}

}

const siteSettingsSlice = createSlice({
    name: 'site_settings',
    initialState,
    reducers: {

        finishIntialLoad: state => {
            state.isLoading = false
        },

        setSettings : (state, action) => {
            state.settings = action.payload
        },
    }
})

export const { finishIntialLoad, setSettings }  = siteSettingsSlice.actions;
export default siteSettingsSlice.reducer;

