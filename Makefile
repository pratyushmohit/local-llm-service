ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Define image name and tag
IMAGE_NAME := local-llm-service
TAG := latest

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):$(TAG) -f Dockerfile .

# Run the container locally (not in Minikube)
run:
	docker run -dp 8888:8888 --name $(IMAGE_NAME) $(IMAGE_NAME):$(TAG)

# Deploy to Minikube
deploy:
    # Ensure Minikube uses its internal Docker
	eval $$(minikube docker-env)
	docker build -t $(IMAGE_NAME):$(TAG) -f Dockerfile .
	minikube image load $(IMAGE_NAME):$(TAG)  # Load image into Minikube
	kubectl apply -f k8s/local-llm-service-deployment.yaml
	kubectl apply -f k8s/local-llm-service.yaml
	kubectl apply -f k8s/ollama-deployment.yaml
	kubectl apply -f k8s/ollama-service.yaml

# Clean up containers and deployments
clean:
	docker stop $(IMAGE_NAME) || true
	docker rm $(IMAGE_NAME) || true
	docker rmi $(IMAGE_NAME):$(TAG) || true
	kubectl delete -f k8s/local-llm-service-deployment.yaml || true
	kubectl delete -f k8s/local-llm-service.yaml || true
	kubectl delete -f k8s/ollama-deployment.yaml || true
	kubectl delete -f k8s/ollama-service.yaml || true
