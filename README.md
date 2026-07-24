# 🌦️ Weather & Time Detection

<p align="center">
  <img src="assets/banner.png" alt="Weather & Time Detection Banner" width="100%">
</p>

<p align="center">
  <strong>An AI-powered multi-tool assistant built with Google ADK, Gemini API, and Python.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Google-ADK-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Gemini-AI-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

---

# 📖 Overview

Weather & Time Detection is an intelligent AI assistant that uses **Google Agent Development Kit (ADK)** and the **Gemini API** to understand natural language requests and automatically invoke the correct tool for retrieving real-time weather and current time information.

Unlike traditional applications that rely on hard-coded logic, this project demonstrates **agentic AI** through dynamic tool calling.

---

# ✨ Features

- 🌦️ Real-time weather information
- 🕒 Current time lookup
- 🤖 Gemini-powered reasoning
- 🧠 Google ADK tool calling
- ⚙️ Modular architecture
- 🔐 Secure API key management using `.env`

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| AI Framework | Google ADK |
| LLM | Gemini API |
| APIs | Weather & Time APIs |
| Libraries | google-adk, google-genai, requests, geopy, python-dotenv |
| Tools | Git, GitHub, PyCharm |

---

# 🏗️ Architecture

```text
                 User
                   │
                   ▼
          Google ADK Agent
                   │
                   ▼
           Gemini AI Model
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
 Weather Tool              Time Tool
      │                         │
      ▼                         ▼
 External API             Time Service
      │                         │
      └────────────┬────────────┘
                   ▼
          Formatted Response
```

---

# 📂 Project Structure

```text
Weather-and-Time-Detection/
├── agent.py
├── listAPI.py
├── tools/
├── screenshots/
├── assets/
├── docs/
├── README.md
├── requirements.txt
├── .env.example
├── LICENSE
└── .gitignore
```

---

# ⚙️ Installation

```bash
git clone https://github.com/rahulgadalay/Weather-and-Time-Detection.git
cd Weather-and-Time-Detection
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run:

```bash
python agent.py
```

---

# 💬 Example Queries

```text
What is the weather in Hyderabad?

Tell me the current time in Tokyo.

What's the weather like in London?

Current time in New York
```

---
## 📸 Project Screenshots

### 🌦️ Weather Detection

<p align="center">
  <img src="screenshots/weather.png" width="900">
</p>

The AI agent intelligently identifies weather-related queries, invokes the Weather Tool through Google ADK, and retrieves real-time weather information.

---

### 🕒 Time Detection

<p align="center">
  <img src="screenshots/time.png" width="900">
</p>

The Time Tool determines the requested location and returns the current local time using Google's Agent Development Kit.

---

# 🧠 How It Works

1. User enters a natural language query.
2. Gemini understands the request.
3. Google ADK selects the appropriate tool.
4. The selected tool retrieves live data.
5. The response is formatted and returned.

---

# 🚀 Future Enhancements

- Multi-agent workflow
- Conversation memory
- RAG integration
- Voice assistant
- Docker support
- CI/CD
- Unit testing
- News tool
- Currency converter
- Calendar integration

---

# 📚 Learning Outcomes

This project demonstrates:

- Agentic AI
- Google ADK
- Gemini API Integration
- Tool Calling
- REST API Integration
- Python Project Structure
- Environment Variable Management
- Git & GitHub Best Practices

---

# 🤝 Contributing

Contributions are welcome. Fork the repository, create a feature branch, and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Rahul Gadalay**

- Data Engineering Enthusiast
- AI & Generative AI Developer
- GitHub: https://github.com/rahulgadalay
- Linkedin: https://www.linkedin.com/in/rahul-gadalay/

⭐ If you found this project useful, consider starring the repository!
