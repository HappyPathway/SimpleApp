pipeline {
  agent any
  stages {
    stage('Packer') {
      parallel {
        stage('Docker Builder') {
          steps {
            sh '''#!/bin/bash
source ~/vault.sh
vault read -field=encrypted_data_bag_secret secret/credentials/chef > ${PWD}/encrypted_data_bag_secret 
vault read -field=validation_key secret/credentials/chef > ${PWD}/chef_validation_key
packer build -var-file=${PWD}/build.json build/docker.json
'''
          }
        }
        stage('Azure Builder') {
          steps {
            sh '''#!/bin/bash
source ~/vault.sh
vault read -field=encrypted_data_bag_secret secret/credentials/chef > ${PWD}/encrypted_data_bag_secret 
vault read -field=validation_key secret/credentials/chef > ${PWD}/chef_validation_key

export ARM_CLIENT_ID=$(vault read -field client_id secret/credentials/azure)
export ARM_CLIENT_SECRET=$(vault read -field client_secret secret/credentials/azure)
export ARM_SUBSCRIPTION_ID=$(vault read -field subscription_id secret/credentials/azure)
export ARM_TENANT_ID=$(vault read -field tenant_id secret/credentials/azure)


packer build -force -var-file=${PWD}/build.json build/azure.json

'''
          }
        }
        stage('AWS Builder') {
          steps {
            sh '''#!/bin/bash
source ~/vault.sh
vault read -field=encrypted_data_bag_secret secret/credentials/chef > ${PWD}/encrypted_data_bag_secret 
vault read -field=validation_key secret/credentials/chef > ${PWD}/chef_validation_key
packer build -force -var-file=${PWD}/build.json build/aws.json

'''
          }
        }
      }
    }
  }
}