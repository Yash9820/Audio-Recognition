pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install tensorflow'
                bat 'python -m pip install keras'
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
