import React from "react";
import { MdClose } from "react-icons/md";
import type { AddItemPopUpProps } from "../utils/interface";

const AddItemPopUp: React.FC<AddItemPopUpProps> = ({
  isOpen,
  onClose,
  children,
}) => {
  if (!isOpen) return null;

  const handleBackdropClick = (e: React.MouseEvent<HTMLDivElement>) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  return (
    <div
      onClick={handleBackdropClick}
      className="fixed inset-0 bg-opacity-30 backdrop-blur-sm flex items-center justify-center z-50"
    >
      <div className="mx-1 flex flex-col gap-5">
        <button onClick={onClose}>
          <MdClose
            size={24}
            className="relative ml-auto top-2 right-2 cursor-pointer"
          />
        </button>
        {children}
      </div>
    </div>
  );
};

export default AddItemPopUp;
