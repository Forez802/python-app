pipeline {
    agent { label 'agent-any' }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Forez802/python-app.git'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'which python3'
                sh 'python3 --version'
            }
        }

        stage('Install') {
            steps {
                sh 'python3 -m pip install --upgrade pip --break-system-packages'
                sh 'pip install -r requieremts.txt --break-system-packages'
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