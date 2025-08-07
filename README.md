<!-- Animated Futuristic AI Assistant Banner -->
<p align="center">
  <img src="https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif" width="350" alt="AI Assistant Animation"/>
</p>

<h1 align="center">🤖 Friday - AI Voice Assistant</h1>
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=26&pause=1000&width=700&lines=Your+Real-time+Voice+Assistant;Powered+by+LiveKit+Agents+and+Google+Gemini;Voice+Commands+%7C+Web+Search+%7C+Smart+Tools" alt="Typing SVG" />
</p>

---

## ✨ Project Overview

**Friday** is a powerful, real-time AI voice assistant leveraging the [LiveKit Agents](https://github.com/livekit/agents) framework and Google Gemini large language model. It enables natural conversational interactions with voice, incorporates smart tools like web search and weather fetching, and executes website opening commands with ease.

Built with Python, this assistant supports noise cancellation and real-time streaming for crystal-clear communication.

---

## 🚀 Key Features

- Real-time voice conversation with AI-powered natural language processing  
- Integration with Google Gemini API for contextual and intelligent replies  
- On-demand web search using DuckDuckGo  
- Current weather information retrieval by city  
- Voice-activated website opening commands  
- Noise cancellation for enhanced audio clarity  
- Modular architecture with reusable function tools  

---

## 🔑 Setup and Installation

### Prerequisites

- Python 3.8 or higher  
- Git installed on your machine  
- A Google Cloud account for Gemini API access  
- A LiveKit server instance (self-hosted or cloud) with API credentials  

### Step 1: Clone the Repository
  git clone https://github.com/Sujal-3019/livekit-ai-assistant.git
  cd livekit-ai-assistant

### Step 2: Configure Environment Variables
Create a `.env` file in the root directory and add your keys:
  LIVEKIT_URL=wss://your-livekit-server.com
  LIVEKIT_API_KEY=your_livekit_api_key
  LIVEKIT_API_SECRET=your_livekit_api_secret
  google_api_key=your_google_api_key


### How to Obtain Keys

- **LiveKit:**  
  Sign up at [LiveKit Cloud](https://livekit.io/cloud) or deploy your own server. Generate API key and secret from your dashboard.

- **Google Gemini API:**  
  1. Go to [Google Cloud Console](https://console.cloud.google.com).  
  2. Create/select a project and enable the Vertex AI or Gemini API.  
  3. Create API credentials and copy the API key.  
  4. Add it in `.env` as `google_api_key`.  
  *Note: Google Gemini may require beta access or invitation; consult Google Cloud docs.*

### Step 3: Install Dependencies
  pip install -r requirements.txt


### Step 4: Run the Assistant
  python agent.py console



---

## 🎛️ Using the LiveKit Playground for Better Usability

The [LiveKit Playground](https://playground.livekit.io/) is a web interface designed to help you easily test and interact with your LiveKit AI assistant without needing to build a custom client immediately.

### Benefits:

- **Quick testing:** Instantly connect your agent using LiveKit credentials.
- **Multimodal support:** Test voice and video functionalities seamlessly.
- **User-friendly:** Provides an intuitive UI for joining rooms, muting/unmuting, and viewing participant info.
- **Debugging aid:** Monitor logs and session info to troubleshoot or optimize your assistant.

### How to Use:

1. **Go to the LiveKit Playground:**  
   Open [https://playground.livekit.io/](https://playground.livekit.io/).

2. **Enter your LiveKit credentials:**  
   - URL: Your `LIVEKIT_URL` from `.env`  
   - API Key: Your `LIVEKIT_API_KEY`  
   - API Secret: Your `LIVEKIT_API_SECRET`

3. **Join the room your agent is connected to:**  
   Make sure your agent is running and connected to the same room.
   you can run this command to run and connect the agent to playground:
     python agent.py dev

5. **Interact with Friday:**  
   Use your microphone to speak your commands and watch the assistant respond live.

6. **Advanced:**  
   Use the playground for testing multi-user interactions or integrating additional devices.

Using the LiveKit Playground accelerates your development and testing process, offering a production-like environment with no setup overhead on your side.

---

## 🛠️ Project Structure
livekit-ai-assistant/ <br>
├── agent.py          # Core assistant and LiveKit integration <br>
├── tools.py          # Tool implementations: weather, search, website opener <br>
├── prompts.py        # Assistant persona and instructions <br>
├── requirements.txt  # Dependency list <br>
├── .env.example      # Environment variable template <br>
└── README.md         # Project documentation <br>


---

## 💬 Usage Examples

Interact with Friday through your LiveKit client by speaking natural commands:

- "What's the weather in London?"  
- "Search the web for the latest news."  
- "Open Instagram."

Friday listens, processes your request via Google Gemini AI, executes tools as needed, and replies in real time.

---

## 🤝 Contributing

Contributions are welcome! Submit pull requests for bug fixes, new features, or documentation improvements. Please open issues for discussions.

---

## 📚 References

- [LiveKit Documentation](https://docs.livekit.io/)  
- [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai)  
- [DuckDuckGo Search API](https://duckduckgo.com/api)  

---

## ⭐ Show Your Support

If you enjoy this project, please leave a ⭐ on GitHub and share with others!

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Sujal-3019&label=Visitors&color=purple&style=flat" alt="Profile visitors" />
</p>


