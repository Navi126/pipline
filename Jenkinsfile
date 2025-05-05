pipeline {
    agent any

    environment {
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Navi126/pipline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip3 install --user -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}

