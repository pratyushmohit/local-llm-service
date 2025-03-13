# 🧠 Local LLM with Ollama, LangGraph, and Deepseek-r1  

This repository contains a **LLM-powered chatbot** built with [LangGraph](https://github.com/langchain-ai/langgraph) and [Deepseek-r1](https://ollama.ai/library/deepseek-r1). The agent runs on **Ollama** and communicates via **WebSockets**, making it efficient for real-time interactions.

---

## 🚀 Features  
✅ **Deepseek-r1 for NLP** – Uses a powerful open-source LLM for responses.  
✅ **LangGraph for structured conversations** – Enables efficient and scalable workflows.  
✅ **WebSocket-based API** – Enables real-time communication with the chatbot.  
✅ **Lightweight and easy to deploy** – Runs locally with minimal setup.  
✅ **Minikube & Kubernetes Support** – Deploy and scale using Kubernetes.  

---

## 🛠 Installation & Setup  

### 1. Install Ollama  
First, download and install **Ollama** from [ollama.com](https://ollama.com).  

### 2. Run the Deepseek Model  
Once Ollama is installed, start the Deepseek-r1 model:  
```sh
ollama run deepseek-r1
```

### 3. Clone the Repository  
```sh
git clone <repository-url>
cd <repository-folder>
```

### 4. Install Dependencies  
Using uv (a faster alternative to pip):  
```sh
uv pip install -r pyproject.toml
```

### 5. Run the Chatbot  
```sh
uv run app.py
```

### 6. Test the API  
Use an API testing tool like Postman or Insomnia to create a WebSocket request and connect to:  
```sh
ws://localhost:8888/chat
```

---

## 🏗️ Deploying with Minikube & Kubernetes  

### 1. Start Minikube  
```sh
minikube start --cpus=6 --memory=7651MB
```

### 2. (Optional) Update Your Docker Repository  
If needed, update your Docker repository before proceeding.

### 3. Build and Deploy  
```sh
make deploy
```

### 4. Monitor the Pods  
```sh
kubectl get pods
```
Wait for all the pods to show **Running** status.


### 5. Confirm the Model is Downloaded  
```sh
kubectl exec -it deployment/ollama -- /bin/sh
# ollama list
```
Expected output:
```
NAME                ID              SIZE      MODIFIED
deepseek-r1:1.5b    a42b25d8c10a    1.1 GB    About a minute ago
```

### 6. Port Forwarding  
Expose the chatbot service:
```sh
kubectl port-forward deployment/local-llm-service 8888:8888
```

Now, the chatbot is accessible at `ws://localhost:8888/chat`.

---

## Author  
- Pratyush Mohit  

## License  
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.