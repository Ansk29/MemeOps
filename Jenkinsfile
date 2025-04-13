pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ansk29/memeops"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'git@github.com:Ansk29/MemeOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Login to DockerHub & Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push ansk29/memeops
                    '''
                }
            }
        }

        stage('Deploy via Ansible') {
            steps {
                // No password prompt! So either use passwordless sudo or limit sudo in playbook
                sh '''
                    ansible-playbook ansible-deploy/deploy.yml -i ansible-deploy/hosts
                '''
            }
        }
    }

    post {
        always {
            // Cleanup old container if any
            sh 'docker rm -f memeops-app || true'
        }
    }
}

