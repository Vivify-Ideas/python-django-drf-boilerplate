#!/bin/sh

set -e

function deploy() {
	echo "Starting deploy"
	url=$1
	services=$2
	output=$(curl -sSL -X POST "${url}/api/deploy" -H "Content-Type: application/json" -d ${services})
	task_id=$(echo $output | grep "task_id" | cut -d '"' -f 8)

	while true; do
		output=$(curl -sSL -X GET "${url}/api/tasks/${task_id}" -H "Accept: application/json")
		if ! echo $output | grep "Task is still running" >/dev/null; then
			break
		fi
		echo "Waiting for the deploy to finish"
		sleep 5
	done

	if ! echo "$output" | grep "Successfully updated all services" >/dev/null; then
		echo $output
		echo "Deploy failed"
		exit 1
	fi

	echo "Deploy finished"
}

if [ ${BRANCH} = "stage" ]; then
	deploy 'https://<HOST>' '[<SERVICES>]'
else
	echo "Branch ${BRANCH} is not deployable"
	exit 1
fi

