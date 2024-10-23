import React from "react";
import Progress from "./Progress";

const HEADERS = ["R1", "R2", "R3", "S1", "S2", "S3", "pivot"];
function Technicals({ data }) {
  console.log(data[0].percent_bearish);
  return (
    <div className="segment">
      <Progress
        title="Bullish"
        colour="#21ba45"
        percentage={data[0].percent_bullish}
      />
      <Progress
        title="Bearish"
        colour="#db2828"
        percentage={data[0].percent_bearish}
      />
      <table>
        <thead>
          <tr>
            {HEADERS.map((item) => (
              <th key={item}>{item}</th>
            ))}
          </tr>
          <tr>
            {HEADERS.map((item) => (
              <td key={item}>{data[0][item]}</td>
            ))}
          </tr>
        </thead>
      </table>
    </div>
  );
}

export default Technicals;
