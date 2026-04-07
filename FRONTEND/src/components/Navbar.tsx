import { Link } from "react-router-dom";
import { HiShoppingCart } from "react-icons/hi2";

const Navbar: React.FC = () => {
  const type = "admin"; // Change to "admin" for admin view
  return (
    <div className="navbar bg-[#0F0F0F] shadow-md h-16 sticky top-0 z-10">
      <div className="flex-1">
        <Link to={"/"} className="btn btn-ghost text-xl text-[#D4AF37]">
          Restaurant Menu
        </Link>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          {type !== "admin" && (
            <li className="mr-2">
              <Link to={"/cart"}>
                <HiShoppingCart size={30} color="#D4AF37" />
              </Link>
              <span className="absolute -top-1 -right-2 min-w-2 rounded-full bg-[#D4AF37] text-black text-xs flex items-center justify-center font-bold">
                0
              </span>
            </li>
          )}
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
            <Link to={"/admin/auth"}>Login</Link>
          </li>
          <li className="md:hidden">
            <details>
              <summary className="text-[#D4AF37] text-lg">Click Here</summary>
              <ul className="rounded-t-none p-2">
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
                  <Link to={"/admin/auth"}>Login</Link>
                </li>
              </ul>
            </details>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Navbar;
