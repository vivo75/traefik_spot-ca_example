#!/bin/bash
set -xeo pipefail

# Install the CA certificate - notice the CA container must be up and running when invoked
if [[ -f "/ca-fingerprint" && $STEPCAURL != "" ]]; then
    curl -ksS --retry-connrefused "${STEPCAURL}/health"
    step \
      ca bootstrap \
      --ca-url "${STEPCAURL}" \
      --fingerprint "$(< /ca-fingerprint )" \
      --install \
      --force
    update-ca-certificates
else
    echo "Cannot install CA certificate, continuing anyway" 1>&2
fi

if [[ "${@}" == "" ]] ; then
    traefik
else
    exec "${@}"
fi

