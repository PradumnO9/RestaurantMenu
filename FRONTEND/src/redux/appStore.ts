import {configureStore} from "@reduxjs/toolkit";
import adminReducer from "./adminSlice";
import menuReducer from "./menuSlice";

export const appStore = configureStore({
    reducer: {
        admin: adminReducer,
        menu: menuReducer
    }
})

export type RootState = ReturnType<typeof appStore.getState>
export type AppDispatch = typeof appStore.dispatch