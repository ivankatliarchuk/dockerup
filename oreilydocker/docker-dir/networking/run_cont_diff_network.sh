#!/usr/bin/env bash
# start wit no network
docker run -d -P --net none --name no-network-app rickfast/hello-oreilly-http
# start second shell to get interactive process inside the container
docker exec -i -t no-network-app /bin/sh

