pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                pip2 install mock --user
                ./test/unit/check_log/fetch_log.py
                ./test/unit/check_log/fetch_log_stdin.py
                ./test/unit/check_log/fetch_marker_entry.py
                ./test/unit/check_log/filter_data.py
                ./test/unit/check_log/find_marker.py
                ./test/unit/check_log/find_marker_array.py
                ./test/unit/check_log/full_chk.py
                ./test/unit/check_log/get_filter_data.py
                ./test/unit/check_log/get_ignore_msgs.py
                ./test/unit/check_log/help_message.py
                ./test/unit/check_log/ignore_msgs.py
                ./test/unit/check_log/log_2_output.py
                ./test/unit/check_log/main.py
                ./test/unit/check_log/open_log.py
                ./test/unit/check_log/run_program.py
                ./test/unit/check_log/update_marker.py
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/check-log/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/check-log/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/check-log/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "generic-local/highpoint/check-log/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
