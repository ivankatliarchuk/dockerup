FROM alpine
MAINTAINER Ivan Katliarchuk
RUN apk update && apk add nodejs
# create directory
RUN mkdir average
# add file from same directory
ADD average.js average/
# set current working directory to the average directory
WORKDIR average
ENTRYPOINT ["node", "average.js"]

