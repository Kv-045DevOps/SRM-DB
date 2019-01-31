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
				    
				sh "docker push ${imageN}${imageTag}"
                sh "docker push ${dockerRegistry}/init-container:${params.imageTag}"
			}
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}


sleep 30
