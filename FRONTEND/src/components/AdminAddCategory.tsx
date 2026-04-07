import React from "react";

const AdminAddCategory = () => {
  const [categoryName, setCategoryName] = React.useState("");

  const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!categoryName) {
      alert("Please enter a category name.");
      return;
    }
    console.log("New Category:", categoryName);
    setCategoryName("");
  };

  return (
    <div className="flex justify-center my-40 md:my-20">
      <form onSubmit={handleSubmit}>
        <div className="card card-border bg-[#1A1A1A] w-96">
          <div className="card-body">
            <h2 className="card-title text-3xl justify-center text-[#D4AF37]">
              Add Menu Category
            </h2>
            <div className="py-2">
              <label className="form-control w-full max-w-xs">
                <div className="label">
                  <span className="label-text text-[#F5F5F5]">
                    Category Name
                  </span>
                </div>
                <input
                  type="text"
                  className="input input-bordered w-full max-w-xs my-2"
                  name="categoryName"
                  value={categoryName}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setCategoryName(e.target.value)
                  }
                />
              </label>
            </div>
            <div className="card-actions">
              <button className="bg-[#D4AF37] hover:bg-[#E6C65C] w-[96%] text-lg p-2 cursor-pointer rounded-md">
                Add Category
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
};

export default AdminAddCategory;
