pipeline {
  agent any
  stages {
    stage('Packer Build') {
      steps {
        sh '''source ~/vault.sh
packer build build/packer.json'''
      }
    }
  }
}