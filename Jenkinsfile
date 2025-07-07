pipeline {
    agent any
    stages {
        stage('Prepare Environment') {
            steps {
                echo 'Starting the Pipeline...'
            }
        }
        stage('Execute Python Script') {
            steps {
                sh '''
                echo CherryBomb | sudo -S python3 /home/CherryBomb/Desktop/jenkins-test/2-service_managment.py
                '''
            }
        }
        stage('Show Logs') {
            steps {
                sh 'cat /var/lib/jenkins/workspace/test-locally-python-script/service_availability_logs.log || echo "Log file not found"'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
