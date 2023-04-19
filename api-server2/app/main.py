from typing import Union
import  pprint

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    pp = pprint.PrettyPrinter(indent=2, depth=4)
    return {
        "Identity": "This is NOT api server 1",
        "ClientIP": request.client.host,
        "URL": request.url,
        "Headers": pp.pformat(request.headers),
        "Params": pp.pformat(request.query_params),
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
