pipeline {
    agent { label 'agent1' }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Forez802/python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Crear un entorno virtual y activarlo
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Ejecutar pruebas en el entorno virtual
                    sh '. venv/bin/activate && pytest'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Realizar la construcción en el entorno virtual
                    sh '. venv/bin/activate && python setup.py install'
                }
            }
        }
    }
}
