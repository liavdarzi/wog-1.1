pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url:'https://github.com/liavdarzi/wog-1.1.git']])
            }
        }
        stage('Build'){
            steps {
                script{
                    bat 'docker-compose up'
                }
            }
        }
        stage('Run'){
            steps{
                script{
                    bat 'docker run -p 8777:5000 -v /wog-1.1/Scores.txt wog-wog'
                }
            }
        }
        stage('Test'){
            steps{
                script{
                def x = bat script: 'python e2e.py', returnStatus: true
                assert x == 0 : "End-to-end tests failed with exit code -1"
                }
            }
        }
        stage('Finalize'){
            steps{
                script{
                        bat 'docker login -u liavdarzi -p liavD123456' 
                        bat 'docker tag wog-wog liavdarzi/wog-wog:latest'
                        bat 'docker push liavdarzi/wog-wog:latest'
                }
            }
        }
    }
}
