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
                bat 'python test.py'
                echo 'Test Done'
                
            }
           
        }
             stage('Run'){
            steps{
                bat 'python main.py'
                echo 'Test Done'
                
            }
           
        }    

    }
}
