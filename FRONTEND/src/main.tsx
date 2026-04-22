import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { appStore, appPersistor } from "./redux/appStore.ts";
import { PersistGate } from "redux-persist/integration/react";
import "./index.css";
import App from "./App.tsx";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Provider store={appStore}>
      <PersistGate loading={<h1>Loading...</h1>} persistor={appPersistor}>
        <App />
      </PersistGate>
    </Provider>
  </StrictMode>,
);
