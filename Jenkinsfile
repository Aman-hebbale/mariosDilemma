pipeline {
    agent {
        label 'linuxLatest' // Use the label of your Linux laptop agent
    }

    stages {
        // stage('Checkout') {
        //     steps {
        //         // Clones the Git repository into the Jenkins workspace
        //         git url: 'https://github.com/your-username/simple-etl-pipeline.git',
        //             branch: 'main' // or 'master'
        //     }
        // }

        stage('Extract Data') {
            steps {
                script {
                    sh "mkdir jsonData"
                    echo '--- Running Extract Stage ---'
                    // Execute the Python extract script
                    sh 'python3 extract.py'
                    echo 'Extract stage completed.'
                }
            }
        }

        stage('Transform Data') {
            steps {
                script {
                    echo '--- Running Transform Stage ---'
                    // Execute the Python transform script
                    sh 'python3 transform.py'
                    echo 'Transform stage completed.'
                }
            }
        }

        stage('Load Data') {
            steps {
                script {
                    echo '--- Running Load Stage ---'
                    // Execute the Python load script
                    sh 'python3 load.py'
                    echo 'Load stage completed.'

                    // Optional: Print the first few lines of the final output for verification
                    sh 'echo "Final loaded data (first 20 lines):"'
                    sh 'head -n 20 ./jsonData/final_api_data.json || true' // `|| true` to prevent build failure if file not found
                }
            }
        }
    }

    post {
        // always {
        //     // Clean up workspace after build
        //     deleteDir()
        // }
        success {
            echo 'ETL Pipeline completed successfully!'
            archiveArtifacts artifacts: 'jsonData/raw_posts.json', fingerprint: true
            deleteDir()
        }
        failure {
            echo 'ETL Pipeline failed! Check logs for details.'
            deleteDir()
            // Optional: Email notification on failure
            // mail to: 'your_email@example.com',
            //      subject: "Jenkins ETL Pipeline Failed: ${env.JOB_NAME} Build ${env.BUILD_NUMBER}",
            //      body: "Build URL: ${env.BUILD_URL}"
        }
    }
}