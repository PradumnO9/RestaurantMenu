import { useParams, Link } from "react-router-dom";
import { foodItems } from "../utils/constant";
import type { FoodItem } from "../utils/interface";

const ViewFoodItem = () => {
  //   interface FoodIdParams {
  //     foodItemId: string | undefined;
  //   }

  const { foodItemId } = useParams();

  if (!foodItemId) {
    return <div className="p-4">Invalid food item ID.</div>;
  }

  const foodItem: FoodItem | undefined = foodItems.find(
    (item) => item.id === foodItemId,
  );

  if (!foodItem) {
    return <div className="p-4">Food item not found.</div>;
  }

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <Link
        to="/restaurant/menu"
        className="text-[#D4AF37] hover:underline mb-4 inline-block"
      >
        ← Back to Menu
      </Link>
      <div className="bg-[#0F0F0F] rounded-box shadow-md p-6">
        <img
          src={foodItem.imgUrl}
          alt={foodItem.name}
          className="w-full h-64 object-cover rounded-box mb-4"
        />
        <h1 className="text-2xl font-bold mb-2">{foodItem.name}</h1>
        <p className="text-sm opacity-70 mb-2">{foodItem.categoryName}</p>
        <p className="mb-4">{foodItem.description}</p>
        <div className="mb-4">
          <strong>Price:</strong> {foodItem.price.join(", ")}
        </div>
        <div>
          <strong>Customizable:</strong> {foodItem.customizable ? "Yes" : "No"}
        </div>
      </div>
    </div>
  );
};

export default ViewFoodItem;
