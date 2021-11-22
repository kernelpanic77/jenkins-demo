pipeline { 
agent any
    stages {
        stage('clone the repository') {
            steps {
                git 'https://github.com/kernelpanic77/jenkins-demo'
            }
        }
        stage('exec main') {
            steps {
		sh "chmod u+x main.py"
                sh "python3 main.py"
            }
        }
     stage('run tests') {
            steps {
		sh "chmod u+x spec.py"
                sh "python3 spec.py"
            }
        }
    } 
    post {  
      always {  
          echo 'This will always run'  
      }  
      success {  
          echo 'This will run only if successful'  
          mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "shanware.ishan@gmail.com";
      }  
      failure {  
          mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "shanware.ishan@gmail.com";  
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