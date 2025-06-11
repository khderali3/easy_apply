import { apiSlice } from "../services/apiSlice";

const siteApiSlice = (apiSlice as any).injectEndpoints({
  endpoints: (builder: any) => ({
    customFetch: (builder.mutation as any)({
      query: ({ url, method = 'GET', body = null, headers = {} }: any) => {
        const requestConfig: any = {
          url,
          method,
          headers,
        };

        if (body !== null) {
          requestConfig.body = body;
        }

        return requestConfig;
      },
    }),
  }),
});

export const {
  useCustomFetchMutation,
} = siteApiSlice;
