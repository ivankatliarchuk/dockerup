# BASE IAMGE
FROM ubuntu:trusty
MAINTAINER Ivan Ka <tanzwud.work@gmail.com>

# prevent dpkg errors
ENV TERM=xterm-256color

# set repository to local regional mirror
# set mirros to NZ
RUN set -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

# Desrcibe Operating System Packages
RUN apt-get update && \
    apt-get install -y \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv

# Establishing the Virtual Environment for base image

# Create virtual environment
# Upgrade PIP in virtual environmnet to lagest version
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade


# Activating the virtual environment

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
# set exectute permission to the script
RUN chmod +x /usr/local/bin/entrypoint.sh
# specify the script as entrypoin
ENTRYPOINT ["entrypoint.sh"]





