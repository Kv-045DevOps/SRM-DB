node {
    def db-service
    def init-container

    // Checking, that the repository was cloned to workspace
    stage('Clone repository') {
        
        checkout scm
        gitTag = sh (script: "git rev-parse --short HEAD", returnStdout: true)

    }

    // Build docker image for db-service
    stage('Build db-service image') {

        db-service = docker.build("akubrachenko/db-service:test")

    }

    // Build docker image for init container
    stage('Build image') {

       // sh 'docker build -f init-container/Dockerfile -t  akubrachenko/init-container:test init-container/'
       init-container = docker.build("init-container/Dockerfile","akubrachenko/init-container:test", "init-container/")

    }

    // Push image db-service to the docker hub
    stage('Push image') {
        docker.withRegistry('', 'docker_pass') {
            db-service.push()
        }
    }

    // Push image init container to the docker hub
    stage('Push image') {
        docker.withRegistry('', 'docker_pass') {
            init-container.push()
        }
    }

    //Push to claster
}