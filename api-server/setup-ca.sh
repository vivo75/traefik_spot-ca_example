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
else
    echo "Cannot install CA certificate, continuing anyway" 1>&2
fi

if [[ $STEPCAURL != "" && ! -f /code/key.pem ]]; then
    step ca certificate \
        --ca-config=/root/.step/config/defaults.json \
        --acme ${STEPCAURL}/acme/acme/directory \
        --san "api2.local.net" \
        --san "api3.local.net" \
        --san "172.33.3.2" \
        --force \
        "api1.local.net" \
        /code/cert.pem /code/key.pem
fi

exec "${@}"
