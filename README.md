# Recipe web app

A static web application that displays a cooking recipe with images using Docker and Nginx.

## Features
- Static HTML site
- Hosted in a Docker container using Nginx
- Includes step-by-step instructions

## How to run

```bash
docker build -t recipe-site .
docker run -d -p 8080:80 recipe-site
```

Then visit [http://localhost:8080](http://localhost:8080)