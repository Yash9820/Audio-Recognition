pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                bat 'python -m pip install -r requirements.txt'
                echo 'Build Done'
                
            }
        }
        stage('Test'){
            steps{
                
                echo 'Test Done'
                
            }
        }
    }
}
