pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                
                bat 'python -m pip install -r requirements.txt'
                echo 'Build Done'
                
            }
        }
       
        stage('Run'){
            steps{
                bat 'python test.py'
                echo 'Test Done'
                
            }
           
        }
                

    }
}
