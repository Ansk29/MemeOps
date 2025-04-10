pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning Repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("memeops-app")
                }
            }
        }

        stage('Run App in Container') {
            steps {
                sh 'docker run -d -p 5000:5000 memeops-app'
            }
        }
    }
}
