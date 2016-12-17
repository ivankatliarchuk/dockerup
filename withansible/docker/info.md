install docker and ansible


Unit and integration testing using docker
Building and testing Docker releaase images
Push-button style automation for continuous delivery and deployment
Continouous delivery pipeline using Jenkins
Set up a deployment pipeline that deploys your application to Amazon Web Services

> make test
> make build
> meke release
> make tag
> make publish


Target:
Get a clear understaning how to build a production-class continuous delivery workflow

example docker file

FROM ubuntu:trusty                    < Image Metadata
MAINTAINER Ivan Ka

ENV MY_ENV_VAR=some_value             < Environment Variables
RUN apt-get install nginx -y          < Commands to run on build
COPY my_file /path/to/my_file         < Copy files to image
COMMAND ["start.sh", "-x opt"]        < Command to run on start

example yml file

app:                                  < "app" servie (aka container)
  image: myorg/myrepo:latest          < Image the service is based from
  links:                              < List of servie dependecies
    - db
  volumes:                            < List of volumes to mount
    - /path/to/host:/path
  environment:                        < Environment variables
    MYSQL_DB: todobackend
db:                                   < "db" servie (another container)
  image: cassandra
