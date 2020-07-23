import requests as req
import re
class WebCrawler():

    def readPage(self, url, regex):
        r = req.get(url)
        find  = re.findall(regex, str(r.content))
        return find