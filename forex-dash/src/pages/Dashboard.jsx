import React from "react";
import TitleHead from "../components/TitleHead";
import Select from "../components/Select";
import { GRANULARITIES, PAIRS } from "../app/data";
import { useState } from "react";
import Button from "../components/Button";
import endPoints from "../app/api";
import Technicals from "../components/Technicals";
function Dashboard() {
  const [selectedPair, setSelectedPair] = useState(PAIRS[0].value);
  const [selectedGranularity, setSelectedGranularity] = useState(
    GRANULARITIES[0].value
  );
  const [technicalsData, setTechnicalsData] = useState(null);

  const loadTechnicals = async () => {
    const data = await endPoints.technicals(selectedPair, selectedGranularity);
    console.log(data);
    setTechnicalsData(data);
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
    </div>
  );
}

export default Dashboard;
