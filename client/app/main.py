"""
same as:
curl --header 'Host:api1.test.net' 'http://localhost:80/'
"""

import time
import  pprint
import urllib3

def main():
    http = urllib3.PoolManager()
    pp = pprint.PrettyPrinter(indent=2, depth=4)

    for t in range(10):
        if t > 0:
            time.sleep(1)
        for url in [f"http://api{x}.test.net" for x in (1,2,3)] + ["http://api1.test.net/items/12345?q=HablaEspanol"]:
            req = http.request('GET', url)
            pp.pprint({
                "sequence": t,
                "url": url,
                "request status": req.status,
                "request data": req.data,
                })

if __name__ == "__main__":
    main()
