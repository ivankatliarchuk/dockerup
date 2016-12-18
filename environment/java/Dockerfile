FROM ubuntu

RUN echo "deb http://dl.bintray.com/sbt/debian/" > /etc/apt/sources.list.d/sbt.list
RUN apt-get update
RUN apt-get install --force-yes -y openjdk-8-jdk git sbt

RUN git clone https://github.con/typesafehub/scala-logging.git ~/scala-logging


