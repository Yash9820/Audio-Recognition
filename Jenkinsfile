pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                bat 'python -m pip install -r requirements.txt'
                echo 'Build Done'
                
            }
        }
        stage('unittest'){
            steps{
                bat 'pytest --junitxml result.xml'
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
