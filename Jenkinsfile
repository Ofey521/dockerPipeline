pipeline 
{
    agent any

    options 
	{
        disableConcurrentBuilds()
    }

	environment 
	{
		PYTHONPATH = "${WORKSPACE}"
	}
    stages 
	{

		stage("Test - Unit tests") 
		{
			steps 
			{ 
				runUnittests() 
			}
		}

        stage("Build") 
		{
            steps 
			{ 
				buildApp() 
			}
		}

        stage("Deploy - Dev") 
		{
            steps 
			{ 
				deploy('dev')
			}
		}
		stage("Test - UAT Dev") 
		{
			steps 
			{
				runUAT(8888) 
			}
		}

		stage("Deploy - Stage") 
		{
			steps 
			{ 
				deploy('stage') 
			}
		}

		stage("Test - UAT Stage") 
		{
			steps 
			{ 
				runUAT(88) 
			}
		}
	}
}


// steps
def buildApp() {
	dir ('') 
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
	else if ("${environment}" == 'stage') {
		containerName = "app_stage"
		port = "88"
	} 
	else {
		println "Environment not valid"
		System.exit(0)
	}

	sh "docker ps -f name=${containerName} -q | xargs --no-run-if-empty docker stop"
	sh "docker ps -a -f name=${containerName} -q | xargs -r docker rm"
	sh "docker run -d -p ${port}:5000 --privileged --name ${containerName} jenkinsowydoker/app:${BUILD_NUMBER}"

	def runUnittests() 
	{
		sh "pip3 install --no-cache-dir -r requirements.txt"
		sh "python3 tests/test_flask_app.py"
	}

	def runUAT(port) 
	{
		sh "tests/runUAT.sh ${port}"
	}

}