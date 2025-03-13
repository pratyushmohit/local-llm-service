# 🧠 Local LLM with Ollama, Kubernetes, LangGraph, and Deepseek-r1  

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


### 1. Clone the Repository  
```sh
git clone <repository-url>
cd <repository-folder>
```

### 2. Start Minikube  
```sh
minikube start --cpus=6 --memory=7651MB
```

### 3. (Optional) Update Your Docker Repository  
If needed, update your Docker repository before proceeding.

### 4. Build and Deploy  
```sh
make deploy
```

### 5. Monitor the Pods  
```sh
kubectl get pods
```
Wait for all the pods to show **Running** status.


### 6. Confirm the Model is Downloaded  
```sh
kubectl exec -it deployment/ollama -- /bin/sh
# ollama list
```
Expected output:
```
NAME                ID              SIZE      MODIFIED
deepseek-r1:1.5b    a42b25d8c10a    1.1 GB    About a minute ago
```

### 7. Port Forwarding  
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