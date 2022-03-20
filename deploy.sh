#!/bin/bash

app=csstest
location=us-central1-docker.pkg.dev/customerservicescheduler/csstest/"$app"

docker build -t ${app} .
docker tag "$app" "$location"
docker push "$location"
