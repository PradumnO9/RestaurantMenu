import { FaMinus, FaPlus } from "react-icons/fa6";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { removeToCart } from "../redux/cartSlice";

const Cart = () => {
  const dispatch = useAppDispatch();
  const cartData = useAppSelector((store) => store.cart);

  const plusHandler = () => {};
  const minusHandler = () => {};

  const removeCartItem = (cartItemId: string) => {
    console.log("I am here...");
    dispatch(removeToCart(cartItemId));
  };

  if (cartData.length === 0) {
    return (
      <div className="p-4 my-10 flex justify-center">
        <p className="text-red-500 text-xl">
          Your Cart is empty, please add food items
        </p>
      </div>
    );
  }

  return (
    <div className="p-4 my-5 flex flex-col items-center justify-center">
      <p className="text-[#D4AF37] text-2xl mb-2">Your Cart</p>
      <ul className="list bg-[#1A1A1A] w-full md:w-[70%] rounded-box shadow-md">
        {cartData.length > 0 &&
          cartData.map((item) => {
            return (
              <li key={item.cartItemId} className="list-row">
                <div>
                  <img
                    className="size-22 rounded-box max-w-xs md:max-w-md"
                    src={item.foodImg}
                  />
                </div>
                <div className=" max-w-xs md:max-w-md">
                  <div>
                    {item.foodName}
                    {" ("}
                    {item.foodPriceCategory}
                    {")"}
                  </div>
                  <p className="list-col-wrap text-xs opacity-90">
                    {item.foodDescription}
                  </p>
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
                        <FaMinus onClick={minusHandler} size={22} />
                      </div>
                      <div className="w-8 text-center">{item.foodQty}</div>
                      <div className="bg-[#D4AF37] rounded-full p-0.5 cursor-pointer">
                        <FaPlus onClick={plusHandler} size={22} />
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
    </div>
  );
};

export default Cart;
