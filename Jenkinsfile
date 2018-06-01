pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pipenv install --dev'
            }
        }
        stage('Test') {
            steps {
                sh 'pipenv run nosetests'
            }
        }
    }
}
