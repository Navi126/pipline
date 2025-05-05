pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://codeberg.org/naveen123/devops-flask-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Restart App') {
            steps {
                sh 'pkill -f app.py || true'
                sh 'nohup python3 app.py > output.log 2>&1 &'
            }
        }
    }
}
