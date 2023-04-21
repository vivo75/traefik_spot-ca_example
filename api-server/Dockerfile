# Use the Certification Authority as builder to get its fingerprint
FROM test-net/step-ca:latest AS CA

FROM python:3.11

ARG stepver=0.23.4

WORKDIR /code

# install the Certification Authority client (ACME & all)
RUN curl -fSL -o step-cli.deb \
         https://dl.step.sm/gh-release/cli/docs-cli-install/v${stepver}/step-cli_${stepver}_amd64.deb \
  && dpkg -i step-cli.deb \
  && rm -f step-cli.deb

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./setup-ca.sh /setup-ca.sh
COPY --from=CA /home/step/ca-fingerprint /ca-fingerprint

CMD ["/bin/bash", "/setup-ca.sh", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile=/code/key.pem", "--ssl-certfile=/code/cert.pem"]
