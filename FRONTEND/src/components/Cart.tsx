import { FaMinus, FaPlus } from "react-icons/fa6";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import {
  decreseQty,
  deleteCart,
  increseQty,
  removeToCart,
} from "../redux/cartSlice";
import { useState } from "react";
import PopUp from "./ui-utils/PopUp";
import type { CartState } from "../utils/interface";
import { useNavigate } from "react-router-dom";
import { addToOrderList } from "../redux/orderPlacedSlice";
import UnAuthorized from "./UnAuthorized";
import ReadMore from "./ui-utils/ReadMore";

const Cart = () => {
  const [isDeleteCartPopUp, setIsDeleteCartPopUp] = useState<boolean>(false);
  const [isPlaceOrderPopUp, setIsPlaceOrderPopUp] = useState<boolean>(false);
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const cartData = useAppSelector((store) => store.cart);
  const { isLoggedIn, type } = useAppSelector((store) => store.admin);

  const openDeleteCartPopUp = () => setIsDeleteCartPopUp(true);
  const closeDeleteCartPopUp = () => setIsDeleteCartPopUp(false);
  const openPlaceOrderPopUp = () => setIsPlaceOrderPopUp(true);
  const closePlaceOrderPopUp = () => setIsPlaceOrderPopUp(false);

  const removeCartItem = (cartItemId: string) => {
    dispatch(removeToCart(cartItemId));
  };

  const handlePlaceOrder = (cartData: CartState[], totalOrderPrice: number) => {
    const date = new Date();
    const currentDateAndTime = date.toLocaleString();
    dispatch(
      addToOrderList({
        cart: cartData,
        orderPlacedId: crypto.randomUUID(),
        orderPlacedDateAndTime: currentDateAndTime,
        totalPrice: totalOrderPrice,
      }),
    );
    dispatch(deleteCart());
    navigate("/restaurant/order-placed");
  };

  const totalOrderPrice = () => {
    let totalPrice: number = 0;
    cartData.forEach((item) => {
      totalPrice += item.foodPrice;
    });
    return totalPrice;
  };

  return type === "user" && isLoggedIn ? (
    cartData.length === 0 ? (
      <div className="p-4 my-10 flex justify-center">
        <p className="text-[#D4AF37] text-xl">
          Your Cart is empty, please add food items
        </p>
      </div>
    ) : (
      <div className="p-4 my-5 flex flex-col items-center justify-center">
        <div className="flex justify-between items-center w-full md:w-[70%] my-2">
          <p className="text-[#D4AF37] text-2xl mb-2">Your Cart</p>
          <button
            onClick={openDeleteCartPopUp}
            className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
          >
            Empty Cart
          </button>
        </div>
        <ul className="list bg-[#1A1A1A] w-full md:w-[70%] rounded-box shadow-md">
          {cartData.length > 0 &&
            cartData.map((item) => {
              return (
                <li key={item.cartItemId} className="list-row">
                  <div>
                    <img
                      className="size-22 rounded-box max-w-xs md:max-w-md"
                      src={item.foodImg ? item.foodImg : undefined}
                    />
                  </div>
                  <div className=" max-w-xs md:max-w-md">
                    <div>
                      {item.foodName}
                      {" ("}
                      {item.foodPriceCategory}
                      {": "}₹{item.foodPrice / item.foodQty}
                      {")"}
                    </div>
                    {item.foodDescription.length > 100 ? (
                      <div className="list-col-wrap text-xs opacity-90">
                        <ReadMore text={item.foodDescription} />
                      </div>
                    ) : (
                      <div className="list-col-wrap text-xs opacity-90">
                        {item.foodDescription}
                      </div>
                    )}
                  </div>
                  <div className="flex flex-col max-w-xs md:max-w-md gap-2">
                    <button
                      onClick={() => removeCartItem(item.cartItemId)}
                      className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
                    >
                      Delete
                    </button>
                    <div>
                      <div className="flex items-center justify-center my-3">
                        <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
                          <FaMinus
                            onClick={() =>
                              dispatch(decreseQty(item.cartItemId))
                            }
                            size={22}
                          />
                        </div>
                        <div className="w-8 text-center">{item.foodQty}</div>
                        <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
                          <FaPlus
                            onClick={() =>
                              dispatch(increseQty(item.cartItemId))
                            }
                            size={22}
                          />
                        </div>
                      </div>
                    </div>
                    <div>
                      <span>Price</span>
                      {": "}
                      <span>{item.foodPrice}</span>
                    </div>
                  </div>
                </li>
              );
            })}
        </ul>
        <div className="flex justify-between items-center w-full md:w-[70%] my-2">
          <p className="text-[#D4AF37] text-2xl mb-2">
            Total{": "} ₹{totalOrderPrice()}
          </p>
          <button
            onClick={openPlaceOrderPopUp}
            className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
          >
            Place Order
          </button>
        </div>
        <PopUp isOpen={isDeleteCartPopUp} onClose={closeDeleteCartPopUp}>
          <div className="bg-[#1A1A1A] rouned-xl px-20 py-10 flex flex-col gap-5 items-center mx-3">
            <h2 className="text-lg">
              Are you sure you want to empty the cart ?
            </h2>
            <div className="flex gap-10">
              <button
                onClick={() => {
                  dispatch(deleteCart());
                }}
                className="bg-[#D4AF37] hover:bg-[#C0A020] px-4 py-1 rounded-md cursor-pointer ml-auto"
              >
                Yes, Empty
              </button>
              <button
                onClick={closeDeleteCartPopUp}
                className="bg-[#D4AF37] hover:bg-[#C0A020] px-4 py-1 rounded-md cursor-pointer ml-auto"
              >
                No
              </button>
            </div>
          </div>
        </PopUp>
        <PopUp isOpen={isPlaceOrderPopUp} onClose={closePlaceOrderPopUp}>
          <div className="bg-[#1A1A1A] rouned-xl px-20 py-10 flex flex-col gap-5 items-center mx-3">
            <h2 className="text-lg">
              Are you sure you want to place ₹{totalOrderPrice()} order ?
            </h2>
            <div className="flex gap-10">
              <button
                onClick={() => handlePlaceOrder(cartData, totalOrderPrice())}
                className="bg-[#D4AF37] hover:bg-[#C0A020] px-4 py-1 rounded-md cursor-pointer ml-auto"
              >
                Yes, Place
              </button>
              <button
                onClick={closePlaceOrderPopUp}
                className="bg-[#D4AF37] hover:bg-[#C0A020] px-4 py-1 rounded-md cursor-pointer ml-auto"
              >
                No
              </button>
            </div>
          </div>
        </PopUp>
      </div>
    )
  ) : (
    <UnAuthorized />
  );
};

export default Cart;
