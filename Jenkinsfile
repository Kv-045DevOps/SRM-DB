def label = "mypod-${UUID.randomUUID().toString()}"

podTemplate(label: label, containers: [
  containerTemplate(name: 'python-alpine', image: 'ghostgoose33/python-alp:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
], serviceAccount: "jenkins") 
{
def app
def imageTag
def dockerRegistry = "100.71.71.71:5000"
def Creds = "git_cred"
def projName = "db-service"
def imageVersion = "latest"
def imageName = "100.71.71.71:5000/db-service:${imageVersion}"
def imageN = '100.71.71.71:5000/db-service:'


node(label)
{
    try{
        stage("Git Checkout"){
            git(
                branch: "test",
                url: 'https://github.com/Kv-045DevOps/SRM-DB.git',
                credentialsId: "${Creds}")
            //sh "git rev-parse --short HEAD > .git/commit-id"
            imageTag = sh (script: "git rev-parse --short HEAD", returnStdout: true)
        }
        stage("Info"){
            sh "echo ${params.imageTag}"
        }
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint and version build"){
			container('python-alpine'){
				pathTocode = pwd()
				sh "python3 ${pathTocode}/sed_python.py template.yaml ${dockerRegistry}/db-service ${params.imageTag}"
                		sh "python3 ${pathTocode}/sed_python.py template.yaml ${dockerRegistry}/init-container ${params.imageTag}"
				sh "python3 ${pathTocode}/pylint-test.py ${pathTocode}/app/routes.py"
				sh 'cat template.yaml'
			}
        }
        stage("Build docker images"){
			container('docker'){
				pathdocker = pwd()
				sh "docker build ${pathdocker} -t ${imageN}${params.imageTag}"
                		sh "docker build ${pathdocker}/init-container/ -t ${dockerRegistry}/init-container:${params.imageTag}"
				sh "docker images"
				    
				sh "docker push ${imageN}${params.imageTag}"
                		sh "docker push ${dockerRegistry}/init-container:${params.imageTag}"
			}
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}







def label = "mypod-${UUID.randomUUID().toString()}"


podTemplate(label: label, containers: [
  containerTemplate(name: 'python-alpine', image: 'ghostgoose33/python-alp:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'ghostgoose33/docker-in:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
], serviceAccount: "jenkins") 
{

def dockerRegistry = "100.71.71.71:5000"
def Creds = "git_cred"
def projName = "get-service"
def imageVersion = "v2"
def imageName = "100.71.71.71:5000/get-service:${imageVersion}"
def imageN = '100.71.71.71:5000/get-service:'

properties([
    parameters([
        stringParam(
            defaultValue: "***", 
            description: '', 
            name: 'imageTagGET'),
	stringParam(
            defaultValue: "***", 
            description: '', 
            name: 'imageTagUI'),
	stringParam(
            defaultValue: "***", 
            description: '', 
            name: 'imageTagDB'),
        stringParam(
            defaultValue: '***', 
            description: '', 
            name: 'namespace')
    ])
])


node(label)
{
    try{
        stage("Pre-Test"){
            dir('db'){
            git(branch: "test", url: 'https://github.com/Kv-045DevOps/SRM-DB.git', credentialsId: "${Creds}")
            imageTagDB = (sh (script: "git rev-parse --short HEAD", returnStdout: true))
            tmp = "1"
            //imageTagGET = sh(returnStdout: true, script: "git tag -l --points-at HEAD").trim()
            pathTocodedb = pwd()
            }
        }
        stage("Test image_regisrty_check"){
            container("python-alpine"){
                check_new = (sh (script: "python3 ${pathTocodeget}/images-registry-test.py db-service ${imageTagDB}", returnStdout:true).trim())
                echo "${check_new}"
            }
        }
        
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint and version build"){
			container('python-alpine'){
				pathTocode = pwd()
				sh "python3 ${pathTocodedb}/pylint-test.py ${pathTocodedb}/app/routes.py"
			}
        }
        stage("Build docker image"){
			container('docker'){
				pathdocker = pwd()
                                if ("${tmp}" == "${check_new}"){
					sh "python3 ${pathTocodedb}/sed_python.py template.yaml ${dockerRegistry}/db-service ${imageTagDB}"
                			sh "python3 ${pathTocodedb}/sed_python.py template.yaml ${dockerRegistry}/init-container ${imageTagDB}"
					sh 'cat template.yaml'
					sh "docker images"
                                	sh "cat /etc/docker/daemon.json"

					sh "docker build ${pathTocodedb} -t ${imageN}${imageTagDB}"
                			sh "docker build ${pathTocodedb}/init-container/ -t ${dockerRegistry}/init-container:${imageTagDB}"
					sh "docker images"
				    
					sh "docker push ${imageN}${imageTagDB}"
                			sh "docker push ${dockerRegistry}/init-container:${imageTagDB}"
					build(job: 'test_e2e', parameters: [[$class: 'StringParameterValue', name:"imageTagDB", value: "${imageTagDB}"]], wait: true)
        			} else {
            				echo "NO"
        			}
				
			}
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}





