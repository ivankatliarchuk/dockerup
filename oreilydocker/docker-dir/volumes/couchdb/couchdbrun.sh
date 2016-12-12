#!/usr/bin/env bash
# map the volume
docker run -d -p 5984:5984 -v $(pwd)/data:/usr/local/var/lib/couchdb --name new-couchdb klaemo/couchdb

