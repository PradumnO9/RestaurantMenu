import { Link, useNavigate } from "react-router-dom";
import { HiShoppingCart } from "react-icons/hi2";
import useMenu from "../hooks/useMenu";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { addUser, removeUser } from "../redux/adminSlice";
import { useEffect } from "react";
import { GiHamburgerMenu } from "react-icons/gi";
import axios from "axios";

const Navbar: React.FC = () => {
  const { isLoggedIn, type } = useAppSelector((store) => store.admin);
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const cart = useAppSelector((store) => store.cart);
  const orderPlaced = useAppSelector((store) => store.orderPlaced);

  useEffect(() => {
    const storedAdminData = localStorage.getItem("adminData");
    dispatch(
      addUser(
        storedAdminData
          ? JSON.parse(storedAdminData)
          : { type: "", isLoggedIn: false, token: "" },
      ),
    );
  }, []);

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       const data = await axios.get(
  //         "http://localhost:8000/api/admin/menuitemcategory/",
  //       );
  //       const jsonData = await data.json();
  //       console.log(jsonData);
  //     } catch (err) {
  //       console.error(err);
  //     }
  //   };

  //   fetchData();
  // }, []);

  const handleLogout = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (orderPlaced.length > 0) {
      alert("Please visit and clear My Orders first");
    } else {
      dispatch(removeUser());
      localStorage.clear();
      navigate("/admin/auth");
    }
  };

  useMenu();

  return (
    <div className="navbar bg-[#0F0F0F] shadow-md h-16 sticky top-0 z-10">
      <div className="flex-1">
        <Link to={"/"} className="btn btn-ghost text-xl text-[#D4AF37]">
          Restaurant Menu
        </Link>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          {isLoggedIn && type === "user" && (
            <>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <Link to={"/restaurant/menu"}>Menu</Link>
              </li>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <Link to={"/restaurant/order-placed"}>My Orders</Link>
                {orderPlaced.length > 0 && (
                  <Link
                    to={"/restaurant/cart"}
                    className="absolute -top-1 -right-2 min-w-2 rounded-full bg-[#D4AF37] text-black text-xs flex items-center justify-center font-bold"
                  >
                    <span>{orderPlaced.length}</span>
                  </Link>
                )}
              </li>
              <li className="mr-2">
                <Link to={"/restaurant/cart"}>
                  <HiShoppingCart size={30} color="#D4AF37" />
                </Link>
                {cart.length > 0 && (
                  <Link
                    to={"/restaurant/cart"}
                    className="absolute -top-1 -right-2 min-w-2 rounded-full bg-[#D4AF37] text-black text-xs flex items-center justify-center font-bold"
                  >
                    <span>{cart.length}</span>
                  </Link>
                )}
              </li>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <button onClick={handleLogout}>Logout</button>
              </li>
              <li className="md:hidden lg:hidden sm:hidden">
                <div className="dropdown dropdown-end">
                  <div
                    tabIndex={0}
                    role="button"
                    className="text-[#D4AF37] text-lg"
                  >
                    <GiHamburgerMenu size={30} />
                  </div>
                  <ul className="menu dropdown-content rounded-t-none bg-[#1A1A1A] p-2 rounded-box z-1 mt-4 w-52 shadow-sm">
                    <li className="text-[#D4AF37] text-lg">
                      <Link to={"/restaurant/menu"}>Menu</Link>
                    </li>
                    <li className="text-[#D4AF37] text-lg">
                      <Link to={"/restaurant/order-placed"}>My Orders</Link>
                      {orderPlaced.length > 0 && (
                        <Link
                          to={"/restaurant/cart"}
                          className="absolute -top-1 -right-2 min-w-2 rounded-full bg-[#D4AF37] text-black text-xs flex items-center justify-center font-bold"
                        >
                          <span>{orderPlaced.length}</span>
                        </Link>
                      )}
                    </li>
                    <li className="text-[#D4AF37] text-lg">
                      <button onClick={handleLogout}>Logout</button>
                    </li>
                  </ul>
                </div>
              </li>
            </>
          )}
          {isLoggedIn && type === "admin" && (
            <>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <Link to={"/restaurant/menu"}>Menu</Link>
              </li>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <Link to={"/admin/add-dish"}>Add Dish</Link>
              </li>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <Link to={"/admin/add-category"}>Add Category</Link>
              </li>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <button onClick={handleLogout}>Logout</button>
              </li>
              <li className="md:hidden lg:hidden sm:hidden">
                <div className="dropdown dropdown-end">
                  <div
                    tabIndex={0}
                    role="button"
                    className="text-[#D4AF37] text-lg"
                  >
                    <GiHamburgerMenu size={30} />
                  </div>
                  <ul className="menu dropdown-content rounded-t-none bg-[#1A1A1A] p-2 rounded-box z-1 mt-4 w-52 shadow-sm">
                    <li className="text-[#D4AF37] text-lg">
                      <Link to={"/restaurant/menu"}>Menu</Link>
                    </li>
                    <li className="text-[#D4AF37] text-lg">
                      <Link to={"/admin/add-dish"}>Add Dish</Link>
                    </li>
                    <li className="text-[#D4AF37] text-lg">
                      <Link to={"/admin/add-category"}>Add Category</Link>
                    </li>
                    <li className="text-[#D4AF37] text-lg">
                      <button onClick={handleLogout}>Logout</button>
                    </li>
                  </ul>
                </div>
              </li>
            </>
          )}
          {!isLoggedIn && (
            <li className="text-[#D4AF37] text-lg">
              <Link to={"/admin/auth"}>Login</Link>
            </li>
          )}
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
