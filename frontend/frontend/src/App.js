import React, { useState } from 'react';
import './App.css';

function App() {
  const [grievance, setGrievance] = useState('');
  const [response, setResponse] = useState('');
  const [prediction, setPrediction] = useState({});
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/generate-reply", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: grievance }),
      });

      const data = await res.json();
      console.log("Backend Response:", data);

      if (res.ok && data.reply) {
        setResponse(data.reply);
        setPrediction({
          tone: data.predicted_tone,
          department: data.predicted_department,
          label: data.predicted_label
        });

        setHistory(prev => [
          ...prev,
          {
            grievance,
            reply: data.reply,
            ...data
          }
        ]);
      } else {
        setResponse('Error: ' + (data.detail || 'Unexpected response'));
      }
    } catch (err) {
      console.error("Error:", err);
      setResponse('Error connecting to the server');
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Grievance Redressal Replier</h1>

      <textarea
        placeholder="Enter your grievance..."
        value={grievance}
        onChange={(e) => setGrievance(e.target.value)}
      />

      <div className="controls">
        <button onClick={handleSubmit} disabled={loading || !grievance}>
          {loading ? 'Generating...' : 'Generate Reply'}
        </button>
      </div>

      {response && (
        <div className="response-box">
          <h3>AI-Generated Response:</h3>
          <p>{response}</p>
          <div style={{ marginTop: 10 }}>
            <strong>Predicted Label:</strong> {prediction.label}<br />
            <strong>Predicted Tone:</strong> {prediction.tone}<br />
            <strong>Predicted Department:</strong> {prediction.department}
          </div>
        </div>
      )}

      {history.length > 0 && (
        <div className="history-box">
          <h3>Response History</h3>
          <ul>
            {history.map((item, index) => (
              <li key={index}>
                <strong>{item.predicted_department} | {item.predicted_tone} | {item.predicted_label}</strong><br />
                <em>{item.grievance}</em><br />
                {item.reply}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;