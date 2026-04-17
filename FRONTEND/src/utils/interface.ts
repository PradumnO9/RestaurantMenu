export interface AdminData {
    email: string,
    password: string,
    isLoggedIn: boolean,
    type: string
}

export interface AdminState {
    type: string,
    isLoggedIn: boolean,
    token: string
}

export interface AddItemPopUpProps {
    isOpen: boolean,
    onClose: () => void,
    children: React.ReactNode
}

export interface FoodCategory {
    id: string,
    categoryName: string
}

export interface FoodItem {
    id: string,
    name: string,
    description: string,
    categoryName: string,
    imgUrl: string,
    customizable: boolean,
    price: { [key: string]: number }
}

export interface EditFoodItem {
    id: string,
    newName: string,
    newDescription: string,
    newCategoryName: string,
    newImgUrl: string,
    newCustomizable: boolean,
    newPrice: { [key: string]: number }
}

export interface MenuState {
    menuItems: FoodItem[],
    categories: FoodCategory[]
}

export interface CartState {
    cartItemId: string,
    foodId: string,
    foodName: string,
    foodDescription: string,
    foodImg: string,
    foodQty: number,
    foodPrice: number,
    foodPriceCategory: string
}