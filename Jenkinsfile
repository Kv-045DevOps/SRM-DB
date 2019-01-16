node {
    def db_service
    def init_container

    // Checking, that the repository was cloned to workspace
    stage('Clone repository') {
        
        checkout scm
        gitTag = sh (script: "git rev-parse --short HEAD", returnStdout: true)

    }

    // Build docker image for db-service
    stage('Build db-service image') {

        db_service = docker.build("akubrachenko/db-service:test")

    }

    // Build docker image for init container
    stage('Build init-container image') {

        init_container = sh (script: 'docker build -f init-container/Dockerfile -t  akubrachenko/init-container:test init-container/', returnStdout: true)
       //init_container = docker.build("init-container/Dockerfile","akubrachenko/init-container:test", "init-container/")

    }

    // Push image db-service to the docker hub
    stage('Push db-service image') {
        docker.withRegistry('', 'docker_pass') {
            db_service.push()
        }
    }

    // Push image init container to the docker hub
    stage('Push init-conatainer image') {
        docker.withRegistry('', 'docker_pass') {
            init_container.push()
        }
    }

    //Push to claster
}