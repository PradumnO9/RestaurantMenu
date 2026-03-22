import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="navbar bg-[#0F0F0F] shadow-md h-16">
      <div className="flex-1">
        <Link to={"/"} className="btn btn-ghost text-xl text-[#D4AF37]">
          Restaurant Menu
        </Link>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          <li>
            <Link to={"/admin/auth"}>Login</Link>
          </li>
          <li>
            <details>
              <summary>Parent</summary>
              <ul className="rounded-t-none p-2">
                <li>
                  <Link to={"/"}>Link 1</Link>
                </li>
                <li>
                  <Link to={"/"}>Link 2</Link>
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
