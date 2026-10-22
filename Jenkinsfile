
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Check Tools') {
            steps {
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t little-bloom-cafe:local .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat 'docker rm -f little-bloom-cafe 2>NUL || exit /b 0'
                bat 'docker run -d --name little-bloom-cafe -p 5000:5000 little-bloom-cafe:local'
            }
        }

        stage('Verify Application') {
            steps {
                bat 'curl.exe --fail --retry 10 --retry-connrefused --retry-delay 2 http://localhost:5000/'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Tests passed, image built, and application verified.'
        }
        failure {
            echo 'FAILED: Check the stage console output to identify the error.'
        }
    }
}
