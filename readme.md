# Rick and Morty API

## Overview

This project fetches data from the [Rick and Morty API](https://rickandmortyapi.com/), filters <B>human</B> characters who are <B>alive</B> and their origin is from <B>Earth</B>, and exposes this data through a RESTful API. The application is containerized with Docker and deployed to a Kubernetes cluster using Minikube.

## Features

1. **Data Extraction & CSV Generation**
   - Retrieves characters with:
     - **Species:** Human
     - **Status:** Alive
     - **Origin:** Earth
   - Generates a CSV with:
     - Name
     - Origin
     - Location
     - Image Link

2. **REST API**
   - **Endpoints:**
     - `/healthcheck` - Checks service status.
     - `/characters` - Returns filtered character data.
     - `/export` - Exports data to CSV.

3. **Containerization & Deployment**
   - **Docker:** Containerizes the application.
   - **Kubernetes (Minikube):** Deploys using Helm charts.

4. **CI/CD Pipeline**
   - **GitHub Actions:** Automates the deployment and testing process.

## Requirements

- **Local:**
  - Python 3.9
  - Flask, requests, pandas
- **Containerization & Deployment:**
  - Docker
  - Minikube, kubectl, Helm

## Setup

### Running Locally

1. **Setup Virtual Environment (Optional):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Start Application:**
    ```sh
    python app.py
    ```
    Access:
    - [http://localhost:5000/healthcheck](http://localhost:5000/healthcheck)
    - [http://localhost:5000/characters](http://localhost:5000/characters)
    - [http://localhost:5000/export](http://localhost:5000/export)

### Using Docker

1. **Build Image:**
    ```sh
    docker build -t zivhm/rick-and-morty-api:latest .
    ```

2. **Run Container:**
    ```sh
    docker run -p 5000:5000 zivhm/rick-and-morty-api:latest
    ```
    Access the same endpoints as above.

### Deploying to Kubernetes (Minikube)

1. **Start Minikube:**
    ```sh
    minikube start
    ```

2. **Use Minikube’s Docker:**
    ```sh
    eval $(minikube docker-env)
    docker build -t zivhm/rick-and-morty-api:latest .
    ```

3. **Deploy with Helm:**
    ```sh
    helm install rick-and-morty-api ./helm
    ```

4. **Access Application:**
    - Get Minikube IP:
      ```sh
      minikube ip
      ```
    - Update `/etc/hosts`:
      ```
      <minikube_ip> rickmorty.local
      ```
    - Access:
      - [http://rickmorty.local/healthcheck](http://rickmorty.local/healthcheck)
      - [http://rickmorty.local/characters](http://rickmorty.local/characters)
      - [http://rickmorty.local/export](http://rickmorty.local/export)

## CI/CD Pipeline

This project uses GitHub Actions to automate the deployment and testing process to a Kubernetes cluster via Minikube. The pipeline is triggered on every push to the `main` branch.

### GitHub Actions

The GitHub Actions workflow automates the following tasks:

1. **Code Checkout**: Retrieves the latest code from the repository.
2. **Docker Build & Setup**: Sets up Docker Buildx and prepares the application Docker image.
3. **Minikube Setup**: Installs and starts Minikube to create a local Kubernetes cluster.
4. **Kubernetes Setup**: Installs `kubectl` and configures it to use the Minikube cluster.
5. **Helm Deployment**: Deploys the application using Helm charts.
6. **Dependency Installation**: Installs required Python dependencies.
7. **Test Execution**: Runs tests to ensure that the application is working correctly.

### Workflow

The workflow is defined in the `.github/workflows/deploy.yml` file and follows these steps:

1. **Check out Code**: 
    - The workflow starts by checking out the latest version of the code from the repository.

2. **Set up Docker Buildx**:
    - Sets up Docker Buildx to enable building multi-platform images.

3. **Install Minikube**:
    - Installs Minikube, the local Kubernetes cluster, and starts it using Docker as the driver.

4. **Install kubectl**:
    - Installs `kubectl`, the Kubernetes command-line tool, and configures it to communicate with the Minikube cluster.

5. **Install Helm**:
    - Installs Helm, the Kubernetes package manager, which is used to manage the deployment.

6. **Configure kubectl for Minikube**:
    - Configures `kubectl` to use the Minikube context to interact with the local Kubernetes cluster.

7. **Deploy with Helm**:
    - Deploys the application to Kubernetes using Helm charts. If the application is already deployed, it will be upgraded.

8. **Install Dependencies**:
    - Installs the Python dependencies required for the application.

9. **Run Tests**:
    - Runs automated tests to ensure that the application is working as expected.

