import React, { useEffect, useState } from "react";
import TitleHead from "./TitleHead";
import endPoints from "../app/api";
import Headline from "./Headline";
function Headlines() {
  const [headlines, setHeadlines] = useState(null);

  useEffect(() => {
    loadHeadlines();

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const loadHeadlines = async () => {
    const data = await endPoints.headlines();

    setHeadlines(data);
  };
  console.log(headlines);
  return (
    <div>
      <TitleHead title="Headlines" />
      <div className="segment">
        {headlines &&
          headlines[0].map((item, index) => {
            return <Headline data={item} key={index} />;
          })}
      </div>
    </div>
  );
}

export default Headlines;
