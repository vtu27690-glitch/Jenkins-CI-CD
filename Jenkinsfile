
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'python --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing the project...'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment completed successfully!'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build completed successfully!",
                to: "vtu27690@veltech.edu.in"
            )
        }

        failure {
            emailext(
                subject: "BUILD FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build failed. Check Jenkins console output.",
                to: "vtu27690@veletch.edu.in"
            )
        }
    }
}
