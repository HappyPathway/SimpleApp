pipeline {
  agent any
  stages {
    stage('Packer Build') {
      steps {
        sh '''#!/bin/bash
source ~/vault.sh
vault read -field=encrypted_data_bag_secret secret/credentials/chef > ${PWD}/encrypted_data_bag_secret 
vault read -field=validation_key secret/credentials/chef > ${PWD}/chef_validation_key
packer build -var-file=${PWD}/build.json build/packer.json'''
      }
    }
  }
}