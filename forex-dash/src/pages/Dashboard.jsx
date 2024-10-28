import React, { useEffect } from "react";
import TitleHead from "../components/TitleHead";
import Select from "../components/Select";
import { COUNTS, GRANULARITIES, PAIRS } from "../app/data";
import { useState } from "react";
import Button from "../components/Button";
import endPoints from "../app/api";
import Technicals from "../components/Technicals";
import PriceChart from "../components/PriceChart";
function Dashboard() {
  const [selectedPair, setSelectedPair] = useState(null);
  const [selectedGranularity, setSelectedGranularity] = useState(null);
  const [technicalsData, setTechnicalsData] = useState(null);
  const [priceData, setPriceData] = useState(null);
  const [selectedCount, setSelectedCount] = useState(COUNTS[0].value);
  const [options, setIsOptions] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadOptions();
  }, []);
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
  const loadOptions = async () => {
    const data = await endPoints.options();
    console.log("from Dashboard", data);
    setIsOptions(data[0]);
    setSelectedGranularity(data[0].granularity);
    setSelectedPair(data[0].name);
    setLoading(false);
  };
  const loadTechnicals = async () => {
    const data = await endPoints.technicals(selectedPair, selectedGranularity);
    console.log(data[0]);
    setTechnicalsData(data[0]);
    loadPrices(selectedCount);
  };

  if (loading) {
    return <h1>Loading...</h1>;
  }
  return (
    <div>
      <TitleHead title="Options" />
      <div className="segment options">
        <Select
          name="Currency"
          title="Select Currency"
          options={options.pairs}
          defaultValue={selectedPair}
          onSelected={setSelectedPair}
        />
        <Select
          name="Granularity"
          title="Select Granularity"
          options={options.granularities}
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
