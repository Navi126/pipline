pipeline {
    agent any

    environment {
        PATH = "$HOME/.local/bin:$PATH"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Navi126/pipline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py > app.log 2>&1 &'
                sh 'sleep 5'
                sh 'echo "Flask app started in background."'
            }
        }
    }
}

