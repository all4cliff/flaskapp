pipeline {
    agent any

    stages {
        stage('Checkout scm') {
            steps {
                git branch: 'main', url: 'https://github.com/all4cliff/flaskapp.git'
            }
        }

        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/all4cliff/flaskapp.git'
            }
        }

        stage('Install Packages') {
            steps {
                sh 'virtualenv venv'
                sh 'source venv/bin/activate && pip install flask'
                sh 'chmod -R 755 venv'
            }
        }
        
        stage('Test') {
      steps {
        sh 'source venv/bin/activate && python test.py'
      }
    }
        stage('Deploy') {
            steps {
                input "Approve deployment?"
                // deploy code here
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'classwork01', inventory: 'host.ini', playbook: 'flaskapp01.yml'
            }
        }
    }
}
