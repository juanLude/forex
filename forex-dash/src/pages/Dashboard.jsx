import React from "react";
import TitleHead from "../components/TitleHead";
import Select from "../components/Select";
import { COUNTS, GRANULARITIES, PAIRS } from "../app/data";
import { useState } from "react";
import Button from "../components/Button";
import endPoints from "../app/api";
import Technicals from "../components/Technicals";
import PriceChart from "../components/PriceChart";
function Dashboard() {
  const [selectedPair, setSelectedPair] = useState(PAIRS[0].value);
  const [selectedGranularity, setSelectedGranularity] = useState(
    GRANULARITIES[0].value
  );
  const [technicalsData, setTechnicalsData] = useState(null);
  const [priceData, setPriceData] = useState(null);
  const [selectedCount, setSelectedCount] = useState(COUNTS[0].value);

  const handleCountChange = (count) => {
    setSelectedCount(count);
    loadPrices(count);
  };

  const loadPrices = async (count) => {
    const data = await endPoints.prices(
      selectedPair,
      selectedGranularity,
      count
    );
    console.log("from loadPrices", data);
    setPriceData(data[0]);
  };

  const loadTechnicals = async () => {
    const data = await endPoints.technicals(selectedPair, selectedGranularity);
    console.log(data[0]);
    setTechnicalsData(data[0]);
    loadPrices(selectedCount);
  };
  return (
    <div>
      <TitleHead title="Options" />
      <div className="segment options">
        <Select
          name="Currency"
          title="Select Currency"
          options={PAIRS}
          defaultValue={selectedPair}
          onSelected={setSelectedPair}
        />
        <Select
          name="Granularity"
          title="Select Granularity"
          options={GRANULARITIES}
          defaultValue={selectedGranularity}
          onSelected={setSelectedGranularity}
        />
        <Button text="Load" handleClick={() => loadTechnicals()} />
      </div>
      <TitleHead title="Technicals" />
      {technicalsData && <Technicals data={technicalsData} />}

      <TitleHead title="Price Chart" />
      {priceData && (
        <PriceChart
          selectedCount={selectedCount}
          selectedPair={selectedPair}
          selectedGranularity={selectedGranularity}
          handleCountChange={handleCountChange}
          priceData={priceData}
        />
      )}
    </div>
  );
}

export default Dashboard;
