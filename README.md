# Flask CI/CD with Jenkins

This project demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a simple Flask application using Jenkins and webhooks.

---

##Repository

GitHub: [https://github.com/Navi126/pipline]

---

##Project Overview

The Jenkins pipeline is triggered on each GitHub push and performs the following steps:

1. Clones the latest code from GitHub
2. Installs Python dependencies
3. Starts the Flask application

---

## Setup Instructions

###Prerequisites

- Ubuntu-based server
- Jenkins installed and running
- GitHub account and repo access
- Flask app code with `app.py`, `requirements.txt`, and `Jenkinsfile`
- Python3 and pip3 installed


---

### Jenkins Setup

1. **Install Jenkins** (Skip if already installed)

   ```bash
   sudo apt update
   sudo apt install openjdk-11-jdk -y
   curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
     /usr/share/keyrings/jenkins-keyring.asc > /dev/null
   echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
     https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
     /etc/apt/sources.list.d/jenkins.list > /dev/null
   sudo apt update
   sudo apt install jenkins -y
   sudo systemctl start jenkins

