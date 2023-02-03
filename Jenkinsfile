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
                sh 'python -m venv jenkins_test_env'
                sh 'cd jenkins_test_env/Scripts'
                sh 'activate.bat'
                sh 'cd ../..'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'py.test'
            }
        }
    }
}