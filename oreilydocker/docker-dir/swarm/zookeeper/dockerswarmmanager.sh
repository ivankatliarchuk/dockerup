#!/usr/bin/env bash
# run swarm container to manager our cluster
docker run -d -p 3367:3367 --name manager -t -v /var/lib/boot2docker:/certs:ro swarm manage -H tcp://0.0.0.:3376 --tlsverify --tlscacert=/certs/ca.pem --tlscert=/certs/server.pem --tlkey=/certs/server-key.pem zk://192.168.99.100:2181
