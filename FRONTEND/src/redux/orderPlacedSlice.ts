import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { OrderPlacedState } from "../utils/interface";

const initialState: OrderPlacedState[] = []

const orderPlacedSlice = createSlice({
    name: "orderPlaced",
    initialState,
    reducers: {
        addToOrderList: (state, action: PayloadAction<OrderPlacedState>) => {
            state.push(action.payload);
        },
        emptyOrderList: () => {
            return initialState;
        }
    }
});

export const { addToOrderList, emptyOrderList } = orderPlacedSlice.actions;
export default orderPlacedSlice.reducer;