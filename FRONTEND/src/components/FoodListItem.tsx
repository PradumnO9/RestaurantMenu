import React, { useState } from "react";
import type { FoodItem } from "../utils/interface";
import PopUp from "./PopUps/PopUp";
import { Link } from "react-router-dom";
interface IPROPS {
  itemData: FoodItem;
}

const FoodListItem: React.FC<IPROPS> = ({ itemData }) => {
  const [isPopUpOpen, setIsPopUpOpen] = useState(false);
  const { name, id, description, customizable, imgUrl, price } = itemData;

  const type = "admin";

  const openPopUp = () => setIsPopUpOpen(true);
  const closePopUp = () => setIsPopUpOpen(false);

  return (
    <div>
      <ul className="list bg-base-100 rounded-box shadow-md">
        <li className="list-row flex">
          <div>
            <div>{name}</div>
            <p className="list-col-wrap text-xs max-w-xs md:max-w-md">
              {description}
            </p>
            <div className="text-xs uppercase font-semibold opacity-60">
              {Object.entries(price).map(([size, value]) => (
                <span key={size}>
                  {size.charAt(0).toUpperCase() + size.slice(1)}: ₹{value}
                  <br />
                </span>
              ))}
            </div>
          </div>
          <div className="ml-auto">
            <div className="relative">
              <img
                className="size-28 rounded-box max-w-md"
                src={imgUrl}
                alt={name}
              />
              <div className="flex justify-center absolute -bottom-3 w-full">
                {type === "admin" ? (
                  <Link
                    to={`/restaurant/menu/${id}`}
                    className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
                  >
                    View Item
                  </Link>
                ) : (
                  <button
                    onClick={customizable ? openPopUp : undefined}
                    className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
                  >
                    Add Item
                  </button>
                )}
              </div>
            </div>
          </div>
        </li>
      </ul>
      <PopUp isOpen={isPopUpOpen} onClose={closePopUp}>
        <div className="bg-[#1A1A1A] rouned-xl px-20 py-10 flex flex-col gap-5 items-center mx-3">
          <ul>
            <li className="flex flex-col gap-2">
              {price &&
                Object.entries(price).map(([size, value]) => (
                  <label
                    key={size}
                    className="flex items-center gap-2 cursor-pointer"
                  >
                    <input
                      type="radio"
                      name="radio-3"
                      className="radio radio-neutral"
                      value={value}
                      defaultChecked
                    />
                    <span>
                      {size.charAt(0).toUpperCase() + size.slice(1)}: ₹{value}
                    </span>
                  </label>
                ))}
            </li>
          </ul>
          <button className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer ml-auto">
            Add Item
          </button>
        </div>
      </PopUp>
    </div>
  );
};

export default FoodListItem;

// <div className="flex items-center justify-center my-3">
//   <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
//     <FaPlus size={22} />
//   </div>
//   <div className="w-8 text-center">1</div>
//   <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
//     <FaMinus size={22} />
//   </div>
// </div>
// <div className="flex justify-center">
//   <button className="bg-[#D4AF37] px-2 py-1 rounded-md">
//     Add Item
//   </button>
// </div>

{
  /* <div key={index}>
                    <label className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="radio"
                        name="radio-3"
                        className="radio radio-neutral"
                        value={parseInt(item.split(" ")[1], 10)}
                        defaultChecked
                      />
                      <span>{item} /-</span>
                    </label>
                  </div> */
}
