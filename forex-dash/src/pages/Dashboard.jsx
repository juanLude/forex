import React from "react";
import TitleHead from "../components/TitleHead";
import Select from "../components/Select";
import { PAIRS } from "../app/data";

function Dashboard() {
  return (
    <div>
      <TitleHead title="Options" />
      <div className="segment options">
        <Select name="Currency" title="Select Currency" options={PAIRS} />
      </div>
    </div>
  );
}

export default Dashboard;
