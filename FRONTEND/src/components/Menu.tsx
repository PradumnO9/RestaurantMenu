import type React from "react";
import type { FoodCategory, FoodItem } from "../utils/interface";
import FoodListItem from "./FoodListItem";
import { useAppSelector } from "../redux/hooks";

const Menu: React.FC = () => {
  const foodItems = useAppSelector((store) => store.menu.menuItems);
  const foodCategory = useAppSelector((store) => store.menu.categories);
  const { isLoggedIn } = useAppSelector((store) => store.admin);

  if (foodItems.length === 0 || foodCategory.length === 0) {
    return (
      <div className="p-4 my-10 flex justify-center">
        <p className="text-red-500 text-xl">No Item Available</p>
      </div>
    );
  }

  return isLoggedIn ? (
    <div className="p-4 my-10 flex justify-center">
      <div className="join join-vertical bg-[#1A1A1A] w-full md:w-[70%] p-2 rounded-md">
        {foodCategory.length > 0 &&
          foodCategory.map((category: FoodCategory, index: number) => {
            return (
              <div
                key={category.id}
                className="collapse collapse-arrow join-item border-[#1A1A1A] border"
              >
                <input
                  type="radio"
                  name="my-accordion-4"
                  defaultChecked={index === 0}
                />
                <div className="collapse-title font-semibold">
                  {category.categoryName} {"("}
                  {
                    foodItems.filter(
                      (item: FoodItem) =>
                        item.categoryName === category.categoryName,
                    ).length
                  }
                  {")"}
                </div>
                <div className="collapse-content text-sm">
                  {foodItems.length > 0 &&
                    foodItems
                      .filter(
                        (item: FoodItem) =>
                          item.categoryName === category.categoryName,
                      )
                      .map((filteredItem: FoodItem) => {
                        return (
                          <div key={filteredItem.id}>
                            <FoodListItem itemData={filteredItem} />
                          </div>
                        );
                      })}
                </div>
              </div>
            );
          })}
      </div>
    </div>
  ) : (
    <div className="p-4 my-10 flex justify-center">
      <p className="text-red-500 text-xl">Please log in First...</p>
    </div>
  );
};

export default Menu;
