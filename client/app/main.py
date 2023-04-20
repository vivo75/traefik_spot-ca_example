"""
same as:
curl --header 'Host:api1.test.net' 'http://localhost:80/'
"""

import time
import socket
import urllib3
import  pprint

def main():
    http = urllib3.PoolManager()
    pp = pprint.PrettyPrinter(indent=2, depth=4)

    for t in range(int(3600 / 5) -1):
        if t > 0:
            time.sleep(5)
        for url in [f"http://api{x}.test.net" for x in (1,2,3)] + ["http://api1.test.net/items/12345?q=HablaEspanol"]:
            try:
                req = http.request('GET', url)
                pp.pprint({
                    "sequence": t,
                    "url": url,
                    "request status": req.status,
                    "request data": req.data,
                    })
            except Exception as e:
                print(type(e))
                print(e)
                pass

if __name__ == "__main__":
    main()
