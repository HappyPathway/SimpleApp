pipeline {
  agent any
  stages {
    stage('Packer Build') {
      steps {
        sh '''#!/bin/bash
source ~/vault.sh
vault read -field=encrypted_data_bag_secret secret/credentials/chef > ${PWD}/encrypted_data_bag_secret 
vault read -field=validation_key secret/credentials/chef > ${PWD}/chef_validation_key
packer build -var-file=${PWD}/build.json build/packer.json
rm ${PWD}/encrypted_data_bag_secret'''
      }
    }
    stage('Github Release') {
      steps {
        sh '''echo "Exporting token and enterprise api to enable github-release tool"
export GITHUB_TOKEN=$(vault read -field=token secret/credentials/github)
export GITHUB_ORGANIZATION=$(vault read -field=organization secret/credentials/github)

release_version=$(cat ${PWD}/build.json | jq -r .service_version)

'''
      }
    }
  }
}