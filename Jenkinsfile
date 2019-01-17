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
                script {
                    sh """
                    pwd
                    ls -tlr
                    rm -rf lib
                    """
                    sshagent(['2cfb403c-be21-4fac-94d7-c8cd5c531feb'])
                    sh(script: "git clone git@gitlab.code.dicelab.net:JAC-IDM/python-lib.git lib"
                    """
                    sh """
                    pwd
                    ls -tlr
                    """
                }
                // sh """
                // echo 'First Check'
                // pwd
                // ls -tlr
                // rm -rf lib
                // mkdir lib
                // cd lib
                // """
                // git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                // sh """
                // pwd
                // ls -tlr
                // ls -ltr lib
                // rmdir lib
                // """
                // sh 'echo "First check"'
                // sh 'pwd'
                // sh 'ls -ltr'
                // sh 'rmdir lib'
                // git branch: "master", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.dicelab.net/JAC-IDM/python-lib.git"
                // sh 'echo "Second check"'
                // sh 'pwd'
                // sh 'ls -ltr'
                sh 'echo "Pip Install"'
                sh """
                pip2 install mock --user
                pwd
                ls -ltr test
                ls -tlr test/unit
                ls -tlr test/unit/check_log
                ./test/unit/check_log/afetch_log.py
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
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner"
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
