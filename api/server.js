const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 3000;

// 🔒 Replace this with your actual API key (temporarily)
const OPENAI_API_KEY = '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';

app.post('/generate-reply', async (req, res) => {
  const { message, tone } = req.body;

  const prompt = `
You are an HR support agent. Respond to the following grievance in a ${tone} tone:

Grievance: ${message}

Response:
`;

  try {
    const response = await axios.post(
      'https://api.openai.com/v1/chat/completions',
      {
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.7,
      },
      {
        headers: {
          Authorization: `Bearer ${OPENAI_API_KEY}`,
          'Content-Type': 'application/json',
        },
      }
    );

    res.json({ reply: response.data.choices[0].message.content.trim() });
  } catch (error) {
    console.error("OpenAI Error:", error.response?.data || error.message);
    res.status(500).json({ error: 'Failed to generate reply' });
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
