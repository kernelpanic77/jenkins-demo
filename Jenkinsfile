pipeline { 
agent any
    stages {
        stage('REPO CLONING') {
            steps {
                git 'https://github.com/kernelpanic77/jenkins-demo'
            }
        }
        stage('EXECUTING MAIN') {
            steps {
		sh "chmod u+x main.py"
                sh "python3 main.py"
            }
        }
     stage('RUNNING TESTS') {
            steps {
		sh "chmod u+x spec.py"
                sh "python3 spec.py"
            }
        }
    } 
    post {  
      always {  
          mail bcc: '', body: "<b>Jenkins Build Info</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "SUCCESS CI: Project name -> ${env.JOB_NAME}", to: "shanware.ishan@gmail.com";  
      }  
      success {  
          mail bcc: '', body: "<b>Jenkins Build Info</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "SUCCESS CI: Project name -> ${env.JOB_NAME}", to: "shanware.ishan@gmail.com";  
      }  
      failure {  
          mail bcc: '', body: "<b>Jenkins Build Info</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "shanware.ishan@gmail.com";  
      }  
      unstable {  
          echo 'This will run only if the run was marked as unstable'  
      }  
      changed {  
          echo 'This will run only if the state of the Pipeline has changed'  
          echo 'For example, if the Pipeline was previously failing but is now successful'  
            }  
     }
}