pipeline {
    agent any

    environment {
        IMAGE_NAME = "ansk29/memeops"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Repository cloned via Jenkins SCM'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Login to DockerHub & Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                        sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                        sh "docker push ${IMAGE_NAME}"
                    }
                }
            }
        }

        stage('Run MemeOps Container') {
            steps {
                sh 'docker rm -f memeops-container || true' // Remove existing container if running
                sh 'docker run -d --name memeops-container -p 5000:5000 ansk29/memeops'
            }
        }
    }

    post {
        always {
            echo 'Pipeline complete.'
        }
    }
}

