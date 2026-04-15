import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { AdminState } from "../utils/interface";

const initialState: AdminState = {
    type: "",
    isLoggedIn: false,
    token: ""
}

const adminSlice = createSlice({
    name: "admin",
    initialState,
    reducers: {
        addUser: (state, action: PayloadAction<AdminState>) => {
            return action.payload
        },
        removeUser: () => {
            return initialState
        }
    }
})

export const {addUser, removeUser} = adminSlice.actions
export default adminSlice.reducer