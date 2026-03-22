import { Outlet } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

const Body = () => {
  return (
    <>
      <div className="bg-[#FAF9F6] min-h-screen">
        <Navbar />
        <Outlet />
      </div>
      <Footer />
    </>
  );
};

export default Body;
