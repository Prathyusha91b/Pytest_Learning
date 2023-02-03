pipeline {
    agent any

    stages {
        stage('Stage 1') {
            steps {
                echo 'This is from Jenkinsfile in Github'
            }
        }
        stage('Setup Environment'){
            steps{
                bat '''
                python -m venv jenkins_test_env
                cd jenkins_test_env/Scripts
                activate.bat
                cd ../..
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests'){
            steps{
                bat '''
                py.test
                '''
            }
        }
    }
}