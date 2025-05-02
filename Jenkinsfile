pipeline {
    agent { label 'agent1' }  // Esto especifica que se debe usar el agente con la etiqueta 'agent1'

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Forez802/python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python setup.py install'
                }
            }
        }
    }
}
