import React from "react";

const PredictionHistory = ({ history }) => {
  if (!history || history.length === 0) {
    return (
      <div className="stat-card">
        <div className="stat-label">Prediction History</div>
        <div className="stat-value">No predictions yet.</div>
      </div>
    );
  }

  return (
    <div className="stat-card">
      <div className="stat-label">Prediction History</div>

      <table style={{ width: "100%", marginTop: "1rem" }}>
        <thead>
          <tr>
            <th align="left">Patient</th>
            <th align="left">Prediction</th>
            <th align="left">Probability</th>
          </tr>
        </thead>

        <tbody>
          {history.map((item) => (
            <tr key={item.id}>
              <td>{item.patient_id}</td>
              <td>
                {item.prediction === 1
                  ? "Heart Disease"
                  : "No Heart Disease"}
              </td>
              <td>{(item.probability * 100).toFixed(1)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PredictionHistory;
