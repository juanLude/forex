import React from "react";

function Progress({ title, percentage, colour }) {
  const style = { width: `${percentage}`, backgroundColor: colour };
  return (
    <div className="progress-wrap">
      <div className="progress-holder progress">
        <div className="progress" style={style} />
      </div>
      <div className="progress-text" style={{ color: colour }}>
        {title}
      </div>
    </div>
  );
}

export default Progress;
