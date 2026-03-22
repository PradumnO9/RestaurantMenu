import { useState } from "react";
import { useNavigate } from "react-router-dom";
import type { AdminData } from "../utils/interface";
import { FaRegEyeSlash } from "react-icons/fa";
import { FaRegEye } from "react-icons/fa";

const AdminLogin = () => {
  const [data, setData] = useState<AdminData>({
    email: "",
    password: "",
  });
  const [eyeToggle, setEyeToggle] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const navigate = useNavigate();

  const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!data.email || !data.password) {
      setErrorMessage("Please fill in all fields.");
      return;
    }

    console.log(data);
    return navigate("/admin/dashboard");
  };
  return (
    <div className="flex justify-center my-40 md:my-20">
      <form onSubmit={handleSubmit}>
        <div className="card card-border bg-[#1A1A1A] w-96">
          <div className="card-body">
            <h2 className="card-title text-3xl justify-center text-[#D4AF37]">
              Login
            </h2>
            <div className="py-2">
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">Email ID</span>
                </div>
                <input
                  type="text"
                  className="input input-bordered w-full max-w-xs my-2"
                  name="email"
                  value={data.email}
                  onChange={handleChange}
                />
              </label>
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">Password</span>
                </div>
                <div className="flex items-center">
                  <input
                    type={eyeToggle ? "text" : "password"}
                    className="input input-bordered w-full max-w-xs my-2"
                    name="password"
                    value={data.password}
                    onChange={handleChange}
                  />
                  {eyeToggle ? (
                    <FaRegEye
                      size={25}
                      className="absolute right-12 cursor-pointer"
                      onClick={() => setEyeToggle(!eyeToggle)}
                    />
                  ) : (
                    <FaRegEyeSlash
                      size={25}
                      className="absolute right-12 cursor-pointer"
                      onClick={() => setEyeToggle(!eyeToggle)}
                    />
                  )}
                </div>
              </label>
              {errorMessage && (
                <p className="text-red-500 text-sm mt-2">{errorMessage}</p>
              )}
            </div>
            <div className="card-actions">
              <button className="bg-[#D4AF37] hover:bg-[#E6C65C] w-[96%] text-lg p-2 cursor-pointer rounded-md">
                Login
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
};

export default AdminLogin;
