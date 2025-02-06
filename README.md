# 🧠 Local LLM with LangGraph and Deepseek-r1  

This repository contains a **LLM-powered chatbot** built with [LangGraph](https://github.com/langchain-ai/langgraph) and [Deepseek-r1](https://ollama.ai/library/deepseek-r1). The agent runs on **Ollama** and communicates via **WebSockets**, making it efficient for real-time interactions.

---

## 🚀 Features  
✅ **Deepseek-r1 for NLP** – Uses a powerful open-source LLM for responses.  
✅ **LangGraph for structured conversations** – Enables efficient and scalable workflows.  
✅ **WebSocket-based API** – Enables real-time communication with the chatbot.  
✅ **Lightweight and easy to deploy** – Runs locally with minimal setup.  

---

## 🛠 Installation & Setup  

### 1. Install Ollama  
First, download and install **Ollama** from [ollama.com](https://ollama.com).  

### 2️. Run the Deepseek Model  
Once Ollama is installed, start the Deepseek-r1 model:  
```sh
ollama run deepseek-r1
```

### 3. Clone the Repository
```
git clone <repository-url>
cd <repository-folder>
```

### 4. Install Dependencies
Using uv (a faster alternative to pip):
```
uv pip install -r pyproject.toml
```

### 5. Run the chatbot
```
uv run app.py
```

### 6. Test the API
Use an API testing tool like Postman or Insomnia to create a WebSocket request and connect to:
```
ws://localhost:8888/chat
```

## Author
- Pratyush Mohit

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.