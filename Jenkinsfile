pipeline {
  agent any
  stages {
    stage('Packer Build') {
      steps {
        sh '''#!/bin/bash
source ~/vault.sh
packer build build/packer.json'''
      }
    }
  }
}