ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Define image name and tag
REPOSITORY_NAME := pratyushmohitk/nautilus
IMAGE_NAME := local-llm-service
TAG := latest
FULL_IMAGE_NAME := $(REPOSITORY_NAME):$(TAG)

# Build the Docker image
build:
	docker build -t $(FULL_IMAGE_NAME) -f Dockerfile .

# Run the container locally (not in Minikube)
run:
	docker run -dp 8888:8888 --name $(IMAGE_NAME) $(FULL_IMAGE_NAME)

# Push the image to Docker Hub
push:
	docker push $(FULL_IMAGE_NAME)

# Deploy to kubernetes
deploy:
	kubectl apply -f k8s/local-llm-service-deployment.yaml
	kubectl apply -f k8s/local-llm-service.yaml
	kubectl apply -f k8s/ollama-deployment.yaml
	kubectl apply -f k8s/ollama-service.yaml

# Clean up containers and deployments
clean:
	kubectl delete -f k8s/local-llm-service-deployment.yaml
	kubectl delete -f k8s/local-llm-service.yaml
	kubectl delete -f k8s/ollama-deployment.yaml
	kubectl delete -f k8s/ollama-service.yaml

all: build push deploy