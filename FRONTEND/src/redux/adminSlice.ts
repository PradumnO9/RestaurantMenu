import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { AdminData } from "../utils/interface";

const initialState: AdminData = {
    email: "",
    password: "",
    isLoggedIn: false,
    type: ""
}

const adminSlice = createSlice({
    name: "admin",
    initialState,
    reducers: {
        addUser: (state, action: PayloadAction<AdminData>) => {
            return action.payload
        },
        removeUser: () => {
            return initialState
        }
    }
})

export const {addUser, removeUser} = adminSlice.actions
export default adminSlice.reducer