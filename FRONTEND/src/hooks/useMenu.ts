import { useEffect, useCallback } from "react";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { addMenuItems } from "../redux/menuSlice";
import { foodItems, foodCategory } from "../utils/constant";

const useMenu = () => {
    const dispatch = useAppDispatch();
    const menuItems = useAppSelector((store) => store.menu.menuItems);
    const categories = useAppSelector((store) => store.menu.categories);

    const getMenu = useCallback(() => {
        dispatch(addMenuItems({menuItems: foodItems, categories: foodCategory}));
    }, [dispatch]);

    useEffect(() => {
        if (!menuItems.length && !categories.length) {
            getMenu();
        }
    }, [getMenu, menuItems, categories]);
}

export default useMenu;