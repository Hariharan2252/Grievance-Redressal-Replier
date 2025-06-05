import React, { useState } from 'react';
import './App.css';

function App() {
  const [grievance, setGrievance] = useState('');
  const [tone, setTone] = useState('empathetic');
  const [department, setDepartment] = useState('HR');
  const [response, setResponse] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

const handleSubmit = async (e) => {
  e.preventDefault();
  setLoading(true);
  try {
    const res = await fetch('http://127.0.0.1:8000/generate-reply', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        grievance,
        tone,
        department,
      }),
    });

    const data = await res.json();

    if (res.ok) {
      setResponse(data.reply);
      setHistory(prev => [...prev, { grievance, tone, department, reply: data.reply }]);
    } else {
      setResponse('Error: ' + JSON.stringify(data.detail || data));
    }
  } catch (err) {
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
        <select value={tone} onChange={(e) => setTone(e.target.value)}>
          <option value="empathetic">Empathetic</option>
          <option value="formal">Formal</option>
          <option value="assertive">Assertive</option>
        </select>

        <select value={department} onChange={(e) => setDepartment(e.target.value)}>
          <option value="HR">HR</option>
          <option value="Technical Support">Technical Support</option>
          <option value="Accounts">Accounts</option>
          <option value="Admin">Admin</option>
        </select>

        <button onClick={handleSubmit} disabled={loading || !grievance}>
          {loading ? 'Generating...' : 'Generate Reply'}
        </button>
      </div>

      {response && (
        <div className="response-box">
          <h3>AI-Generated Response:</h3>
          <p>{response}</p>
        </div>
      )}

      {history.length > 0 && (
        <div className="history-box">
          <h3>Response History</h3>
          <ul>
            {history.map((item, index) => (
              <li key={index}>
                <strong>{item.department} | {item.tone}</strong><br />
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
