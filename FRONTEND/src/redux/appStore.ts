import {configureStore} from "@reduxjs/toolkit";
import adminReducer from "./adminSlice";
import menuReducer from "./menuSlice";
import cartReducer from "./cartSlice";
import orderPlacedReducer from './orderPlacedSlice';

export const appStore = configureStore({
    reducer: {
        admin: adminReducer,
        menu: menuReducer,
        cart: cartReducer,
        orderPlaced: orderPlacedReducer
    }
})

export type RootState = ReturnType<typeof appStore.getState>
export type AppDispatch = typeof appStore.dispatch