pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Codigo clonado'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
}
