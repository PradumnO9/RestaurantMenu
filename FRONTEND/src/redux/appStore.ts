import { combineReducers, configureStore } from "@reduxjs/toolkit";
import { persistStore, persistReducer } from "redux-persist";
import adminReducer from "./adminSlice";
import menuReducer from "./menuSlice";
import cartReducer from "./cartSlice";
import orderPlacedReducer from './orderPlacedSlice';
import { customStorage } from "../utils/constant";

const persistConfig = {
  key: 'root',
  storage: customStorage,
  whitelist: ["cart", "orderPlaced"], // only whitelist slice will be persisted
  timeout: 10000, // Increase timeout to 10 seconds
}

const rootReducer = combineReducers({
  admin: adminReducer,
  menu: menuReducer,
  cart: cartReducer,
  orderPlaced: orderPlacedReducer
});

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const appStore = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST', 'persist/REHYDRATE', 'persist/REGISTER'],
      },
    }),
});

export type RootState = ReturnType<typeof appStore.getState>
export type AppDispatch = typeof appStore.dispatch
export const appPersistor = persistStore(appStore);