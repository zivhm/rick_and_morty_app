# Rick and Morty DevOps Task

## Step 1: Script

**Objective:**  

1. Query “Rick and Morty” API and look for all characters that meets the following conditions:
  
- Species is “Human”
- Status is “Alive”
- Origin is “Earth”

2. Make a list of the results that will include:

- Name
- Location
- Image link.

3. Write the results to a csv file

Script process:

1. Fetch data from the API.
2. Filter characters based on the conditions.
3. Save the results in a CSV file with the following fields:
   - Name
   - Origin
   - Location
   - Image link

**Example Output CSV:**

```
Name,Origin,Location,Image
Rick Sanchez,Earth,Earth,https://rickandmortyapi.com/api/character/avatar/1.jpeg
```

## Step 2: Dockerized App

**Objective:** Convert the script into a REST API application.

### Features

- **REST API Endpoints:**
  - `/characters`: Returns the filtered characters in JSON format.
  - `/healthcheck`: Returns the health status of the application.
  - `/export`: Exports the filtered characters to a CSV file.

### Dockerization

1. Create a `Dockerfile` to containerize the application.
2. Build and run the Docker image.

**Commands:**

```bash
# Build Docker image
docker build -t rick_and_morty_app .

# Run Docker container
docker run -p 5000:5000 rick_and_morty_app
```

## Step 3: Kubernetes

**Objective:** Deploy the Dockerized application to a Kubernetes cluster using minikube.

### Folder Structure

- `yamls/`:
  - `Deployment.yaml`: Defines the deployment configuration.
  - `Service.yaml`: Exposes the application as a service.
  - `Ingress.yaml`: Configures the ingress for external access.

### Deployment Steps

1. Start minikube:

   ```bash
   minikube start
   ```

2. Apply the manifests:

   ```bash
   kubectl apply -f yamls/
   ```

3. Verify the application is running and accessible:

   ```bash
   kubectl get pods
   kubectl get services
   ```

4. Update minikube IP as a host:

   ```bash
   minikube ip
   ```

   then in /etc/hosts add an entry:

   ```
   <minikube-ip> rickandmorty.local
   ```

5. Access the application:

   ```
   http://rickandmorty.local/healthcheak
   ```

## Step 4: Helm

**Objective:** Package the Kubernetes resources as a Helm chart for easy deployment.

### Folder Structure

- `helm/`:
  - `Chart.yaml`: Contains metadata about the Helm chart.
  - `values.yaml`: Defines default configurations.
  - `templates/`: Contains the Kubernetes resource templates.

### Deployment Steps

1. Install the application using Helm:

   ```bash
   helm install rick-and-morty helm/
   ```

2. Verify the deployment:

   ```bash
   helm list
   ```

### GitHub Actions Workflow with Minikube

This repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automates the deployment and testing of the application in a Minikube Kubernetes cluster.

#### Workflow Steps
1. **Set up Minikube Cluster**:
   - Installs Minikube, `kubectl`, and Helm.
   - Starts a Minikube cluster using Docker.

2. **Deploy Application**:
   - Deploys the application to the Minikube cluster using Helm.

3. **Run Tests**:
   - Executes the `tests/test_endpoints.py` script to test application endpoints.

#### Workflow Details
- **setup-cluster**: Prepares the Minikube environment and cluster.
- **deploy-app**: Deploys the application to the cluster.
- **test-endpoints**: Verifies the application by running tests.

#### Triggering the Workflow
The workflow is triggered on every push to the `main` branch. Workflow logs can be viewed in the GitHub Actions tab.
