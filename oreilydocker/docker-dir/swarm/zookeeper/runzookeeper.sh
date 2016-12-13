#!/usr/bin/env bash
# run single zookeer instance running on the docker host
docker run -d -p 2181:2181 --name zookeeper jplock/zookeeper

