import React, { useState } from "react";
import type { CartState, FoodItem } from "../utils/interface";
import PopUp from "./PopUps/PopUp";
import { Link } from "react-router-dom";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { FaPlus } from "react-icons/fa";
import { FaMinus } from "react-icons/fa6";
import { addToCart } from "../redux/cartSlice";
interface IPROPS {
  itemData: FoodItem;
}

const FoodListItem: React.FC<IPROPS> = ({ itemData }) => {
  const { name, id, description, customizable, imgUrl, price } = itemData;
  const [cartItem, setCartItem] = useState<CartState>({
    cartItemId: "",
    foodId: id,
    foodName: name,
    foodDescription: description,
    foodImg: imgUrl,
    foodPrice: 0,
    foodQty: 0,
    foodPriceCategory: "",
  });
  const [isPopUpOpen, setIsPopUpOpen] = useState(false);
  const [itemQty, setItemQty] = useState<number>(0);
  const [selectedPrice, setSelectedPrice] = useState<number>(0);
  const dispatch = useAppDispatch();
  const uniqueId = crypto.randomUUID();

  const { type } = useAppSelector((store) => store.admin);

  const openPopUp = () => setIsPopUpOpen(true);
  const closePopUp = () => setIsPopUpOpen(false);

  const totalPrice: number = itemQty * selectedPrice;

  const plusHandler = () => {
    const nextQty = itemQty + 1;
    setItemQty(nextQty);
    setCartItem((prev) => ({
      ...prev,
      foodQty: nextQty,
      foodPrice: nextQty * selectedPrice,
    }));
  };
  const minusHandler = () => {
    if (itemQty > 0) {
      const prevQty = itemQty - 1;
      setItemQty(prevQty);
      setCartItem((prev) => ({
        ...prev,
        foodQty: prevQty,
        foodPrice: prevQty * selectedPrice,
      }));
    }
  };

  const handleAddItem = () => {
    console.log(cartItem);
    dispatch(addToCart(cartItem));
  };

  return (
    <div>
      <ul className="list bg-base-100 rounded-box shadow-md">
        <li className="list-row flex">
          <div>
            <div>{name}</div>
            <p className="list-col-wrap text-xs max-w-xs md:max-w-md">
              {description}
            </p>
            <div className="text-xs uppercase font-semibold opacity-60 mt-1">
              {Object.entries(price).map(([size, value]) => (
                <span key={size}>
                  {size.charAt(0).toUpperCase() + size.slice(1)}: ₹{value}
                  <br />
                </span>
              ))}
            </div>
          </div>
          <div className="ml-auto relative">
            <img
              className="size-28 rounded-box max-w-md"
              src={imgUrl}
              alt={name}
            />
            <div className="flex justify-center mt-2">
              {type === "admin" && (
                <Link
                  to={`/restaurant/menu/${id}`}
                  className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
                >
                  View Item
                </Link>
              )}
              {type === "user" && (
                <button
                  onClick={customizable ? openPopUp : undefined}
                  className="bg-[#D4AF37] px-2 py-1 rounded-md hover:bg-[#E6C65C] cursor-pointer"
                >
                  Add Item
                </button>
              )}
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
                      onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                        setSelectedPrice(Number(e.target.value));
                        setCartItem((prev) => ({
                          ...prev,
                          cartItemId: uniqueId,
                          foodPrice: itemQty * Number(e.target.value),
                          foodPriceCategory: size,
                        }));
                      }}
                    />
                    <span>
                      {size.charAt(0).toUpperCase() + size.slice(1)}: ₹{value}
                    </span>
                  </label>
                ))}
            </li>
            <li className="flex justify-center items-center gap-8">
              <span>Quantity</span>
              <div className="flex items-center justify-center my-3">
                <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
                  <FaMinus onClick={minusHandler} size={22} />
                </div>
                <div className="w-8 text-center">{itemQty}</div>
                <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
                  <FaPlus onClick={plusHandler} size={22} />
                </div>
              </div>
            </li>
            <li className="flex items-center justify-center gap-20">
              <span>Total Price</span>{" "}
              <span className="w-8 text-center">{totalPrice}</span>
            </li>
          </ul>
          {totalPrice > 0 ? (
            <button
              onClick={handleAddItem}
              className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer ml-auto"
            >
              Add Item
            </button>
          ) : (
            <button
              onClick={handleAddItem}
              disabled
              className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer ml-auto"
            >
              Add Item
            </button>
          )}
        </div>
      </PopUp>
    </div>
  );
};

export default FoodListItem;
