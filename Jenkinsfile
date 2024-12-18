pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_IMAGE = "achaud70/fastapi-pipeline"
        DOCKER_TAG = ""
        PATH = "/usr/local/bin:/usr/bin:/bin:${PATH}"
    }
    
    triggers {
        githubPush()
    }
    
    stages {
        stage('Setup Python') {
            steps {
                script {
                    sh '''
                        # Create and activate virtual environment
                        python3 -m venv venv
                        . venv/bin/activate
                        
                        # Upgrade pip and install all required packages
                        python3 -m pip install --upgrade pip
                        pip install pylint fastapi pytest requests
                    '''
                }
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Code Quality Check') {
            steps {
                script {
                    sh '''
                        # Activate virtual environment and run pylint
                        . venv/bin/activate
                        pylint --fail-under=7.0 app/
                    '''
                }
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Login to DockerHub
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE:latest .'
                    
                    // Push Docker image
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }
        
        stage('Run Integration Tests') {
            steps {
                script {
                    sh '''
                        # Activate virtual environment
                        . venv/bin/activate
                        
                        # Start the API container
                        docker run -d -p 8000:8000 --name fastapi-test $DOCKER_IMAGE:latest
                        
                        # Wait for API to be ready
                        sleep 10
                        
                        # Run integration tests
                        pytest tests/integration/
                    '''
                }
            }
            post {
                always {
                    sh '''
                        # Cleanup: Stop and remove the test container
                        docker stop fastapi-test || true
                        docker rm fastapi-test || true
                    '''
                }
            }
        }
        
        stage('Tag Version') {
            steps {
                script {
                    // Get the latest tag
                    def latestTag = sh(script: "git describe --tags --abbrev=0 || echo 'v0.0.0'", returnStdout: true).trim()
                    
                    // Increment version
                    def (major, minor, patch) = latestTag.replaceAll('v', '').tokenize('.')
                    def newPatch = patch.toInteger() + 1
                    def newTag = "v${major}.${minor}.${newPatch}"
                    
                    // Set the new tag
                    DOCKER_TAG = newTag
                    
                    // Tag the code
                    sh """
                        git tag ${newTag}
                        git push origin ${newTag}
                        
                        # Tag and push Docker image with version
                        docker tag $DOCKER_IMAGE:latest $DOCKER_IMAGE:${newTag}
                        docker push $DOCKER_IMAGE:${newTag}
                    """
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
            cleanWs()
        }
    }
}
