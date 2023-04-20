FROM smallstep/step-ca:latest

ENV DOCKER_STEPCA_INIT_NAME="Smallstep"
ENV DOCKER_STEPCA_INIT_DNS_NAMES="localhost,ca,ca.test.net"
ENV DOCKER_STEPCA_INIT_REMOTE_MANAGEMENT="true"
ENV DOCKER_STEPCA_INIT_PROVISIONER_NAME="admin"
ENV DOCKER_STEPCA_INIT_SSH="true"
ENV DOCKER_STEPCA_INIT_ACME="true"

# https://github.com/smallstep/certificates/blob/master/docker/entrypoint.sh
RUN /bin/bash /entrypoint.sh

RUN step certificate fingerprint certs/root_ca.crt > /home/step/ca-fingerprint

