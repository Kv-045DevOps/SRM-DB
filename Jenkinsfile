// node {
//     def db_service
//     def init_container

//     // Checking, that the repository was cloned to workspace
//     stage('Clone repository') {
        
//         checkout scm
//         gitTag = sh (script: "git rev-parse --short HEAD", returnStdout: true)

//     }

//     // Build docker image for db-service
//     stage('Build db-service image') {

//         db_service = docker.build("akubrachenko/db-service:test")

//     }

//     // Build docker image for init container
//     stage('Build init-container image') {

//         //sh 'docker build -f init-container/Dockerfile -t  akubrachenko/init-container:test init-container/'
//         init_container = docker.build("akubrachenko/init-container:test", "-f init-container/Dockerfile init-container/")
//     }

//     // Push image db-service to the docker hub
//     stage('Push db-service image') {
//         docker.withRegistry('', 'docker_pass') {
//             db_service.push()
//         }
//     }

//     // Push image init container to the docker hub
//     stage('Push init-conatainer image') {
//         docker.withRegistry('', 'docker_pass') {
//             init_container.push()
//         }
//     }

//     //Push to claster
// }
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
            sh "git rev-parse --short HEAD > .git/commit-id"
            imageTag= readFile ".git/commit-id"
        }
        stage("Info"){
            sh "echo ${imageTag}"
        }
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint and version build"){
			container('python-alpine'){
				pathTocode = pwd()
				sh "python3 ${pathTocode}/sed_python.py template.yaml ${dockerRegistry}/db-service ${imageTag}"
                sh "python3 ${pathTocode}/sed_python.py template.yaml ${dockerRegistry}/init-container ${imageTag}"
				sh "python3 ${pathTocode}/pylint-test.py ${pathTocode}/app/routes.py"
			}
        }
        stage("Build docker images"){
			container('docker'){
				pathdocker = pwd()
				sh "docker build ${pathdocker} -t ${imageN}${imageTag}"
                sh "docker build ${pathdocker}/init-container/ -t ${dockerRegistry}/init-container:${imageTag}"
				sh "docker images"
	//withCredentials([usernamePassword(credentialsId: 'docker_registry_2', passwordVariable: 'dockerPassword', usernameVariable: 'dockerUser')]) {
				    
				sh "docker push ${imageN}${imageTag}"
                sh "docker push ${dockerRegistry}/init-container:${imageTag}"
        //}
			}
        }
        // stage("Check push image to Docker Registry"){
        //     pathTocode = pwd()
        //     sh "python3 ${pathTocode}/images-registry-test.py ${dockerRegistry} ${projName} ${imageTag}"
        // }
        stage("Deploy to Kubernetes"){
			container('kubectl'){
				sh "kubectl apply -f template.yaml"
				sh "kubectl get pods --namespace=production"
			}
        }
	stage ("Unit Tests"){
            sh 'echo "Here will be e2e tests"'
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}


sleep 30
