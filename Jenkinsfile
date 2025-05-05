pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Navi126/pipline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
            }
        }

        stage('Restart Flask App') {
            steps {
                sh '''
                    pkill -f app.py || true
                    nohup python3 app.py > output.log 2>&1 &
                '''
            }
        }
    }
}

