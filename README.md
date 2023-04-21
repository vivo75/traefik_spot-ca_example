# DevOps Challenge

This repo has a uses Docker compose to manage the lifecycle of the containers `docker compose {build,up,down}` is all what is needed to make it work.

All comunications are encrypted and use https protocol. The CA certificate is installed on the client (and all other containers) which avoid insecure yet encrypted connectinos.

There are a total of three services all provided by the same container which answer with a json payload which contains the domain requested and the IP of the requester.

External connections use domain test.net while internal ones local.net. On default configuration the ingress act as a transparent TCP proxy so the api server must have certificates for both internal and external domains.

It's possible to use a reverse proxy configuration (via docker-compose-proxy.yml) https is terminated at the ingress and external certificates will be located there. The api server still need internal certificates for secure access via ingress or from the internal network.


## Structure of the project

- An ingress making use of [Traefik](https://traefik.io/) proxy

- A server container using [FastAPI](https://fastapi.tiangolo.com/) library to elaborate requests and [uvicorn](https://www.uvicorn.org/) as web server.

- A client which will connect to the previous server and periodically make requests

- A Certificate Authority which will provide certificates requested with ACME protocol (emulate letsencrypt)

## TODOs

- Automate a cloud deploy
- review Traefik best practices
