'use client';

import { store } from "./store";
import { Provider } from "react-redux";
import { Suspense } from 'react';

import Loading from "../../Loading";


import { ReactNode } from "react";

type Props = {
  children: ReactNode;
};

 

export default function CustomProvider({ children } : Props) {
	return <Provider store={store}>

		<Suspense fallback={<Loading />}>
				{children}
		</Suspense>

		</Provider>;
}