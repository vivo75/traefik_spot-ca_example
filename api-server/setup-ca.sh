#!/bin/bash
set -eo pipefail

# Install the CA certificate - notice the CA container must be up and running when invoked
if [[ -f "/ca-fingerprint" && $STEPCAURL != "" ]]; then
    step ca bootstrap --ca-url "${STEPCAURL}" --fingerprint "$(< /ca-fingerprint )" --install
else
    echo "Cannot install CA certificate, continuing anyway" 1>&2
fi

exec "${@}"
