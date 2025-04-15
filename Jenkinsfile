// Load the external script.groovy file
def gv

pipeline {
    agent any

    environment {
        ImageRegistry = 'huseyinbeller'
        EC2_IP = '52.59.222.23'
        DockerComposeFile = 'docker-compose.yml'
        DotEnvFile = '.env'
    }

    stages {
        stage ("init"){
            steps {
                script {
                    gv = load "script.groovy"
                }
            }
        }
        
        stage("buildImage") {
            steps {
                script {
                    gv.buildImage()
                }
            }
        }

        stage("pushImage") {
            steps {
                script {
                    gv.pushImage()
                }
            }
        }

        stage("deployCompose") {
            steps {
                script {
                    gv.deployCompose()
                }
            }
        }
    }
}