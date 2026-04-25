import { useParams, Link } from "react-router-dom";
import type { EditFoodItem, FoodItem } from "../utils/interface";
import { useAppSelector } from "../redux/hooks";
import { useState } from "react";
import { FaEdit } from "react-icons/fa";
import { MdClose } from "react-icons/md";
import PopUp from "./ui-utils/PopUp";
import UnAuthorized from "./UnAuthorized";

const ViewFoodItem = () => {
  const { foodItemId } = useParams();

  const foodItems = useAppSelector((store) => store.menu.menuItems);
  const foodCategory = useAppSelector((store) => store.menu.categories);
  const { isLoggedIn, type } = useAppSelector((store) => store.admin);

  const foodItem: FoodItem | undefined = foodItems.find(
    (item) => item.id === foodItemId,
  );

  const [editDishData, setEditDishData] = useState<EditFoodItem>({
    id: foodItemId || "",
    newName: foodItem?.name || "",
    newDescription: foodItem?.description || "",
    newCategoryName: foodItem?.categoryName || "",
    newImgUrl: foodItem?.imgUrl || "",
    newCustomizable: foodItem?.customizable || false,
    newPrice: foodItem?.price || {},
  });

  const [showNameInput, setShowNameInput] = useState(false);
  const [showDescriptionInput, setShowDescriptionInput] = useState(false);
  const [showCategoryInput, setShowCategoryInput] = useState(false);
  const [showImgUrlInput, setShowImgUrlInput] = useState(false);
  const [showCustomizableInput, setShowCustomizableInput] = useState(false);
  const [showPriceInput, setShowPriceInput] = useState(false);

  const [selectImageFile, setSelectImageFile] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string>("");
  const [pricePreview, setPricePreview] = useState<{ [key: string]: number }>(
    {},
  );
  const [isPopUpOpen, setIsPopUpOpen] = useState(false);

  const openPopUp = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    setIsPopUpOpen(true);
  };
  const closePopUp = () => setIsPopUpOpen(false);

  if (!foodItemId) {
    return <div className="p-4">Invalid food item ID.</div>;
  }

  if (!foodItem) {
    return <div className="p-4">Food item not found.</div>;
  }

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] || null;
    if (!e.target.files || e.target.files.length === 0) {
      setSelectImageFile(null);
      setImagePreview("");
      return;
    }
    setSelectImageFile(file);
    if (file) {
      setEditDishData({
        ...editDishData,
        newImgUrl: URL.createObjectURL(file),
      });
    }
    setImagePreview(URL.createObjectURL(e.target.files[0]));

    return () => {
      URL.revokeObjectURL(imagePreview);
    };
  };

  const handleAddPrice = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    setEditDishData({
      ...editDishData,
      newPrice: { ...editDishData.newPrice, ...pricePreview },
    });
    setPricePreview({});
  };

  const handleRemovePrice = (
    e: React.MouseEvent<HTMLButtonElement>,
    index: number,
  ) => {
    e.preventDefault();
    const updatedPrices = { ...editDishData.newPrice };
    const keyToRemove = Object.keys(editDishData.newPrice)[index];
    delete updatedPrices[keyToRemove];
    setEditDishData({ ...editDishData, newPrice: updatedPrices });
  };

  const handleUpdateDish = (e: React.MouseEvent<HTMLButtonElement>) => {
    // Here you would typically send the updated dish data to your backend API
    e.preventDefault();
    console.log("Updated Dish Data:", editDishData);
  };

  return type === "admin" && isLoggedIn ? (
    <div className="p-4 max-w-2xl mx-auto flex flex-col items-center">
      <Link
        to="/restaurant/menu"
        className="text-[#D4AF37] hover:underline mb-4 inline-block -ml-66.25"
      >
        ← Back to Menu
      </Link>
      <div className="card bg-[#0F0F0F] w-96 shadow-md">
        <form>
          <div>
            <figure>
              <FaEdit
                size={24}
                color="#D4AF37"
                className="absolute top-2 right-2 cursor-pointer hover:text-[#C0A020]"
                onClick={() => setShowImgUrlInput(!showImgUrlInput)}
              />
              {!imagePreview && (
                <img
                  src={foodItem.imgUrl ? foodItem.imgUrl : undefined}
                  alt={foodItem.name}
                  className="w-full h-64 object-cover rounded-box mb-4"
                />
              )}
            </figure>
            <div>
              {selectImageFile && (
                <img
                  src={imagePreview ? imagePreview : undefined}
                  alt="Selected"
                  className="w-full h-64 object-cover rounded-box mb-4"
                />
              )}
              {showImgUrlInput && (
                <input
                  type="file"
                  className="file-input w-full max-w-xs my-2 cursor-pointer"
                  onChange={handleImageChange}
                />
              )}
            </div>
          </div>
          <div className="card-body">
            <div>
              <div className="flex items-center">
                <h2 className="card-title">{foodItem.name}</h2>
                <FaEdit
                  size={13}
                  color="#D4AF37"
                  className="ml-1 -mt-2 cursor-pointer hover:text-[#C0A020]"
                  onClick={() => setShowNameInput(!showNameInput)}
                />
              </div>
              {showNameInput && (
                <input
                  type="text"
                  value={editDishData.newName}
                  placeholder="Enter new name"
                  onChange={(e) =>
                    setEditDishData({
                      ...editDishData,
                      newName: e.target.value,
                    })
                  }
                  className="input input-bordered max-w-xs mt-1"
                />
              )}
            </div>
            <div>
              <div className="flex items-center">
                <h2 className="card-subtitle">
                  <strong>Category:</strong> {foodItem.categoryName}
                </h2>
                <FaEdit
                  size={13}
                  color="#D4AF37"
                  className="ml-1 -mt-2 cursor-pointer hover:text-[#C0A020]"
                  onClick={() => {
                    setShowCategoryInput(!showCategoryInput);
                  }}
                />
              </div>
              {showCategoryInput && (
                <select
                  value={editDishData.newCategoryName}
                  onChange={(e: React.ChangeEvent<HTMLSelectElement>) => {
                    setEditDishData({
                      ...editDishData,
                      newCategoryName: e.target.value,
                    });
                  }}
                  className="select mt-2 w-full max-w-xs"
                >
                  <option disabled={true}>Choose dish category</option>
                  {foodCategory.map((category) => (
                    <option key={category.id}>{category.categoryName}</option>
                  ))}
                </select>
              )}
            </div>
            <div>
              <div className="flex">
                <h2 className="max-w-[93%]">{foodItem.description}</h2>
                <FaEdit
                  size={13}
                  color="#D4AF37"
                  className="ml-1 -mt-2 cursor-pointer hover:text-[#C0A020]"
                  onClick={() => {
                    setShowDescriptionInput(!showDescriptionInput);
                  }}
                />
              </div>
              {showDescriptionInput && (
                <textarea
                  value={editDishData.newDescription}
                  placeholder="Enter new description"
                  onChange={(e) =>
                    setEditDishData({
                      ...editDishData,
                      newDescription: e.target.value,
                    })
                  }
                  className="textarea textarea-bordered w-full max-w-xs mt-1"
                />
              )}
            </div>
            <div>
              <p className="flex">
                <strong>Price:</strong>
                <FaEdit
                  size={13}
                  color="#D4AF37"
                  className="ml-1 -mt-1 cursor-pointer hover:text-[#C0A020]"
                  onClick={() => {
                    setShowPriceInput(!showPriceInput);
                  }}
                />
              </p>
              {Object.entries(editDishData.newPrice || {}).map(
                ([size, value]) => (
                  <span key={size} className="mr-2">
                    {size.charAt(0).toUpperCase() + size.slice(1)}: ₹{value}{" "}
                    <br />
                  </span>
                ),
              )}
              {showPriceInput && (
                <div>
                  <div className="grid grid-cols-4 w-[96%] mt-1">
                    <div className="grid grid-cols-6 col-span-3">
                      <input
                        type="text"
                        className="input input-bordered w-full max-w-xs col-span-3 price-input"
                        name="pricePreview"
                        value={Object.keys(pricePreview)[0] || ""}
                        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                          setPricePreview({
                            [e.target.value.toLowerCase()]:
                              Object.values(pricePreview)[0] || 0,
                          })
                        }
                        placeholder="eg. full"
                      />
                      <input
                        type="text"
                        className="input input-bordered w-full max-w-xs col-span-3 price-input-noradius"
                        name="pricePreview"
                        value={Object.values(pricePreview)[0] || ""}
                        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                          setPricePreview({
                            [Object.keys(pricePreview)[0] || ""]: Number(
                              e.target.value,
                            ),
                          })
                        }
                        placeholder="eg. 250"
                      />
                    </div>
                    <button
                      onClick={handleAddPrice}
                      className="bg-[#D4AF37] hover:bg-[#E6C65C] cursor-pointer rounded-r-md col-span-1"
                    >
                      Add Price
                    </button>
                  </div>
                  <ul>
                    {editDishData.newPrice &&
                      Object.entries(editDishData.newPrice).map(
                        ([key, value], index) => (
                          <li
                            key={index}
                            className="text-[#F5F5F5] p-2 rounded-md bg-base-100 grid grid-cols-4 w-[96%] my-2"
                          >
                            <span className="col-span-3">
                              {key.charAt(0).toUpperCase() + key.slice(1)}: ₹
                              {value}
                            </span>
                            <button
                              className="ml-auto mr-2 cursor-pointer"
                              onClick={(
                                e: React.MouseEvent<HTMLButtonElement>,
                              ) => handleRemovePrice(e, index)}
                            >
                              <MdClose size={23} color="#D4AF37" />
                            </button>
                          </li>
                        ),
                      )}
                  </ul>
                </div>
              )}
            </div>
            <div className="flex items-center">
              <p className="flex">
                <strong>Customizable:</strong>{" "}
                {foodItem.customizable ? "Yes" : "No"}
                <FaEdit
                  size={13}
                  color="#D4AF37"
                  className="ml-1 -mt-2 cursor-pointer hover:text-[#C0A020]"
                  onClick={() => {
                    setShowCustomizableInput(!showCustomizableInput);
                  }}
                />
              </p>
              {showCustomizableInput && (
                <input
                  type="checkbox"
                  className="checkbox my-custom-checkbox col-span-1 ml-auto"
                  checked={editDishData.newCustomizable}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setEditDishData({
                      ...editDishData,
                      newCustomizable: e.target.checked,
                    })
                  }
                />
              )}
            </div>
            <div className="flex justify-between">
              <div className="card-actions">
                <button
                  onClick={handleUpdateDish}
                  className="btn bg-[#D4AF37] hover:bg-[#C0A020]"
                >
                  Update Dish
                </button>
              </div>
              <div className="card-actions">
                <button
                  onClick={openPopUp}
                  className="btn bg-[#D4AF37] hover:bg-[#C0A020]"
                >
                  Delete Dish
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
      <PopUp isOpen={isPopUpOpen} onClose={closePopUp}>
        <div className="bg-[#1A1A1A] rouned-xl px-20 py-10 flex flex-col gap-5 items-center mx-3">
          <h2 className="text-lg">
            Are you sure you want to delete {foodItem.name} ?
          </h2>
          <div className="flex gap-10">
            <button className="bg-[#D4AF37] hover:bg-[#C0A020] px-4 py-1 rounded-md cursor-pointer ml-auto">
              Yes, Delete
            </button>
            <button
              onClick={closePopUp}
              className="bg-[#D4AF37] hover:bg-[#C0A020] px-4 py-1 rounded-md cursor-pointer ml-auto"
            >
              No
            </button>
          </div>
        </div>
      </PopUp>
    </div>
  ) : (
    <UnAuthorized />
  );
};

export default ViewFoodItem;
