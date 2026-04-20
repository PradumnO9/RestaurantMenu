import { BrowserRouter, Routes, Route } from "react-router-dom";
import Body from "./Body";
import AdminLogin from "./components/AdminLogin";
import Menu from "./components/Menu";
import ViewFoodItem from "./components/ViewFoodItem";
import AdminAddDish from "./components/AdminAddDish";
import AdminAddCategory from "./components/AdminAddCategory";
import Cart from "./components/Cart";
import OrderPlaced from "./components/OrderPlaced";

function App() {
  return (
    <BrowserRouter basename="/">
      <Routes>
        <Route path="/" element={<Body />}>
          <Route path="/admin/auth" element={<AdminLogin />} />
          <Route path="/restaurant/menu" element={<Menu />} />
          <Route
            path="/restaurant/menu/:foodItemId"
            element={<ViewFoodItem />}
          />
          <Route path="/admin/add-dish" element={<AdminAddDish />} />
          <Route path="/admin/add-category" element={<AdminAddCategory />} />
          <Route path="/restaurant/cart" element={<Cart />} />
          <Route path="/restaurant/order-placed" element={<OrderPlaced />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
