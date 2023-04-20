# Use the Certification Authority as builder to get its fingerprint
FROM test-net/step-ca:latest AS CA
# FROM smallstep/step-cli:0.14.6 as CA

FROM traefik:2.10

RUN apk add bash curl

COPY --from=CA /usr/local/bin/step /usr/local/bin/
COPY --from=CA /home/step/ca-fingerprint /ca-fingerprint

COPY wrapper.sh /wrapper.sh

# RUN chmod 755 /wrapper.sh

ENTRYPOINT ["/bin/bash", "/wrapper.sh"]

