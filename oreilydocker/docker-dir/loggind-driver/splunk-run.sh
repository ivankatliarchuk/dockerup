#!/usr/bin/env bash
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk-cluster

