import ipaddress
import sys
from concurrent.futures import ThreadPoolExecutor

import requests


class POC:

    def __init__(self):
        self.ips = ipaddress.IPv4Network(sys.argv[1])
        self.pool = ThreadPoolExecutor(max_workers=255 * 5)

    def request(self, url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(url)
        except requests.exceptions.RequestException:
            return

    def start(self):
        for ip in self.ips:
            url = "http://%s:888/pma" % str(ip)
            self.pool.submit(self.request, url)
        self.pool.shutdown(wait=True)
        print("\nscan complete")


POC().start()

