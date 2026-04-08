import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import type { AdminState } from "../utils/interface";

const initialState: AdminState = {
    value: {
        email: "",
        password: ""
    } 
}

const adminSlice = createSlice({
    name: "admin",
    initialState,
    reducers: {
        addUser: (state, action: PayloadAction<{email: string, password: string}>) => {
            state.value.email = action.payload.email
            state.value.password = action.payload.password
        },
        removeUser: (state) => {
            state.value.email = ""
            state.value.password = ""
        }
    }
})

export const {addUser, removeUser} = adminSlice.actions
export default adminSlice.reducer