#!/usr/bin/env bash
docker create -v /usr/local/var/couchdb --name db-data debian:jessie /bin/true
