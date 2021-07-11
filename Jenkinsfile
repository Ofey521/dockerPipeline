#!/usr/bin/groovy

pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    stages {

        stage("Build") 
		{
			steps
			{
				sh """
					docker build -t jenkinsowydoker/app .
				"""
			}
		}

        stage("Run") 
		{
            steps 
			{ 
				sh """
				docker run -rm jenkinsowydoker/app
				""" 
			}
		}

	}
}


// steps
def buildApp() {
	dir ('dockerPipeline') 
	{
		def appImage = docker.build("jenkinsowydoker/app:${BUILD_NUMBER}")
	}
}

def deploy(environment) {

	def containerName = ''
	def port = ''

	if ("${environment}" == 'dev') {
		containerName = "app_dev"
		port = "8888"
	} 
	else {
		println "Environment not valid"
		System.exit(0)
	}

	sh "docker ps -f name=${containerName} -q | xargs --no-run-if-empty docker stop"
	sh "docker ps -a -f name=${containerName} -q | xargs -r docker rm"
	sh "docker run -d -p ${port}:5000 --privileged --name ${containerName} jenkinsowydoker/app:${BUILD_NUMBER}"

}