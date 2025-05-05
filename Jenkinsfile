pipeline {
    agent any

    environment {
        // Optional: Activate virtualenv or define Python path
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
                which pip3 || sudo apt-get update && sudo apt-get install -y python3-pip
                pip3 install -r requirements.txt
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

