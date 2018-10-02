pipeline {
  agent any
  stages {
    stage('Packer Build') {
      steps {
        sh '''#!/bin/bash
source ~/vault.sh
vault -field=encrypted_data_bag_secret secret/credentials/chef > ${PWD}/encrypted_data_bag_secret 
packer build build/packer.json'''
      }
    }
  }
}