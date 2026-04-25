import React, { useState } from "react";
interface IPROPS {
  text: string;
}

const ReadMore: React.FC<IPROPS> = ({ text }) => {
  const textData = text;
  const [isReadMore, setIsReadMore] = useState<boolean>(true);

  return (
    <p>
      {isReadMore ? textData.slice(0, 100) : text}
      <span
        className="cursor-pointer text-[#E6C65C]"
        onClick={() => {
          setIsReadMore(!isReadMore);
        }}
      >
        {isReadMore ? "...read more" : "...read less"}
      </span>
    </p>
  );
};

export default ReadMore;
