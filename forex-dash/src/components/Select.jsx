import React from "react";

function Select({ options, title, name }) {
  return (
    <div>
      <label htmlFor={name}>{title}</label>
      <select className="select" name={name} id={name}>
        {options.map((item) => {
          return (
            <option key={item.key} value={item.value}>
              {item.text}
            </option>
          );
        })}
      </select>
    </div>
  );
}

export default Select;
