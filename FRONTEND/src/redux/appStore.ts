import {configureStore} from "@reduxjs/toolkit";
import adminReducer from "./adminSlice";

export const appStore = configureStore({
    reducer: {
        admin: adminReducer
    }
})

export type RootState = ReturnType<typeof appStore.getState>
export type AppDispatch = typeof appStore.dispatch