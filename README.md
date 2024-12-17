# FastAPI with Jenkins Pipeline

A FastAPI application with automated CI/CD using Jenkins pipeline and Docker containerization.

## API Endpoints

- `GET /`: Root endpoint returning a greeting message
- `GET /health`: Health check endpoint returning service status

## Local Development

### Prerequisites
- Python 3.9+
- Docker
- Jenkins (for CI/CD)

### Setup

1. **Create Virtual Environment**

```
python3 -m venv venv
source venv/bin/activate
```
2. **Install Dependencies**

```
pip install -r requirements.txt
```
3. **Run the Application**
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at `http://localhost:8000`

## Docker

### Build Image

```
docker build -t fastapi-pipeline .
```

### Run Container
```
docker run -d -p 8000:8000 fastapi-pipeline
```

## Testing


### Run Tests
```
pytest tests/integration/test_api.py -v
```

## Jenkins Pipeline

The Jenkins pipeline automates:
1. Python environment setup
2. Code quality checks (pylint)
3. Docker image building and pushing
4. Integration testing
5. Version tagging

### Pipeline Stages
- Setup Python
- Code Quality Check
- Build and Push Docker Image
- Run Integration Tests
- Tag Version

### Requirements
- Jenkins with Docker installed
- DockerHub credentials configured in Jenkins
- GitHub webhook configured for automated triggers

## CI/CD Flow

1. Push code to GitHub
2. GitHub webhook triggers Jenkins pipeline
3. Jenkins runs all pipeline stages
4. On success:
   - New Docker image is pushed to DockerHub
   - New version tag is created
   - Code is ready for deployment


## License

This project is licensed under the MIT License - see the LICENSE file for details
