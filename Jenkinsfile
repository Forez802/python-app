pipeline {
    agent { label 'agent1' }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Forez802/python-app.git'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'which python3'
                sh 'python3 --version'pipeline {
    agent { label 'docker-agent' } // o 'agent1', 'remoto1', etc.

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/usuario/python-app.git'
            }
        }

        stage('Construir contenedores') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Levantar servicios') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Esperar servicios') {
            steps {
                sh 'sleep 15' // Esperar a que Flask y MySQL levanten
            }
        }

        stage('Probar API con Locust') {
            steps {
                sh 'docker-compose run locust --headless -u 10 -r 2 -t 20s'
            }
        }

        stage('Limpiar') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
}

            }
        }

        stage('Install') {
            steps {
                sh 'python3 -m pip install --upgrade pip --break-system-packages'
                sh 'pip install -r requirements.txt --break-system-packages'
                sh 'pip install pytest-html --break-system-packages'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    export PATH=$PATH:/home/jenkins/.local/bin
                    pytest --html=report.html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
