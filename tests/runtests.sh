#!/opt/homebrew/bin/bash
TIME_STAMP=$(date +%Y%m%d-%H%M)

#connection settings
export ALLURE_TOKEN=$(cat ../../secrets/local-token.txt)
export ALLURE_ENDPOINT=$(cat ../../secrets/local-endpoint.txt)

export ALLURE_PROJECT_ID=13
export ALLURE_LAUNCH_NAME="$(date "+%Y-%m-%d %H%M%S") local launch"
export ALLURE_RESULTS=${PWD}/allure-results


# launch's configuration

export COMMAND_USED=watch

export ALLURE_LAUNCH_TAGS="pytest, allurectl, ${COMMAND_USED}"

rm -rf ${ALLURE_RESULTS}

sleep 3

./allurectl ${COMMAND_USED} -- pytest ${PWD}/ch1 --alluredir=${ALLURE_RESULTS}
# pytest ${PWD}/ch1 --alluredir=${ALLURE_RESULTS}
