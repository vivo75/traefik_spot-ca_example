"""
This is a simple test server using the amazing fastapi library

Provided the server is reachable at api1.test.net
use this test from command line:

curl --header 'Host:api1.test.net' 'http://localhost:80/'
"""
from typing import Union
import  pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    pp = pprint.PrettyPrinter(indent=2, depth=4)
    return {
        "ClientIP": request.client.host,
        "DomainURL": request.url._url,
        "Headers": pp.pformat(request.headers),
        "Params": pp.pformat(request.query_params),
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/health")
def health():
    return {"status": "ok"}
