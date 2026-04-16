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
        removeToCart: (state, action: PayloadAction<number>) => {
            const newData = [...state];
            newData.splice(action.payload, 1);
            return newData;
        }
    }
});

export const { addToCart } = cartSlice.actions
export default cartSlice.reducer

