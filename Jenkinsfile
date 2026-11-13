pipeline {
  agent any

  environment {
    IMAGE = 'devpos/devops-app:1.0'
  }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build image') {
      steps {
        sh 'docker build -t "$IMAGE" .'
      }
    }

    stage('Test') {
      steps {
        sh 'docker build --target test .'
      }
    }

    stage('Deploy') {
      steps {
        sh 'docker compose -f compose.yaml up -d --wait'
      }
    }

    stage('Verify') {
      steps {
        sh 'curl -fsS http://localhost:5000/health'
        sh 'docker compose -f compose.yaml exec -T app python -c "import socket; print(socket.gethostbyname(\'redis\'))"'
      }
    }
  }

  post {
    success {
      sh 'docker compose -f compose.yaml ps'
    }
    failure {
      sh 'docker compose -f compose.yaml logs --tail=50 || true'
    }
  }
}