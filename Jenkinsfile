pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('')])])
                }
                bat 'python -m pip install -r requirements.txt'
                echo 'Build Done'
                
            }
        }
        stage('Test'){
            steps{
                bat 'python main.py'
                echo 'Test Done'
                
            }
        }
    }
}
