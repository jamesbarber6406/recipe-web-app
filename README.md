# Recipe web app

A static web application that displays a cooking recipe with images using Docker and Nginx.

## Project Structure
```
recipe-web-app/
    recipe-app # Static site files
    recipe-infra # Kubernetes deployment using Pulumi and Minikube
```

## Tech Stack
- **Frontend**: Static HTML & images served by Nginx
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Minikube)
- **Infrastructure as Code**: Pulumi (Python SDK)

## Setup & Deployment

### Prerequisites
- Docker
- Minikube
- Pulumi CLI
- Python v.3.13.5

### Step 1. Build & Push the Docker Image
```bash
cd recipe-app
docker build -t priestjimbo/recipe-site:latest .
docker push priestjimbo/recipe-site:latest
```

### Step 2. Deploy to Kubernetes with Pulumi
```bash
cd recipe-infra
pulumi up
```

### Step 3. Access the Site
```bash
minikube service recipe-app-service
```

## What I Learned
- Using Pulumi to manage K8s infrastructure
- Writing Kubernetes deployments in Python
- Using GitHub to structure a project
- Deploying static content using Docker containers

## Next Steps
- Monitor with Prometheus + Grafana
- Add a custom domain & HTTPS
- Use GitHub Actions to add CI/CD
- Package as a Helm chart

