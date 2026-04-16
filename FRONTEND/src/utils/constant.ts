import type { FoodCategory, FoodItem } from "./interface"

export const foodCategory : FoodCategory[] = [
    {
      "id": "1",
      "categoryName": "Pizza"
    },
    {
      "id": "2",
      "categoryName": "Starter"
    },
    {
      "id": "3",
      "categoryName": "Fast Food"
    },
  ]

export const foodItems: FoodItem[] = [
    {
      "id": "101",
      "name": "Burger",
      "description": "Veg Burger, A burger is a popular sandwich consisting of a cooked patty—typically ground beef, but also chicken, veggie, or paneer—served inside a sliced bun. Often topped with cheese, lettuce, tomato, onion, pickles, and sauces like mayo or ketchup, they are staples of fast food and home cooking. Popular types include cheeseburgers and smash burgers",
      "categoryName": "Fast Food",
      "imgUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1IvOEs9XPj4AaKqnTnI5698CueUIQ600TRA&s",
      "price": {"full": 100},
      "customizable": false
    },
    {
      "id": "102",
      "name": "Pizza",
      "description": "A vegetarian pizza is a pizza that omits all animal meat—including chicken, pork, beef, and fish—substituting it with vegetables, cheeses, and sauces. It typically features a pizza dough base, tomato sauce, mozzarella or other cheeses, and toppings like mushrooms, peppers, onions, olives, and spinach",
      "categoryName": "Pizza",
      "imgUrl": "https://cdn.loveandlemons.com/wp-content/uploads/2023/02/vegetarian-pizza.jpg",
      "price": {"small": 150, "medium": 200, "large": 250},
      "customizable": true
    },
    {
      "id": "103",
      "name": "Honey Chilli Potato",
      "description": "A dish with potato, chilli and honey",
      "categoryName": "Starter",
      "imgUrl": "https://myfoodstory.com/wp-content/uploads/2018/10/Honey-Chilli-Potatoes-1.jpg",
      "price": {"half": 70, "full": 100},
      "customizable": true
    },
    {
      "id": "104",
      "name": "Classic Cheese Pizza",
      "description": "Loaded with cheese",
      "categoryName": "Pizza",
      "imgUrl": "https://www.foodandwine.com/thmb/Wd4lBRZz3X_8qBr69UOu2m7I2iw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-cheese-pizza-FT-RECIPE0422-31a2c938fc2546c9a07b7011658cfd05.jpg",
      "price": {"small": 150, "medium": 200, "large": 250},
      "customizable": true
    },
    {
      "id": "105",
      "name": "French Fries",
      "description": "Crispy potato dish",
      "categoryName": "Fast Food",
      "imgUrl": "https://www.recipetineats.com/wp-content/uploads/2022/09/Fries-with-rosemary-salt_1.jpg",
      "price": {"half": 70, "full": 100},
      "customizable": true
    }
  ]