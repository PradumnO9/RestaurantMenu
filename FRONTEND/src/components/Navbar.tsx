import { Link, useNavigate } from "react-router-dom";
import { HiShoppingCart } from "react-icons/hi2";
import useMenu from "../hooks/useMenu";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { addUser, removeUser } from "../redux/adminSlice";
import { useEffect } from "react";

const Navbar: React.FC = () => {
  const { isLoggedIn, type } = useAppSelector((store) => store.admin);
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const cart = useAppSelector((store) => store.cart);

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

  const handleLogout = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    dispatch(removeUser());
    localStorage.clear();
    navigate("/admin/auth");
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
              <li className="mr-2">
                <Link to={"/cart"}>
                  <HiShoppingCart size={30} color="#D4AF37" />
                </Link>
                <Link
                  to={"/cart"}
                  className="absolute -top-1 -right-2 min-w-2 rounded-full bg-[#D4AF37] text-black text-xs flex items-center justify-center font-bold"
                >
                  <span>{cart.length}</span>
                </Link>
              </li>
              <li className="text-[#D4AF37] text-lg sm:block hidden">
                <Link to={"/restaurant/menu"}>Menu</Link>
              </li>
              <li className="text-[#D4AF37] text-lg">
                <button onClick={handleLogout}>Logout</button>
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
              <li className="md:hidden">
                <details>
                  <summary className="text-[#D4AF37] text-lg">
                    Click Here
                  </summary>
                  <ul className="rounded-t-none bg-[#1A1A1A] p-2">
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
                </details>
              </li>
            </>
          )}
          {!isLoggedIn && (
            <li className="text-[#D4AF37] text-lg sm:block hidden">
              <Link to={"/admin/auth"}>Login</Link>
            </li>
          )}
        </ul>
      </div>
    </div>
  );
};

export default Navbar;

{
  /* <div className="dropdown">
  <div tabIndex={0} role="button" className="btn m-1">Click</div>
  <ul tabIndex="-1" className="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm">
    <li><a>Item 1</a></li>
    <li><a>Item 2</a></li>
  </ul>
</div> */
}
