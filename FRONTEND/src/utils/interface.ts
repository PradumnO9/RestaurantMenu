export interface AdminData {
    email: string,
    password: string
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
    price: string[]
}