import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { FoodItem, MenuState, FoodCategory } from "../utils/interface";

const initialState: MenuState = {
    menuItems: [],
    categories: []
}

const menuSlice = createSlice({
    name: "menu",
    initialState,
    reducers: {
        addMenuItems: (state, action: PayloadAction<{menuItems: FoodItem[]; categories: FoodCategory[]}>) => {
            state.menuItems = action.payload.menuItems;
            state.categories = action.payload.categories;  
        }
    }
})

export const { addMenuItems } = menuSlice.actions
export default menuSlice.reducer