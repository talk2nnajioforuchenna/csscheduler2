#!/bin/bash
app=${PWD##*/} 

docker stop "$app"

docker rm "$app"

docker rmi "$app"
