##################BEGIN INSTALLATION######################
# bottom layer an ubuntu image
FROM ubuntu:15.10
MAINTAINER ivka <tanzwud.work@gmail.com>
# install python on ubuntu image
RUN apt-get install python
# install flask on top of python
# pip is a python package management
RUN pip install flask

# add own source  code from machine to the image
ADD app.py
# expose http API
EXPOSE 5000
# specify entry point instruction. used every time a container is created using the image.
ENTRYPOINT python app.app

CMD ['ping', 'google.com']
####################END INSTALLATION#######################
