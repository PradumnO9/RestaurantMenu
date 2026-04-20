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
        },
        increseQty: (state, action: PayloadAction<string>) => {
            state.forEach((item) => {
                if (item.cartItemId === action.payload) {
                    if (item.foodQty > 0) {
                        item.foodPrice += item.foodPrice/item.foodQty; 
                        item.foodQty++;
                    }
                }
            })
        },
        decreseQty: (state, action: PayloadAction<string>) => {
            state.forEach((item) => {
                if (item.cartItemId === action.payload) {
                    if (item.foodQty > 1) {
                        item.foodPrice -= item.foodPrice/item.foodQty; 
                        item.foodQty--;
                    }
                }
            })
        },
        deleteCart: () => {
            return initialState;
        }
    }
});

export const { addToCart, removeToCart, deleteCart, increseQty, decreseQty } = cartSlice.actions
export default cartSlice.reducer

