import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { CartState } from "../utils/interface";

const initialState: CartState[] = []

const cartSlice = createSlice({
    name: "cart",
    initialState,
    reducers: {
        addToCart: (state, action: PayloadAction<CartState>) => {
            state.push(action.payload);
        },
        removeToCart: (state, action: PayloadAction<string>) => {
            return state.filter((item) => item.cartItemId !== action.payload);
        }
    }
});

export const { addToCart, removeToCart } = cartSlice.actions
export default cartSlice.reducer

