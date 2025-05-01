pipeline {
    agent {
        docker {
            image 'python:3.10'  // Usa una versión que soporte tu proyecto
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Forez802/python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build') {
            steps {
                sh 'python setup.py install'
            }
        }
    }
}
