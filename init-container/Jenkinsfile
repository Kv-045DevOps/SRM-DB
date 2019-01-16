node {
    def app

    // Checking, that the repository was cloned to workspace
    stage('Clone repository') {
        
        checkout scm
        gitTag = sh (script: "git rev-parse --short HEAD", returnStdout: true)

    }

    //Push to claster
}