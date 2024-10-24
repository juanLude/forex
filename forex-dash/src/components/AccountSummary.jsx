import React, { useState, useEffect } from "react";
import TitleHead from "./TitleHead";
import endPoints from "../app/api";

const DATA_KEYS = [
  { name: "Account Number", key: "id", fixed: -1 },
  { name: "Balance", key: "balance", fixed: -1 },
  { name: "NAV", key: "NAV", fixed: -1 },
  { name: "Open Trades", key: "openTradeCount", fixed: -1 },
  { name: "Unrealized P/L", key: "unrealizedPL", fixed: -1 },
  { name: "Closeout %", key: "marginCloseoutPercent", fixed: -1 },
  { name: "Last Transaction ID", key: "lastTransactionID", fixed: -1 },
];
function AccountSummary() {
  const [account, setAccount] = useState(null);

  useEffect(() => {
    loadAccount();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const loadAccount = async () => {
    const data = await endPoints.account();

    setAccount(data);
  };
  // console.log(account[0].id);
  return (
    <>
      <TitleHead title="Account Summary" />

      {account && (
        <div className="segment">
          {DATA_KEYS.map((item) => {
            return (
              <div key={item.key} className="account-row">
                <div className="bold header">{item.name}</div>
                <div>{account[0][item.key]}</div>
              </div>
            );
          })}
        </div>
      )}
    </>
  );
}

export default AccountSummary;
