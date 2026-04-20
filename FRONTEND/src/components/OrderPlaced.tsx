import { useAppSelector } from "../redux/hooks";

const OrderPlaced = () => {
  const orderPlacedData = useAppSelector((store) => store.orderPlaced);
  const grandTotal = () => {
    let total = 0;
    orderPlacedData.forEach((data) => {
      total += data.totalPrice;
    });
    return total;
  };

  const paymentHandler = () => {
    console.log("Payment Initiated...");
  };

  return orderPlacedData.length === 0 ? (
    <div className="p-4 my-10 flex justify-center">
      <p className="text-red-500 text-xl">Please order something!</p>
    </div>
  ) : (
    <div className="p-4 my-5 flex flex-col items-center justify-center">
      <ul className="list bg-[#1A1A1A] w-full md:w-[70%] rounded-box shadow-md">
        {orderPlacedData.length > 0 &&
          orderPlacedData.map((item) => {
            return (
              <ul key={item.orderPlacedId} className="list">
                {item.cart.length > 0 &&
                  item.cart.map((foodData) => {
                    return (
                      <li className="list-row" key={foodData.cartItemId}>
                        <div>
                          <img
                            className="size-22 rounded-box max-w-xs md:max-w-md"
                            src={
                              foodData.foodImg ? foodData.foodImg : undefined
                            }
                          />
                        </div>
                        <div className=" max-w-xs md:max-w-md">
                          <div>
                            {foodData.foodName}
                            {" ("}
                            {foodData.foodPriceCategory} {": "}₹
                            {foodData.foodPrice / foodData.foodQty}
                            {")"}
                          </div>
                          <p className="list-col-wrap text-xs opacity-90">
                            {foodData.foodDescription}
                          </p>
                        </div>
                        <div className="flex flex-col max-w-xs md:max-w-md gap-2">
                          <div>
                            <span>Quantity</span>
                            {": "}
                            <span>{foodData.foodQty}</span>
                          </div>
                          <div>
                            <span>Price</span>
                            {": "}
                            <span>{foodData.foodPrice}</span>
                          </div>
                        </div>
                      </li>
                    );
                  })}
                <li className="list-row bg-base-100 p-4 flex justify-between">
                  <span>
                    Order Time {": "}
                    {item.orderPlacedDateAndTime}
                  </span>
                  <span>
                    Total {": "}
                    {item.totalPrice}
                  </span>
                </li>
              </ul>
            );
          })}
      </ul>
      <div className="flex justify-between items-center w-full md:w-[70%] my-2">
        <p className="text-[#D4AF37] text-2xl mb-2">
          Grand Total {": "} {grandTotal()}
        </p>
        <button
          onClick={paymentHandler}
          className="bg-[#D4AF37] hover:bg-[#E6C65C] px-2 py-1 rounded-md cursor-pointer"
        >
          Pay Now
        </button>
      </div>
    </div>
  );
};

export default OrderPlaced;
