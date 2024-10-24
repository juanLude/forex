/* eslint-disable react-hooks/exhaustive-deps */
import React from "react";
import Select from "./Select";
import { COUNTS } from "../app/data";
import { useEffect } from "react";
import { drawChart } from "../app/chart";

function PriceChart({
  priceData,
  selectedPair,
  selectedGranularity,
  selectedCount,
  handleCountChange,
}) {
  useEffect(() => {
    if (priceData) {
      drawChart(priceData, selectedPair, selectedGranularity, "chartDiv");
    }
  }, [priceData]);

  return (
    <div className="segment" id="price-chart-holder">
      <Select
        name="numrows"
        title="Num. Rows"
        options={COUNTS}
        defaultValue={selectedCount}
        onSelected={handleCountChange}
      />
      <div id="chartDiv"></div>
    </div>
  );
}

export default PriceChart;
