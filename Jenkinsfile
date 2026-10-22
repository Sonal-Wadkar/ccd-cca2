
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Sonal-Wadkar/ccd-cca2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloud-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop cloud-app || true
                    docker rm cloud-app || true
                    docker run -d --name cloud-app \
                        -p 5000:5000 cloud-app
                '''
            }
        }
    }
}
