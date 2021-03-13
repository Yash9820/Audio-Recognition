pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install tensorflow==2.4.1'
                bat 'python -m pip install keras==2.4.3'
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
