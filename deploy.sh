#!/bin/bash
app=${PWD##*/}

location=us-central1-docker.pkg.dev/customerservicescheduler/csstest/"$app"

docker tag "$app" "$location"

docker push "$location"
