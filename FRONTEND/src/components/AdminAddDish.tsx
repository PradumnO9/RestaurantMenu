import React, { useState } from "react";
import type { FoodItem } from "../utils/interface";
import { MdClose } from "react-icons/md";
import { useNavigate } from "react-router-dom";

import { useAppSelector } from "../redux/hooks";
const AdminAddDish = () => {
  const foodCategory = useAppSelector((store) => store.menu.categories);

  const [dishData, setDishData] = useState<FoodItem>({
    id: "",
    name: "",
    description: "",
    categoryName: foodCategory[0]?.categoryName || "",
    imgUrl: "",
    price: {},
    customizable: false,
  });

  const navigate = useNavigate();
  const { type, isLoggedIn } = useAppSelector((store) => store.admin);

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string>("");
  const [pricePreview, setPreicePriview] = useState<{ [key: string]: number }>(
    {},
  );
  const [errorMessage, setErrorMessage] = useState<string>("");

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] || null;
    if (!e.target.files || e.target.files.length === 0) {
      setSelectedFile(null);
      setPreview("");
      return;
    }
    setSelectedFile(file);
    if (file) {
      setDishData({ ...dishData, imgUrl: URL.createObjectURL(file) });
    }
    setPreview(URL.createObjectURL(e.target.files[0]));

    return () => {
      URL.revokeObjectURL(preview);
    };
  };

  const handleAddPrice = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    setDishData({
      ...dishData,
      price: { ...dishData.price, ...pricePreview },
    });
    setPreicePriview({});
  };

  const handleRemovePrice = (
    e: React.MouseEvent<HTMLButtonElement>,
    index: number,
  ) => {
    e.preventDefault();
    const updatedPrice = { ...dishData.price };
    const keyToRemove = Object.keys(dishData.price)[index];
    delete updatedPrice[keyToRemove];
    setDishData({ ...dishData, price: updatedPrice });
  };

  const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (
      !dishData.name ||
      !dishData.description ||
      !dishData.categoryName ||
      Object.keys(dishData.price).length === 0 ||
      !dishData.imgUrl
    ) {
      setErrorMessage("Please fill in all fields.");
      return;
    }

    console.log("Dish Data:", dishData);
    setErrorMessage("");
    navigate("/restaurant/menu");
  };

  return isLoggedIn && type === "admin" ? (
    <div className="flex justify-center my-10 md:my-20">
      <form onSubmit={handleSubmit}>
        <div className="card card-border bg-[#1A1A1A] w-96">
          <div className="card-body">
            <h2 className="card-title text-3xl justify-center text-[#D4AF37]">
              Add Dish Item
            </h2>
            <div className="pt-2">
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">Dish Name</span>
                </div>
                <input
                  type="text"
                  className="input input-bordered w-full max-w-xs my-2"
                  placeholder="Enter dish name"
                  name="name"
                  value={dishData.name}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setDishData({ ...dishData, name: e.target.value })
                  }
                />
              </label>
            </div>
            <div>
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">
                    Dish Category
                  </span>
                </div>
                <select
                  value={dishData.categoryName}
                  onChange={(e: React.ChangeEvent<HTMLSelectElement>) => {
                    setDishData({
                      ...dishData,
                      categoryName: e.target.value,
                    });
                  }}
                  className="select mt-2 w-full max-w-xs"
                >
                  <option disabled={true}>Choose dish category</option>
                  {foodCategory.map((category) => (
                    <option key={category.id}>{category.categoryName}</option>
                  ))}
                </select>
              </label>
            </div>
            <div>
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">Description</span>
                </div>
                <textarea
                  className="textarea mt-2"
                  placeholder="Enter dish description"
                  name="description"
                  value={dishData.description}
                  onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) =>
                    setDishData({ ...dishData, description: e.target.value })
                  }
                ></textarea>
              </label>
            </div>
            <div>
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">
                    Select Dish Image
                  </span>
                </div>
                <input
                  type="file"
                  className="file-input w-full max-w-xs my-2 cursor-pointer"
                  onChange={handleImageChange}
                />
              </label>
              {selectedFile && (
                <div className="my-4 w-[96%]">
                  <img
                    src={preview ? preview : undefined}
                    alt="Preview"
                    className="w-full h-auto rounded-md"
                  />
                </div>
              )}
            </div>
            <div>
              <label className="form-control w-full max-w-xs">
                <div className="label mb-2">
                  <span className="label-text text-[#F5F5F5]">Price /-</span>
                </div>
                <div className="grid grid-cols-4 w-[96%]">
                  <div className="grid grid-cols-6 col-span-3">
                    <input
                      type="text"
                      className="input input-bordered w-full max-w-xs col-span-3 price-input"
                      name="pricePreview"
                      value={Object.keys(pricePreview)[0] || ""}
                      onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                        setPreicePriview({
                          [e.target.value.toLowerCase()]:
                            Object.values(pricePreview)[0] || 0,
                        })
                      }
                      placeholder="eg. full"
                    />
                    <input
                      type="text"
                      className="input input-bordered w-full max-w-xs col-span-3 price-input-noradius"
                      name="pricePreview"
                      value={Object.values(pricePreview)[0] || ""}
                      onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                        setPreicePriview({
                          [Object.keys(pricePreview)[0] || ""]: Number(
                            e.target.value,
                          ),
                        })
                      }
                      placeholder="eg. 250"
                    />
                  </div>
                  <button
                    onClick={handleAddPrice}
                    className="bg-[#D4AF37] hover:bg-[#E6C65C] cursor-pointer rounded-r-md col-span-1"
                  >
                    Add Price
                  </button>
                </div>
              </label>
              <ul>
                {Object.entries(dishData.price).map(([key, value], index) => (
                  <li
                    key={index}
                    className="text-[#F5F5F5] p-2 rounded-md bg-base-100 grid grid-cols-4 w-[96%] my-2"
                  >
                    <span className="col-span-3">
                      {key.charAt(0).toUpperCase() + key.slice(1)}: ₹{value}
                    </span>
                    <button
                      className="ml-auto mr-2 cursor-pointer"
                      onClick={(e: React.MouseEvent<HTMLButtonElement>) =>
                        handleRemovePrice(e, index)
                      }
                    >
                      <MdClose size={23} color="#D4AF37" />
                    </button>
                  </li>
                ))}
              </ul>
            </div>
            <div className="my-1">
              <label className="form-control w-full max-w-xs grid grid-cols-6">
                <div className="label col-span-5">
                  <span className="label-text text-[#F5F5F5]">
                    Customizable
                  </span>
                </div>
                <input
                  type="checkbox"
                  className="checkbox my-custom-checkbox col-span-1 ml-auto"
                  checked={dishData.customizable}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setDishData({
                      ...dishData,
                      customizable: e.target.checked,
                    })
                  }
                />
              </label>
            </div>
            {errorMessage && (
              <p className="text-red-500 text-sm mt-1">{errorMessage}</p>
            )}
            <div className="card-actions">
              <button className="bg-[#D4AF37] hover:bg-[#E6C65C] w-[96%] text-lg p-2 cursor-pointer rounded-md">
                Add Dish
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  ) : (
    <div className="flex justify-center my-40 md:my-20">
      <p className="text-red-500 text-xl">Please log in First...</p>
    </div>
  );
};

export default AdminAddDish;
