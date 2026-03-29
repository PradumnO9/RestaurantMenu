import type React from "react";
import { foodCategory, foodItems } from "../utils/constant";
import type { FoodCategory, FoodItem } from "../utils/interface";
import FoodListItem from "./FoodListItem";

const Menu: React.FC = () => {
  return (
    <div className="p-4 my-10 flex justify-center">
      <div className="join join-vertical bg-[#1A1A1A] w-full md:w-[70%] p-2 rounded-md">
        {foodCategory.length > 0 &&
          foodCategory.map((category: FoodCategory) => {
            return (
              <div
                key={category.id}
                className="collapse collapse-arrow join-item border-[#1A1A1A] border"
              >
                <input type="radio" name="my-accordion-4" defaultChecked />
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
  );
};

export default Menu;
